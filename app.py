from flask import Flask, render_template

app = Flask(__name__)

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



if __name__ == "__main__":
  app.run(debug=True)
  
