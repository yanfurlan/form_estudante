import os

# Caminho absoluto para o banco de dados dentro da pasta "universidade"
DB_PATH = r"\\\\\\universidade.db"

# URL do banco para conexão (caso futuramente queira usar SQLAlchemy)
DATABASE_URL = f"sqlite:///{DB_PATH}"
