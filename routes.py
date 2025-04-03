from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

# Definição do caminho absoluto do banco de dados
DB_PATH = r"\\\\\universidade.db"

app = Flask(__name__)

# Conectar ao banco de dados com tratamento de erro
def conectar_banco():
    try:
        db_path = os.path.abspath(DB_PATH)  # Garante o caminho absoluto
        conn = sqlite3.connect(db_path)
        return conn
    except sqlite3.Error as e:
        print(f"Erro ao conectar ao banco: {e}")
        return None

# Criar a tabela se não existir
def inicializar_banco():
    conn = conectar_banco()
    if conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS estudantes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                curso TEXT NOT NULL,
                periodo TEXT NOT NULL,
                disciplinas TEXT NOT NULL,
                email TEXT NOT NULL
            )
        """)
        conn.commit()
        conn.close()

@app.route('/')
def index():
    conn = conectar_banco()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='estudantes'")
        if cursor.fetchone():  # Verifica se a tabela existe
            cursor.execute("SELECT * FROM estudantes")
            estudantes = cursor.fetchall()
        else:
            estudantes = []
        conn.close()
        return render_template('index.html', estudantes=estudantes)
    return "Erro ao conectar ao banco de dados.", 500

@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar():
    if request.method == 'POST':
        nome = request.form['nome']
        curso = request.form['curso']
        periodo = request.form['periodo']
        disciplinas = request.form['disciplinas']
        email = request.form['email']
        
        conn = conectar_banco()
        if conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO estudantes (nome, curso, periodo, disciplinas, email) 
                VALUES (?, ?, ?, ?, ?)
            """, (nome, curso, periodo, disciplinas, email))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
        return "Erro ao conectar ao banco de dados.", 500
    return render_template('form.html')

@app.route('/deletar/<int:id>')
def deletar(id):
    conn = conectar_banco()
    if conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM estudantes WHERE id = ?", (id,))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return "Erro ao conectar ao banco de dados.", 500

if __name__ == '__main__':
    inicializar_banco()  # Garante que a tabela será criada antes de rodar o app
    app.run(debug=True)
