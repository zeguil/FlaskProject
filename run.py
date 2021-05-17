from flask import Flask, render_template, url_for, redirect, request
from flask_sqlalchemy import SQLAlchemy

#beekeeper
#sqlite browser
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Cliente(db.Model):
    __tablename__ = "cliente"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(90), nullable=True)
    telefone = db.Column(db.String(20), unique=True, nullable=False)
    cpf = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(90), nullable=False, unique=True, index=True)
    
    def __init__(self, name, telefone, cpf, email):
        self.name = name
        self.telefone = telefone
        self.cpf = cpf
        self.email = email
    
db.create_all()


@app.route("/index", methods = ['GET', 'POST'])
def index():
    return render_template("index.html")

@app.route("/cadastro", methods = ['GET', 'POST'])
def cadastro():
    print("ola mundo")
    if request.method == "POST":
        name = request.form.get("name")
        telefone = request.form.get("telefone")
        cpf = request.form.get("cpf")
        email = request.form.get("email")

        if name and telefone and cpf and email:
            print(name)
            p = Cliente(name, telefone, cpf, email)
            db.session.add(p)
            db.session.commit()
        return redirect(url_for("index"))
    return render_template("cadastro.html")    

@app.route("/lista")
def lista():
    pessoas = Cliente.query.all()
    return render_template("lista.html", pessoas=pessoas)

if __name__ == "__main__":
    app.run(debug=True)
