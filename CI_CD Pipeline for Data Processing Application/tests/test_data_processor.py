import pytest
import pandas as pd
from src.data_processor import process_data

def test_process_data():
    # Create a sample input file
    input_df = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    })
    input_file = 'test_input.csv'
    input_df.to_csv(input_file, index=False)
    
    # Process the data
    output_file = 'test_output.csv'
    result_df = process_data(input_file, output_file)
    
    # Check if the output file was created
    assert pd.read_csv(output_file).shape == (3, 2)
    
    # Check if the data was standardized
    assert result_df['A'].mean() == pytest.approx(0, abs=1e-6)
    assert result_df['A'].std() == pytest.approx(1, abs=1e-6)
