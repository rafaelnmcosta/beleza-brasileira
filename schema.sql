DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS services;

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    endereco TEXT NOT NULL,
    telefone TEXT NOT NULL,
    ref TEXT NOT NULL,
    senha TEXT NOT NULL,
    tipo TEXT NOT NULL,
    cpf_cnpj TEXT NOT NULL,
    descricao TEXT
);

CREATE TABLE services (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data DATE NOT NULL,
    horario TIME NOT NULL,
    duracao INTEGER NOT NULL,
    descricao TEXT NOT NULL,
    ref_cliente TEXT NOT NULL,
    ref_estab TEXT NOT NULL
);