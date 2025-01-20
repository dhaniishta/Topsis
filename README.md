# Topsis-Dhanishta-102203520

This package implements the Topsis method for decision-making.
# Topsis Implementation and Python Package

This repository contains the implementation of the **TOPSIS** (Technique for Order Preference by Similarity to Ideal Solution) method as a Python program and package. The project is divided into two main parts:

1. **Program 1:** A command-line Python program to compute TOPSIS scores and rankings.
2. **Program 2:** A reusable Python package for TOPSIS calculations, published on PyPi.

---

## **Program 1: Command-Line Python Program**

### **Usage**
The program computes the TOPSIS score and rank for alternatives provided in a CSV file. 

### **Input File Requirements**
- The input file must be a CSV file containing three or more columns.
  - The **first column** should contain the names of the alternatives (e.g., M1, M2, M3, ...).
  - The **remaining columns** should contain numeric values only (criteria values).
  
### **Output File**
- The output will include all columns from the input file, with two additional columns:
  - **Topsis Score**
  - **Rank**

### **Running the Program**
Run the program through the command line using the following format:
```bash
python <RollNumber>.py <InputDataFile> <Weights> <Impacts> <ResultFileName>


## Installation

You can install the package using pip:

```bash
pip install Topsis-Dhanishta-102203520
