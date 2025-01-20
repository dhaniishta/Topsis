import unittest
import pandas as pd
import os
from Topsis_Dhanishta_102203520.topsis import main

class TestTopsis(unittest.TestCase):
    def setUp(self):
        """Set up a temporary CSV file for testing."""
        self.input_file = 'test_input.csv'
        self.output_file = 'test_output.csv'

        # Create a sample input CSV file
        data = {
            'Name': ['A', 'B', 'C', 'D'],
            'Criterion1': [250, 200, 300, 275],
            'Criterion2': [16, 16, 32, 24],
            'Criterion3': [12, 8, 16, 14]
        }
        df = pd.DataFrame(data)
        df.to_csv(self.input_file, index=False)

    def tearDown(self):
        """Clean up temporary files after testing."""
        if os.path.exists(self.input_file):
            os.remove(self.input_file)
        if os.path.exists(self.output_file):
            os.remove(self.output_file)

    def test_topsis_functionality(self):
        """Test the TOPSIS implementation with valid inputs."""
        # Prepare command-line arguments
        import sys
        sys.argv = [
            'topsis.py',                # Mock script name
            self.input_file,            # Input file
            '1,1,1',                    # Weights
            '+,+,-',                    # Impacts
            self.output_file            # Output file
        ]

        # Run the main function
        main()

        # Check if the output file is created
        self.assertTrue(os.path.exists(self.output_file), "Output file was not created.")

        # Validate the output file content
        result = pd.read_csv(self.output_file)

        # Check if required columns are present
        self.assertIn('Topsis Score', result.columns, "Topsis Score column missing in the output.")
        self.assertIn('Rank', result.columns, "Rank column missing in the output.")

        # Check if the number of rows is correct
        self.assertEqual(len(result), 4, "Output file row count mismatch.")

        # Check if the ranks are correctly calculated
        ranks = result['Rank'].tolist()
        self.assertEqual(sorted(ranks), [1, 2, 3, 4], "Ranks are not correctly assigned.")

if __name__ == '__main__':
    unittest.main()


