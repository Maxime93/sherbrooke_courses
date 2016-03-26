from bs4 import BeautifulSoup
import urllib
import pprint
import sqlite3

conn = sqlite3.connect('sherbrooke.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS courses''')

cur.execute('''
CREATE TABLE Courses (
    Title TEXT, Code TEXT, Credits TEXT, Cibles TEXT, Contenu TEXT, Lien TEXT, PRIMARY KEY(Code))'''
);

# La fiche cours n'existe pas
# <div id="main">...
#   <div id="stilib_common_columnsContainer">
#       <div id="stilib_common_contentArea">
#           <h1>Attention

# La fiche cours existe
# <div id="main">...
#   <div id="stilib_common_columnsContainer">
#       <div id="stilib_common_contentArea">
#           <div class="stilib_common_contentNarrow">
#               <table><tbody>
#                   <tr></tr>
#                   <tr><td><h2>code</h2><h1>title</h1></td><td>credits</td></tr>
#                   <tr><td><Cibles formation</td></tr>
#                   <tr><td><Contenu</td></tr>

codes = [
"ADM",
"COP",
"CTB",
"DVL",
"ECN",
"GIS",
"GRH",
"INS",
"INT",
"MAR",
"MMP",
"MQG",
"GIN",
"SCA",
"GCH",
"GBI",
"GBT",
"IML",
"MAT",
"MCB",
"TSB",
"GCI",
"GEI",
"GEL",
"GEN",
"GIF",
"GLO",
"IFT",
"IGL",
"AMC",
"GMC",
"IMC",
"ING",
"BMG",
"ESG"
]

for v in codes :
    for indice in range(100) :
        print indice
        fiche = "http://www.usherbrooke.ca/fiches-cours/index.php?id=" + v + str(indice)
        url = fiche
        html = urllib.urlopen(url).read()
        soup = BeautifulSoup(html, "lxml")

        # Fetch title ---------------------------
        title = soup.h1
        real_title = title.string
        if real_title == "Attention" :
            pass
        else :
            print fiche
            print real_title
            # ---------------------------------------

            # Fetch sub titles ----------------------
            sub_title = soup('h2')
            if len(sub_title) > 1 :
                course_code = sub_title[0].string
                print course_code
                credits = sub_title[1].string
                print credits
            else :
                course_code = ""
                credits = ""
            # ---------------------------------------

            # print

            # Fetch content -------------------------
            content = soup.find_all('td')
            if len(content) > 4 :
                # print type(content[3])
                cible_forma = content[3].contents
                cible_formation = cible_forma[1].string
                # print cible_formation

                # print type(content[4])
                contenu = content[4].contents
                vcontenu = contenu[1].string
                # print vcontenu
            else :
                cible_formation = ""
                vcontenu = ""
            # ---------------------------------------

            # Insert to database --------------------
            cur.execute('SELECT Title, Code FROM Courses WHERE Code = ? ', (course_code, ))
            row = cur.fetchone()
            if row is None:
                cur.execute('''INSERT INTO Courses (Code, Title, Credits, Cibles, Contenu, Lien)
                        VALUES ( ?, ?, ?, ?, ?, ? )''', ( course_code, real_title, credits, cible_formation, vcontenu, fiche ) )
            conn.commit()

cur.close()
        # ---------------------------------------
