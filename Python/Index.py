from flask import Flask, render_template

app = Flask(__name__)


@app.route('/Inicio')
def Inico():
    return render_template ('Inicio.html')
    
@app.route('/Seguidor Solar') 
def Seguidorsolar():
    return render_template ('Solar.html')

@app.route('/Proyecto')
def Proyecto():
    return render_template ('Proyecto.html')

if __name__ == '__main__':
    app.run()