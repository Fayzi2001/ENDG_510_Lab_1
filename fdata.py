import random
import pandas as pd # in case of error, install pnadas using: pip install pandas 
# Read the CSV file into a DataFrame 
df = pd.read_csv('data.csv') 

i=500
while i>=0:
    new_data = { 
        'Temp': random.randrange(0,366,5), 
        'Humd': random.randrange(0,901,5), 
        'Label': 0 
    } 
    i=i-1
    df = df._append(new_data, ignore_index=True) 

# Step 3: Save the DataFrame to a new CSV file 
df.to_csv("data.csv", index=False)