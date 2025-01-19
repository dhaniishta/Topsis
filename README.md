# TOPSIS-Method-Implementation

This repository contains a Python program that implements the **TOPSIS (Technique for Order Preference by Similarity to Ideal Solution)** method. The program reads an input dataset, applies the TOPSIS method, and generates an output CSV file with the calculated TOPSIS scores and rankings.

## Project Overview

TOPSIS is a method used to rank alternatives based on their proximity to the ideal solution. The alternatives are evaluated based on multiple criteria (e.g., cost, efficiency, etc.), and the method computes a score that reflects how close each alternative is to the ideal solution.

### Input:
- An input CSV file containing decision matrix data (alternatives and their criteria).
- Weights for each criterion.
- Impacts for each criterion (`+` for benefit and `-` for cost).

### Output:
- An output CSV file with the original data along with two new columns:
  - **Topsis Score**: The calculated TOPSIS score for each alternative.
  - **Rank**: The rank of each alternative based on the TOPSIS score (higher score means better rank).

### Usage:
git clone https://github.com/your-username/your-repository.git
cd your-repository

