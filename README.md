# Python Mini Exception Handling Examples

This repository contains three Python scripts that demonstrate how to create and use custom exceptions. These examples include handling negative ages, maintaining a minimum account balance, and validating simple calculator input.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Negative Age Exception](#negative-age-exception)
 


## Introduction

This project includes three mini Python scripts that implement custom exception handling:
1. **Negative Age Exception**: Handles invalid age inputs and classifies age stages.
2. **Account Balance Exception**: Ensures that account withdrawals do not reduce the balance below a minimum threshold.
3. **Simple Calculator with Exception Handling**: Validates and evaluates simple arithmetic expressions.

## Features

- **Custom Exceptions**: Learn how to define and raise custom exceptions in Python.
- **Age Classification**: Classifies life stages based on age input.
- **Balance Management**: Maintains minimum account balance during withdrawals.
- **Calculator Validation**: Ensures valid arithmetic expression input.

## Installation



Clone the repository and navigate to the project directory:

```bash
git clone https://github.com/Rakshitachadalawada/Python-Custom-Exceptions-Mini-Projects.git
cd Python-Custom-Exceptions-Mini-Projects
## Usage

### Negative Age Exception

Use this script to classify age stages and handle invalid age inputs:

```python
from MiniUserDefinedExceptions import stage

try:
    age = int(input("Enter age: "))
    stage(age)
except (ValueError, NegativeAgeException) as e:
    print(e)


