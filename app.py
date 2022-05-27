from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Primeiro app no Lab de DEVOPS"

if __name__ == '__main__':
    app.run()