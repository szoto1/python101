from flask import Flask
from flask import render_template
from flask import request, redirect, url_for
from Homeworks.day12.model import Wpis
from Homeworks.day12.model import Ksiega

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html') #otworzy plik index.html z domyslnego katalogu /templates
    #uwaga na cache'owanie (chrome CTRL+SHIFT+R disable cache)

    #html = "<h1>heading1</h1>\n<h2>heading2</h2>\n<h3>heading3</h3>"
    #return html

@app.route("/dodaj_wpis", methods=['GET','POST'])
def dodaj_wpis():

    if request.method == 'POST':
        ksiega = Ksiega()
        wpis = Wpis(request.form['autor'], request.form['tresc'], request.form['tytul'])
        ksiega.dodajWpis(wpis)
        return redirect(url_for('lista_wpisow'))

    return render_template('dodaj_wpis.html')

@app.route("/lista_wpisow")
def lista_wpisow():
    ksiega = Ksiega()
    wpisy = ksiega.wpisy
    # wpisy = ksiega.wpisy[::-1] #reverse order
    # wpisy.reverse() #reverse order
    return render_template('lista_wpisow.html', wpisy_html=wpisy)

@app.route("/hello")
@app.route("/hello2")
def hello():
    return "Hello"

@app.route("/witaj/<imie>")
def hello2(imie):
    return 'Witaj {}!'.format(imie)

@app.route("/witaj/<int:numer>")
def hello3(numer):
    return 'Twój nr to {}!'.format(numer)


app.run(debug=True)
