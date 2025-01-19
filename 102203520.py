import pandas as pd
import numpy as np
import sys

def read_input_file(input_file):
    try:
        data = pd.read_csv(input_file)
        if data.shape[1] < 3:
            raise ValueError("Input file must contain at least 3 columns.")
        return data
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

def validate_input_weights_impacts(weights_str, impacts_str, num_columns):
    weights = list(map(float, weights_str.split(',')))
    impacts = impacts_str.split(',')
    
    if len(weights) != num_columns - 1:
        print(f"Error: Number of weights should be {num_columns - 1}.")
        sys.exit(1)
    
    if len(impacts) != num_columns - 1:
        print(f"Error: Number of impacts should be {num_columns - 1}.")
        sys.exit(1)
    
    if not all(imp in ('+', '-') for imp in impacts):
        print("Error: Impacts should only be '+' or '-'.")
        sys.exit(1)
    
    return weights, impacts

def normalize_matrix(matrix):
    norm_matrix = matrix / np.linalg.norm(matrix, axis=0)
    return norm_matrix

def apply_weights(norm_matrix, weights):
    weighted_matrix = norm_matrix * weights
    return weighted_matrix

def ideal_negative_ideal_solutions(weighted_matrix, impacts):
    ideal_solution = []
    negative_ideal_solution = []
    
    for i in range(weighted_matrix.shape[1]):
        if impacts[i] == '+':
            ideal_solution.append(np.max(weighted_matrix[:, i]))
            negative_ideal_solution.append(np.min(weighted_matrix[:, i]))
        else:
            ideal_solution.append(np.min(weighted_matrix[:, i]))
            negative_ideal_solution.append(np.max(weighted_matrix[:, i]))
    
    return ideal_solution, negative_ideal_solution

def euclidean_distance(matrix, solution):
    return np.sqrt(np.sum((matrix - solution) ** 2, axis=1))

def calculate_topsis_scores(dist_ideal, dist_negative_ideal):
    return dist_negative_ideal / (dist_ideal + dist_negative_ideal)

def main():
    if len(sys.argv) != 5:
        print("Usage: python <program.py> <InputDataFile> <Weights> <Impacts> <ResultFileName>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    weights_str = sys.argv[2]
    impacts_str = sys.argv[3]
    result_file = sys.argv[4]
    
    # Step 1: Read input file and validate
    data = read_input_file(input_file)
    num_columns = data.shape[1]
    
    # Step 2: Validate weights and impacts
    weights, impacts = validate_input_weights_impacts(weights_str, impacts_str, num_columns)
    
    # Step 3: Extract numeric data and normalize
    matrix = data.iloc[:, 1:].values
    norm_matrix = normalize_matrix(matrix)
    
    # Step 4: Apply weights to the normalized matrix
    weighted_matrix = apply_weights(norm_matrix, weights)
    
    # Step 5: Determine the ideal and negative-ideal solutions
    ideal_solution, negative_ideal_solution = ideal_negative_ideal_solutions(weighted_matrix, impacts)
    
    # Step 6: Calculate Euclidean distances
    dist_ideal = euclidean_distance(weighted_matrix, ideal_solution)
    dist_negative_ideal = euclidean_distance(weighted_matrix, negative_ideal_solution)
    
    # Step 7: Calculate TOPSIS scores
    topsis_scores = calculate_topsis_scores(dist_ideal, dist_negative_ideal)
    
    # Step 8: Rank the alternatives
    ranks = topsis_scores.argsort()[::-1] + 1  # Rank in descending order
    
    # Step 9: Prepare output data
    data['Topsis Score'] = topsis_scores
    data['Rank'] = ranks
    
    # Step 10: Save result to CSV
    data.to_csv(result_file, index=False)
    print(f"Results saved to '{result_file}'.")

if __name__ == "__main__":
    main()
