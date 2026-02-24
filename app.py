from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__, template_folder='templates')
app.secret_key = 'projeto_tech'

USUARIO = {
"email": "admin@senai.com",
"senha": generate_password_hash("123456")
}

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email') 
        senha = request.form.get('senha') 

        if email == USUARIO['email'] and check_password_hash(USUARIO['senha'], senha):
            session['user'] = email 
            return redirect(url_for('dashboard'))
        else:
            flash('Erro: E-mail ou senha inválidos!', 'danger') 
            
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user' not in session: 
        return redirect(url_for('login'))
    return render_template('dashboard.html', email=session['user'])

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login')) 

if __name__ == '__main__':
    app.run(debug=True, port=5001)