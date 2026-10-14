import unittest
import subprocess
import json


class TestDeployment(unittest.TestCase):

    def test_python_version_check(self):
        result = subprocess.run(
            ["python", "--version"],
            capture_output=True,
            text=True
        )
        self.assertEqual(result.returncode, 0)

    def test_environment_configuration(self):
        with open("config.json", "r") as file:
            config = json.load(file)

        self.assertIn("dev", config)
        self.assertIn("staging", config)
        self.assertIn("prod", config)


if __name__ == "__main__":
    unittest.main()