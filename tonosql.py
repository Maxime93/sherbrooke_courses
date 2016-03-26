from pymongo import MongoClient
import pprint
import sqlite3

# Use MongoClient to create a connection:
client = MongoClient()
db = client.sherbrooke

# Get the information from the sqlite database
conn = sqlite3.connect('sherbrooke.sqlite')
cur = conn.cursor()

cur.execute('SELECT * FROM Courses')
row = cur.fetchall()

for i in row :
    print i[2]
    # Insert in nosql database
    result = db.sherbrooke.insert_one({
        "Title" : i[0],
        "Code" : i[1],
        "Credits" : i[2],
        "Cibles" : i[3],
        "Contenu" : i[4],
        "Lien" : i[5]
    })
# ---------------------------------------
