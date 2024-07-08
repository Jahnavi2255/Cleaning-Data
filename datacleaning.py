import pandas as pd
df = pd.read_csv(r"C:\Users\jaanu\Downloads\archive (3)\customer_data.csv.csv")
print(df.head())
print("Column names:", df.columns)
df.columns = df.columns.str.strip()
if 'age' in df.columns:
    df['age'].fillna(df['age'].mean(), inplace=True)
else:
    print("Column 'age' does not exist in the dataset.")
if 'purchase_amount' in df.columns:
    df['purchase_amount'].fillna(df['purchase_amount'].mean(), inplace=True)
else:
    print("Column 'purchase_amount' does not exist in the dataset.")
print("Missing values in each column:\n", df.isnull().sum())

df.drop_duplicates(inplace=True)
print("Cleaned DataFrame:\n", df.head())
df.to_csv(r"C:\Users\jaanu\Downloads\archive (3)\cleaned_customer_data.csv", index=False)
