import sqlite3
import pandas as pd

# conn = sqlite3.connect('database.db')
# query = "SELECT name FROM sqlite_master WHERE type='table';"
# df_tables = pd.read_sql_query(query, conn)
# conn.close()
# print(df_tables)

conn = sqlite3.connect('database.db')
query = "SELECT * FROM weather_data;"
df_resultado = pd.read_sql_query(query, conn)
print(df_resultado)
conn.close()