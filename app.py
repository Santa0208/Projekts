from flask import Flask, render_template, url_for, request, session, redirect
import requests
import csv
import os
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.secret_key="manaatslega"

def init_db():
  conn = sqlite3.connect('database.db')
  cursor = conn.cursor()
  cursor.execute('''
    CREATE TABLE IF NOT EXISTS lietotaji(
      "id" INTEGER UNIQUE,
      "vards" TEXT NOT NULL,
      "dzimums" TEXT NOT NULL,
      "hobiji" TEXT NOT NULL,
      PRIMARY KEY("id" AUTOINCREMENT)
    )
  ''')
  cursor.execute('''
    CREATE TABLE IF NOT EXISTS administratori(
      "id" INTEGER,
      "lietotajvards" TEXT NOT NULL,
      "parole" TEXT NOT NULL,
      PRIMARY KEY("id" AUTOINCREMENT)
    )
  ''')
  cursor.execute('SELECT * FROM administratori WHERE lietotajvards = ?', ('admin',))
  if not cursor.fetchone():
    cursor.execute('INSERT INTO administratori (lietotajvards, parole) VALUES (?,?)', ('admin', generate_password_hash('admin')))
  conn.commit()
  conn.close()
  
init_db() 

@app.route('/')
def home():
  return render_template("index.html")

@app.route('/par_mums')
def par_mums():
  return render_template("par_mums.html")

@app.route('/kontakti')
def kontakti():
  return render_template("kontakti.html")

@app.route('/pamati_sintakse')
def pamati_sintakse():
  return render_template("pamati_sintakse.html")

@app.route('/sveiciens')
def sveiciens():
  return render_template("sveiciens.html")

@app.route('/mainigie')
def mainigie():
  vards = "Igors"
  vecums = 35
  skaitlis1 = 4
  skaitlis2 = 7
  summa = skaitlis1 + skaitlis2
  print(summa)
  return render_template("mainigie.html", vards=vards, vecums=vecums, summa=summa)

@app.route('/datu_tipi')
def datu_tipi():
  teksts = "Sveicieni, šis ir teksts"
  skaitlis = 100
  decimals = 10.5
  saraksts = ["vards", 2, 3, 4, 5]
  mans_dict = {"vards": "Anna", "vecums":20}
  mans_kopa = {1,2,3,4,5}
  return render_template("datu_tipi.html", teksts=teksts, skaitlis=skaitlis, decimals=decimals, saraksts=saraksts, mans_dict=mans_dict, mans_kopa=mans_kopa)

@app.route('/operatori')
def operatori():
  a = 13
  b = 6
  summa = a + b
  starpiba = a - b
  reizinajums = a * b
  dalijums = a / b
  atlikums = a % b
  vienads = a == b
  print(vienads)
  print(summa)
  return render_template("operatori.html", summa=summa, starpiba = starpiba, 
                         reizinajums = reizinajums, dalijums = dalijums, 
                         atlikums = atlikums, vienads = vienads)
  
@app.route('/kontroles_strukturas')
def kontroles_strukturas():
  x = 4
  if x >= 40 and x <= 50:
    rezultats = "Ir tādi darbnieki"
    print(rezultats)
  else: 
    rezultats = "nesakrīt"
    print(rezultats)
    
    for_cikls_rezultats = [i for i in range(1,11)]
    
    while_cikls_rezultats = []
    y = 0
    while y <= 5:
      while_cikls_rezultats.append(y)
      y+=1
      return render_template("kontroles_strukturas.html", rezultats = rezultats, for_cikls_rezultats = for_cikls_rezultats, 
                          while_cikls_rezultats = while_cikls_rezultats)
    
@app.route('/funkcijas')
def funkcijas():
  def sveiciens(vards="Pēteris", uzvards="Bērzs"):
    return "Sveiks " + vards + " " + uzvards + "!"
  noklusejuma_sveiciens = sveiciens()
  izmainitais_sveiciens = sveiciens("Jānis", "Kārkliņš")
  return render_template("funkcijas.html", noklusejuma_sveiciens = noklusejuma_sveiciens, 
                         izmainitais_sveiciens = izmainitais_sveiciens)

@app.route('/ievade_izvade', methods=['GET', 'POST'])
def ievade_izvade():
  if request.method == "POST":
    vards = request.form['vards']
    return render_template("ievade_izvade.html", vards = vards)
  return render_template("ievade_izvade.html", vards = None)

@app.route('/failu_apstrade')
def failu_apstrade():
  saturs = ""
  try:
    with open('piemers.txt', 'r') as fails:
      saturs = fails.read()
  except IOError:
      saturs = "Fails nav atrasts!"
  return render_template("failu_apstrade.html", saturs = saturs)

@app.route('/oop')
def oop():
  class Persona:
    def __init__ (self, vards, vecums):
      self.vards = vards
      self.vecums = vecums
    def sveiciens(self):
      return "Sveiki, mani sauc " + self.vards + " un mans vecums ir " + self.vecums + " gadi."
  persona = Persona("Janis", "30")
  sveiciens = persona.sveiciens()
  
  return render_template("oop.html", sveiciens = sveiciens)

@app.route('/moduli')
def moduli():
  import math
  sqrt_rezultats = math.sqrt(16)
  pow_rezultats = math.pow(16,2)
  print(sqrt_rezultats)
  print(pow_rezultats)
  summa = sqrt_rezultats + pow_rezultats
  
  return render_template("moduli.html", summa = summa)

