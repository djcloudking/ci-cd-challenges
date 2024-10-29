import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

def process_data(input_file, output_file):
    # Read data
    df = pd.read_csv(input_file)
    
    # Perform data processing
    # Example: Standardize numeric columns
    numeric_columns = df.select_dtypes(include=[np.number]).columns
    scaler = StandardScaler()
    df[numeric_columns] = scaler.fit_transform(df[numeric_columns])
    
    # Save processed data
    df.to_csv(output_file, index=False)
    
    return df
