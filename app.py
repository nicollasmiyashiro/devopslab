from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

csrf = CSRFProtect(app)

@app.route("/")
def pagina_inicial():
    return "Primeiro app no Lab de DEVOPS"

if __name__ == '__main__':
    port = os.getenv('PORT')
    app.run()