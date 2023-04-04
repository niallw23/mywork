# Lab work Week 11
import pandas as pd

with pd.ExcelWriter(Week 11grades.xlsx, engine='openpyxl', mode='a') as writer:
    df.describe().to_excel(writer, sheet_name="summary")

