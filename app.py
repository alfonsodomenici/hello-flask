from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

#db configuration and inizialization
# Required
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "root"
app.config["MYSQL_DB"] = "db24centromedico"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)

@app.route("/")
def index():
    return "index page.."

@app.route("/hello")
def hello():
    return "ciao ciao"

@app.route("/db")
def db():
    cur = mysql.connection.cursor()
    cur.execute("""SELECT nome,cognome,usrmail FROM tbclienti""")
    rv = cur.fetchall()
    return str(rv)