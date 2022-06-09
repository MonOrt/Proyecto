from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def principal():
    return "Seguidor Solar"
    

@app.route('/contacto')
def contacto():
    return "Esta es la página de contacto"


@app.route('/Solar')
def sesolar():
    seguidor = ("Seguidor Solar")
    return render_template('solar.html', solar = seguidor)


@app.route('/Arduino')
def contacto():
    return render_template('Arduino.html')


if __name__ == '__main__':
    app.run(debug=True, port=5017)