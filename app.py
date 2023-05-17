from flask import Flask, app, flash, redirect, render_template, request, redirect
import ibm_db
import ibm_db_dbi as dbi
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(32)
# Database credentials
database = "bludb"
hostname = "3883e7e4-18f5-4afe-be8c-fa31c41761d2.bs2io90l08kqb1od8lcg.databases.appdomain.cloud"
port = "31498"
username = "qwh90818"
password = "d8O436rEebMYO5NH"
ssl_cert = "DigiCertGlobalRootCA.crt"

# Establish a connection to the IBM Db2 database
conn_str = f"DATABASE={database};HOSTNAME={hostname};PORT={port};PROTOCOL=TCPIP;UID={username};PWD={password};SECURITY=SSL;SSLServerCertificate={ssl_cert};"
conn = ibm_db.connect(conn_str, '', '')
# Route for frontend
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('About.html')

@app.route('/testimonals')
def testimonials():
    return render_template('Testimonials.html')

@app.route('/imageai')
def imageai():
    return render_template('ImageAI.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/loginpage')
def loginpage():
    return render_template('LoginPage.html')

@app.route('/loginuser', methods=['POST'])
def loginuser():
    x = [x for x in request.form.values()]
    EMAIL = x[0]
    PASSWORD = x[1]
    sql = "SELECT * FROM REGISTER WHERE EMAIL = ? AND PASSWORD = ?"
    stmt = ibm_db.prepare(conn, sql)
    ibm_db.bind_param(stmt, 1, EMAIL)
    ibm_db.bind_param(stmt, 2, PASSWORD)
    ibm_db.execute(stmt)
    account = ibm_db.fetch_assoc(stmt)
    if account:
        return render_template('dashboard.html', user=account)
    else:
        error_message = "Invalid email or password"
        return render_template('LoginPage.html', error=error_message)

# Profile page
@app.route('/profile')
def profile():
    return render_template('dashboard.html')

# Background Remover page
@app.route('/background-remover')
def background_remover():
    return render_template('dashboard.html')

# Cartoon Face page
@app.route('/cartoon-face')
def cartoon_face():
    return render_template('dashboard.html')

# Remove Vehicle Background page
@app.route('/remove-vehicle-background')
def remove_vehicle_background():
    return render_template('dashboard.html')


@app.route('/registerpage')
def registerpage():
    return render_template("RegisterPage.html")

@app.route('/register1', methods=['POST'])
def register1():
    x = [x for x in request.form.values()]
    NAME = x[0]
    EMAIL = x[1]
    PASSWORD = x[2]
    sql = "SELECT * FROM REGISTER WHERE EMAIL = ?"
    stmt = ibm_db.prepare(conn, sql)
    ibm_db.bind_param(stmt, 1, EMAIL)
    ibm_db.execute(stmt)
    account = ibm_db.fetch_assoc(stmt)
    if account:
        return render_template('LoginPage.html', pred="You are already a member, please Login using your details")
    else:
        insert_sql = "INSERT INTO REGISTER (NAME, EMAIL, PASSWORD) VALUES (?, ?, ?)"
        prep_stmt = ibm_db.prepare(conn, insert_sql)
        ibm_db.bind_param(prep_stmt, 1, NAME)
        ibm_db.bind_param(prep_stmt, 2, EMAIL)
        ibm_db.bind_param(prep_stmt, 3, PASSWORD)
        ibm_db.execute(prep_stmt)
        return render_template('LoginPage.html', pred="Registration Successful, please Login using your details")



if __name__ == '__main__':
    app.run()