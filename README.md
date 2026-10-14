# AI Deployment Assistant DevOps

## Project Overview
AI Deployment Assistant DevOps is a Python-based project that demonstrates deployment configuration, risk assessment, machine-learning risk prediction, automated testing, simulated deployment, and rollback.

## Features
- Environment configuration using JSON
- Rule-based deployment risk scoring
- Machine-learning risk prediction using a Decision Tree Classifier
- External command execution using subprocess
- Automated testing using unittest
- Simulated deployment for Development and Staging
- Rollback to a previously saved version
- Production deployment disabled for safety in this demo

## Technologies Used
- Python
- scikit-learn
- PyYAML
- JSON
- subprocess
- unittest

## Requirements
Python 3.13 or a compatible version.

Install the required packages:

`pip install -r requirements.txt`

## How to Run
1. Open the project folder in a terminal.
2. Run:

   `python AI_dep_as_devops.py`

3. Select an option from the displayed menu.

## Run Automated Tests
Run:

`python -m unittest test_deployment -v`

The tests check Python command execution and the required environment configuration.

## Important Note
This is an educational demonstration. Deployment and rollback are simulated locally; the project does not deploy to a real server. The machine-learning model uses illustrative sample training data and is not validated for production use.

## Author
Aishwarya Acharya
