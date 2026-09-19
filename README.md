# Prompt Injection Detector

## Overview

Prompt Injection Detector is a rule-based prompt injection detection
prototype designed to identify suspicious instructions
and potential prompt injection attempts in LLM applications.

This project will gradually evolve into a data-driven,
machine learning-based security system.

## Current Features

- Regex-based prompt detection
- Suspicious keyword detection
- Attack category identification
- Risk level classification
- Detection reasons
- Latency measurement
- Interactive command-line interface

## Technologies Used

- Python
- Regular Expressions
- Object-Oriented Programming
- Rule-Based Detection

## How to Run

1. Clone the repository.
2. Navigate to the project directory.
3. Run the following command:

   python detector.py

4. Enter a prompt to view the detection result.
5. Type `exit` to close the program.

## Limitations

This prototype uses predefined rules and keywords.
It cannot detect every type of prompt injection attack.

A SAFE result only means that no configured pattern
was detected.

## Future Improvements

- Dataset collection and labeling
- Exploratory Data Analysis
- Machine Learning-based detection
- Semantic analysis
- FastAPI backend
- Web dashboard
- Docker and deployment

## Project Status

Version 0.1 - Initial Rule-Based Prototype
