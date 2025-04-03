# 📌 Projeto: Sistema de Cadastro de Estudantes

## 📖 Sobre o Projeto
Este projeto é um sistema simples de cadastro de estudantes utilizando **Flask** e **SQLite**. Ele permite adicionar, visualizar e deletar estudantes armazenados no banco de dados.

Além disso, foi implementada uma **view para visualização** dos dados e uma **Stored Procedure (simulada via trigger)** para registrar automaticamente log de novos cadastros.

---

## 🚀 Tecnologias Utilizadas
- **Python** (Flask para criação da API e renderização de páginas HTML)
- **HTML/CSS** (Interface para cadastro e visualização)
- **SQLite** (Banco de dados para armazenamento das informações)
- **SQL** (Criação de tabelas, triggers e views)


## 🏗️ Configuração do Banco de Dados
Antes de rodar a aplicação, é necessário garantir que o banco de dados **SQLite** está criado corretamente.

**📌 Criando a Tabela de Estudantes:**
```sql
CREATE TABLE IF NOT EXISTS estudantes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    curso TEXT NOT NULL,
    periodo TEXT NOT NULL,
    disciplinas TEXT NOT NULL,
    email TEXT NOT NULL
);
```

**📌 Criando uma View para Visualização dos Dados:**
```sql
CREATE VIEW vw_estudantes AS
SELECT id, nome, curso, periodo, disciplinas, email
FROM estudantes;
```
Essa view pode ser utilizada para simplificar consultas:
```sql
SELECT * FROM vw_estudantes;
```

**📌 Criando um Trigger para Simular uma Procedure no SQLite:**
Como o SQLite **não possui Stored Procedures**, utilizamos um **Trigger** para registrar logs automaticamente:

```sql
CREATE TABLE log_estudantes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    mensagem TEXT NOT NULL,
    data TEXT NOT NULL
);
```

```sql
CREATE TRIGGER trg_after_insert_estudantes
AFTER INSERT ON estudantes
BEGIN
    INSERT INTO log_estudantes (mensagem, data)
    VALUES ('Novo estudante cadastrado: ' || NEW.nome, datetime('now'));
END;
```
Agora, sempre que um estudante for cadastrado, uma mensagem será armazenada automaticamente em `log_estudantes`.

---

## 🖥️ Configuração e Execução
### 📌 Passo 1: Instalar as Dependências
```sh
pip install flask
```

### 📌 Passo 2: Executar a Aplicação
```sh
python app.py
```
A aplicação estará disponível em **http://127.0.0.1:5000**

---

## 🌍 Rotas da Aplicação
### 📌 Página Inicial (`/`)
Lista todos os estudantes cadastrados no banco.

### 📌 Adicionar Estudante (`/adicionar`)
Formulário para cadastrar novos estudantes.

### 📌 Deletar Estudante (`/deletar/<id>`)
Remove um estudante do banco de dados.


## 📌 Autor
Desenvolvido por **Yan Furlan** 🚀