import pandas as pd
import numpy as np

import sqlite3

database = 'database.sqlite'

conn = sqlite3.connect(database)
print('Opened data successfully')

# Step 2: Display all tables in the database
tables = pd.read_sql("""
    SELECT name
    FROM sqlite_master
    WHERE type='table';
""", conn)

print("Tables in the database:")
print(tables)

# Step 3: Display first five rows of Player_Match table
player_match = pd.read_sql("SELECT * FROM Player_Match;", conn)
print("\nFirst 5 rows of Player_Match table:")
print(player_match.head())

# Step 4: Check for null values in Player_Match (Team_Id)
null_player_match = pd.read_sql("""
    SELECT *
    FROM Player_Match
    WHERE Team_Id IS NULL;
""", conn)

print("\nRows in Player_Match where Team_Id is NULL:")
print(null_player_match)

# Step 5: Display first five rows of Match table
match_table = pd.read_sql("SELECT * FROM Match;", conn)
print("\nFirst 5 rows of Match table:")
print(match_table.head())

# Step 6: Check for null values in Match table (Match_Winner)
null_match = pd.read_sql("""
    SELECT *
    FROM Match
    WHERE Match_Winner IS NULL;
""", conn)

print("\nRows in Match table where Match_Winner is NULL:")
print(null_match)

# Step 7: Close connection
conn.close()
print("\nConnection closed.")
