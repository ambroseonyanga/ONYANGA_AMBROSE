import pandas as pd
from dateutil import parser

df = pd.read_csv("Mine.csv")
df.columns = df.columns.str.strip() 

print("Columns:", df.columns.tolist())


def clean_date(date_str):
    try:
        if pd.isna(date_str):
            return pd.NaT
        date_str = str(date_str).strip("'") 
        return parser.parse(date_str, dayfirst=False, yearfirst=True)
    except Exception:
        return pd.NaT

df['Date'] = df['Date'].apply(clean_date)

print("\nMissing values per column:")
print(df.isnull().sum())


print("\nCleaned Data Sample:")
print(df.head(100))
