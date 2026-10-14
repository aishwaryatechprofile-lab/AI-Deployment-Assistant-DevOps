

import json
import os
import shutil
import subprocess
import pickle
from sklearn.tree import DecisionTreeClassifier
# Run an external command safely
def run_command(command):
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=30,
            check=False
        )

        print("Command output:", result.stdout)
        print("Error output:", result.stderr)
        print("Return code:", result.returncode)

        return result.returncode == 0

    except subprocess.TimeoutExpired:
        print("Command timed out!")
        return False
# Test command execution


# Training examples for deployment risk prediction
X = [
    [2, 95, 0],
    [5, 90, 0],
    [8, 85, 0],
    [12, 70, 0],
    [15, 60, 1],
    [25, 40, 2],
    [30, 30, 3],
    [5, 40, 0],
    [10, 90, 2],
    [25, 85, 0]
]

# Expected risk categories for the examples
y = [
    "LOW",
    "LOW",
    "LOW",
    "MEDIUM",
    "HIGH",
    "HIGH",
    "HIGH",
    "MEDIUM",
    "HIGH",
    "MEDIUM"
]

# Train the decision tree model
model = DecisionTreeClassifier(random_state=42)
model.fit(X, y)

print("Deployment risk ML model trained successfully!")

# Load environment configuration
with open("config.json", "r") as file:
    config = json.load(file)

# Create folders for simulated deployments
os.makedirs("deployments", exist_ok=True)
os.makedirs("releases", exist_ok=True)

print("=" * 45)
print("     AI DEPLOYMENT ASSISTANT DEVOPS")
print("=" * 45)
print("\n1. View Environment Configuration")
print("2. Assess Deployment Risk")
print("3. Simulate Deployment")
print("4. Rollback Deployment")
print("5. Run Automated Tests")
print("6. Exit")

choice = input("\nEnter your choice: ")

# Feature 1: Environment configuration
if choice == "1":
    print("\nAvailable Environments:")

    for key, value in config.items():
        print(key, "-", value["name"])

    env = input("\nChoose environment (dev/staging/prod): ").lower()

    if env in config:
        print("\nEnvironment Details")
        print("Name:", config[env]["name"])
        print("Version:", config[env]["version"])
        print("Debug:", config[env]["debug"])
    else:
        print("Invalid environment!")

# Feature 2: Deployment risk assessment
elif choice == "2":
    changes = int(input("Number of changed files: "))
    coverage = float(input("Test coverage percentage (0-100): "))
    failed_tests = int(input("Number of failed tests: "))

    if not 0 <= coverage <= 100 or changes < 0 or failed_tests < 0:
        print("Invalid input values!")
    else:
        risk = 0

        if changes > 20:
            risk += 30
        elif changes > 10:
            risk += 20
        elif changes > 5:
            risk += 10

        if coverage < 50:
            risk += 30
        elif coverage < 80:
            risk += 15

        risk += min(failed_tests * 15, 40)
        risk = min(risk, 100)

        print("\nDeployment Risk Score:", risk, "/ 100")

        prediction = model.predict([[changes, coverage, failed_tests]])

        print("ML Predicted Risk Level:", prediction[0])
# Feature 3: Simulated deployment
elif choice == "3":
    env = input("Choose environment (dev/staging/prod): ").lower()

    if env not in config:
        print("Invalid environment!")
    elif env == "prod":
        print("Production deployment is disabled in this demo.")
        print("Use dev or staging for simulation.")
    else:
        version = input("Enter version to deploy: ").strip()

        if not version:
            print("Version cannot be empty!")
        else:
            target = os.path.join("deployments", env)
            os.makedirs(target, exist_ok=True)

            version_file = os.path.join(target, "version.txt")

            # Save the previous version for rollback
            if os.path.exists(version_file):
                shutil.copy2(
                    version_file,
                    os.path.join(target, "previous_version.txt")
                )

            with open(version_file, "w") as file:
                file.write(version)

            print("\nDeployment simulated successfully!")
            print("Environment:", config[env]["name"])
            print("Deployed version:", version)

# Feature 4: Rollback simulation
elif choice == "4":
    env = input("Choose environment (dev/staging): ").lower()

    if env not in ["dev", "staging"]:
        print("Invalid environment!")
    else:
        target = os.path.join("deployments", env)
        current = os.path.join(target, "version.txt")
        previous = os.path.join(target, "previous_version.txt")

        if os.path.exists(previous):
            shutil.copy2(previous, current)

            with open(current, "r") as file:
                version = file.read()

            print("Rollback simulation completed!")
            print("Restored version:", version)
        else:
            print("No previous version available.")
            print("Deploy at least two versions first.")
            # Feature 5: Run automated tests
elif choice == "5":
    print("\nRunning automated tests...")
    run_command(["python", "-m", "unittest", "test_deployment", "-v"])
elif choice == "6":
    print("Exiting Deployment Assistant.")

else:
    print("Invalid choice. Please choose 1 to 5.")