from flask import Flask, render_template, url_for, request
import requests
import csv
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.secret_key="manaatslega"

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
      return "Sveiki, mani sauc " + self.vards + "un mans vecums ir " + self.vecums + " gadi."
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

@app.route('/csv')
def csv_skats():
  with open("dati.csv", mode='r', encoding="utf-8") as fails:
    csv_lasitajs = csv.reader(fails)
    dati = list(csv_lasitajs)
    print(dati)
    return render_template("csv.html", dati = dati[0][0])

@app.route('/aptauja')
def aptauja():
    return render_template("aptauja.html")
  
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

    
if __name__ == "__main__":
  app.run(debug=True)
  
