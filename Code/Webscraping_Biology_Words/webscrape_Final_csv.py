import pandas as pd

# Read the CSV files
df1 = pd.read_csv('Glossary_Biology_words_Wikipedia.csv')
df2 = pd.read_csv('Biology_terms_Collins.csv')
df3 = pd.read_csv('Complete_list_biology_terms_Biology_Dictionary.csv')
df4 = pd.read_csv('Understanding_difficult_biology_words.csv')

# Specify the column name to merge on
column_name = 'Biology_Words'

# Concatenate the data from all four DataFrames into a single DataFrame
merged_df = pd.concat([df1[column_name], df2[column_name], df3[column_name], df4[column_name]], ignore_index=True)

# Save the merged data to a new CSV file
merged_df.to_csv('Biology_words_data.csv', index=False)

print("Merged data saved to merged_data.csv")
