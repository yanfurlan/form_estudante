import os
import sqlite3
from config import DB_PATH

# Criar a pasta se não existir
os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

def criar_banco():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS alunos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            curso TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()
    print(f"Banco de dados criado em: {DB_PATH}")

if __name__ == "__main__":
    criar_banco()