@app.route('/joks')
def joks():
  url = "https://api.chucknorris.io/jokes/random"
  atbilde = requests.get(url)
  print(atbilde)
  dati = atbilde.json()
  print(type(dati))
  print(dati)
  print(dati['value'])
  return render_template("joks.html", joks = dati['value'], adrese = dati['url'], avatars = dati['icon_url'])

@app.route('/darbs', methods=['GET', 'POST'])
def darbs():
    rezultats = None
    sk1 = sk2 = None

    if request.method == 'POST':
        try:
            sk1 = int(request.form.get('sk1'))
            sk2 = int(request.form.get('sk2'))
            rezultats = sk1 + sk2
        except (ValueError, TypeError):
            rezultats = "Nederīga ievade – lūdzu ievadi tikai skaitļus."

    return render_template('darbs.html', rezultats=rezultats, sk1=sk1, sk2=sk2)

@app.route('/aptauja')
def aptauja():
    return render_template('aptauja.html')
  
@app.route('/iesniegt', methods=['GET', 'POST'])
def iesniegt():
    if request.method == 'POST':
        vards = request.form['vards']
        dzimums = request.form['dzimums']
        hobiji = request.form.getlist('hobiji')
        hobiji_str = ', '.join(hobiji)

        print(vards)
        print(dzimums)
        print(hobiji)
        print(hobiji_str)
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO lietotaji (vards, dzimums, hobiji)
            VALUES (?, ?, ?)
        ''', (vards, dzimums, hobiji_str))
        conn.commit()
        conn.close()

        return render_template("paldies.html")
      
@app.route('/pieteikties', methods=['GET', 'POST'])
def pieteikties():
  if request.method == 'POST':
    lietotajvards = request.form['lietotajvards']
    parole = request.form['parole']
    print(lietotajvards)
    print(parole)
    
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM administratori WHERE lietotajvards = ?', (lietotajvards,))
    admin = cursor.fetchone()
    print(admin[0])
    conn.close()
    
    if admin and check_password_hash(admin[2], parole):
      session['lietotajvards'] = lietotajvards
      return redirect('panelis')
    
  return render_template('pieteikties.html')

@app.route('/panelis')
def panelis():
  if 'lietotajvards' not in session:
    return redirect(url_for('pieteikties'))
  conn = sqlite3.connect('database.db')
  cursor = conn.cursor()
  cursor.execute('SELECT * FROM lietotaji')
  lietotaji = cursor.fetchall()
  print(lietotaji)
  print(type(lietotaji))
  return render_template('panelis.html', lietotaji = lietotaji)

@app.route('/dzest/<int:id>')
def dzest_lietotaju(id):
  if 'lietotajvards' not in session:
    return redirect(url_for('pieteikties'))
  conn = sqlite3.connect('database.db')
  cursor = conn.cursor()
  cursor.execute('DELETE FROM lietotaji WHERE id = ?', (id,))
  conn.commit()
  conn.close()
  
  return redirect(url_for('panelis'))

@app.route('/dzest2/<string:vards>')
def dzest_rindu_csv(vards):
  jauni_dati = []
  print("datu tips jauni_dati")
  print(type(jauni_dati))
  with open('dati.csv', newline="", encoding="utf-8") as csvfails:
    lasitajs = csv.reader(csvfails)
    print("Rezultāti no CSV datu struktūrā")
    print(lasitajs)
    for rinda in lasitajs:
      if rinda[0] !=vards:
        jauni_dati.append(rinda)
      print('jaunie dati:')
      print(jauni_dati)
      with open('dati.csv', 'w', newline="", encoding="utf-8") as csvfails:
        rakstitajs = csv.writer(csvfails)
        rakstitajs.writerows(jauni_dati)
  
  return redirect(url_for('csv_skats'))

@app.route('/izlogoties')
def izlogoties():
  session.pop('lietotajvards', None)
  return redirect(url_for('pieteikties'))

@app.route('/csv')
def csv_skats():
  try:
    
    with open("dati.csv", mode='r', encoding="utf-8") as fails:
      csv_lasitajs = csv.reader(fails)
      dati = list(csv_lasitajs)
      print(dati)
      return render_template("csv.html", dati = dati)
  except FileNotFoundError:
    with open('dati.csv', mode='w', encoding="utf-8", newline="") as fails:
      fails.write('vārds,uzvārds,vecums\n')
      print("Fails tika izveidots")
    return render_template('kluda.html', zinojums = "Fails dati.csv nav atrasts")
  
@app.errorhandler(404)
def internal_server_error(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404
  
def ierakstit_csv(faila_nosaukums, dati):
  fails = 'dati.csv'
  fails_eksiste = os.path.isfile(fails)
  if not fails_eksiste:
    csv_rakstitajs.writerow(['vārds'], ['uzvārds'], ['vecums'])
  with open(faila_nosaukums, mode='a', encoding="utf-8") as fails:
    csv_rakstitajs = csv.writer(fails)
    csv_rakstitajs.writerow(dati)
  
@app.route('/pievienot', methods=['POST'])
def pievienot():
  vards = request.form['vards']
  uzvards = request.form['uzvards']
  vecums = request.form['vecums']
  print(vards)
  ierakstit_csv('dati.csv', [vards, uzvards, vecums])
  return redirect(url_for('csv_skats'))

if __name__ == "__main__":
  app.run(debug=True)
  