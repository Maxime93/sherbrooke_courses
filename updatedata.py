import pprint
import sqlite3

conn = sqlite3.connect('sherbrooke_updated.sqlite')
cur = conn.cursor()

conn2 = sqlite3.connect('sherbrooke.sqlite')
cur2 = conn2.cursor()

cur.execute('''
DROP TABLE IF EXISTS Courses''')

cur.execute('''
CREATE TABLE Courses (
    Title TEXT, CodeLettre TEXT, Code TEXT, Credits TEXT, Cibles TEXT, Contenu TEXT, Lien TEXT, PRIMARY KEY(Code))'''
);

cur2.execute('SELECT * FROM Courses')
row = cur.fetchall()
for i in row :
    print i
