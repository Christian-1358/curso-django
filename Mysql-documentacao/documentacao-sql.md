Guia de Comandos MySQL

Este documento contém os principais comandos do MySQL, divididos por categorias (DDL, DML, DQL, DCL, DTL e Funções Utilitárias), com exemplos práticos de uso.

1. DDL (Data Definition Language)

Comandos usados para definir e alterar a estrutura do banco de dados e de suas tabelas.

Criar e Gerenciar Banco de Dados

-- Criar um novo banco de dados
CREATE DATABASE cadastro;

-- Criar banco de dados apenas se não existir
CREATE DATABASE IF NOT EXISTS cadastro
DEFAULT CHARACTER SET utf8mb4
DEFAULT COLLATE utf8mb4_general_ci;

-- Selecionar o banco de dados para uso
USE cadastro;

-- Excluir um banco de dados
DROP DATABASE IF EXISTS cadastro;


Criar Tabelas

CREATE TABLE IF NOT EXISTS pessoas (
    id INT NOT NULL AUTO_INCREMENT,
    nome VARCHAR(30) NOT NULL,
    nascimento DATE,
    sexo ENUM('M', 'F'),
    peso DECIMAL(5,2),
    altura DECIMAL(3,2),
    nacionalidade VARCHAR(20) DEFAULT 'Brasil',
    PRIMARY KEY (id)
) DEFAULT CHARSET = utf8mb4;


Alterar Tabelas (ALTER TABLE)

-- Adicionar nova coluna
ALTER TABLE pessoas ADD COLUMN profissao VARCHAR(20) AFTER nome;

-- Adicionar coluna na primeira posição
ALTER TABLE pessoas ADD COLUMN codigo INT FIRST;

-- Modificar tipo ou restrições de uma coluna
ALTER TABLE pessoas MODIFY COLUMN profissao VARCHAR(30) NOT NULL DEFAULT '';

-- Renomear uma coluna
ALTER TABLE pessoas CHANGE COLUMN profissao cargo VARCHAR(30);

-- Apagar uma coluna
ALTER TABLE pessoas DROP COLUMN cargo;

-- Apagar uma restrição UNIQUE / ÍNDICE
ALTER TABLE pessoas DROP INDEX nome_do_indice;

-- Renomear a tabela inteira
ALTER TABLE pessoas RENAME TO gafanhotos;


Limpar e Excluir Tabelas

-- Apagar todos os dados da tabela e resetar o AUTO_INCREMENT
TRUNCATE TABLE pessoas;

-- Apagar a tabela completamente da base de dados
DROP TABLE IF EXISTS pessoas;


2. DML (Data Manipulation Language)

Comandos usados para manipular os dados armazenados dentro das tabelas.

Inserir Dados (INSERT INTO)

-- Inserir um único registro
INSERT INTO pessoas (nome, nascimento, sexo, peso, altura, nacionalidade)
VALUES ('Godofredo', '1984-01-02', 'M', 78.5, 1.83, 'Brasil');

-- Inserir múltiplos registros de uma só vez
INSERT INTO pessoas VALUES
(DEFAULT, 'Ana', '2000-05-10', 'F', 55.2, 1.62, DEFAULT),
(DEFAULT, 'Pedro', '1995-12-22', 'M', 80.0, 1.75, 'Portugal');


Atualizar Dados (UPDATE)

-- Atualizar um registro específico
UPDATE pessoas 
SET nome = 'Ana Maria', peso = 56.0 
WHERE id = 2;

-- Atualizar com limite de segurança
UPDATE pessoas 
SET nacionalidade = 'Brasil' 
WHERE nacionalidade IS NULL 
LIMIT 1;


Deletar Dados (DELETE)

-- Deletar registro específico
DELETE FROM pessoas 
WHERE id = 2;

-- Deletar registros com limite
DELETE FROM pessoas 
WHERE nacionalidade = 'Portugal' 
LIMIT 1;


3. DQL (Data Query Language)

Comandos para consulta e filtragem de dados.

Seleção Básica

-- Selecionar todas as colunas de todos os registros
SELECT * FROM pessoas;

-- Selecionar colunas específicas e ordenar
SELECT nome, nascimento FROM pessoas ORDER BY nome ASC; -- ou DESC


Filtragem com WHERE

-- Operadores relacionais (=, !=, <, >, <=, >=)
SELECT * FROM pessoas WHERE peso >= 70.0;

-- Entre valores (BETWEEN)
SELECT nome, ano FROM cursos WHERE ano BETWEEN 2014 AND 2018;

-- Em uma lista específica (IN)
SELECT nome, ano FROM cursos WHERE ano IN (2014, 2016, 2020);

-- Operadores lógicos (AND, OR, NOT)
SELECT * FROM pessoas WHERE sexo = 'F' AND peso < 60.0;


Busca por Padrões (LIKE)

-- Começa com 'A'
SELECT * FROM pessoas WHERE nome LIKE 'A%';

-- Termina com 'A'
SELECT * FROM pessoas WHERE nome LIKE '%a';

-- Contém 'A' em qualquer posição
SELECT * FROM pessoas WHERE nome LIKE '%a%';

-- Não contém 'A'
SELECT * FROM pessoas WHERE nome NOT LIKE '%a%';

-- Padrão com caractere curinga de tamanho fixo (_)
SELECT * FROM pessoas WHERE nome LIKE 'PH_TOSHOP%';


Agrupamento e Funções de Agregação

-- Contar registros
SELECT COUNT(*) FROM pessoas;

-- Maior e Menor valor
SELECT MAX(peso), MIN(peso) FROM pessoas;

-- Soma e Média
SELECT SUM(carga), AVG(carga) FROM cursos;

-- Agrupar dados (GROUP BY)
SELECT nacionalidade, COUNT(*) FROM pessoas GROUP BY nacionalidade;

-- Filtrar grupos (HAVING)
SELECT ano, COUNT(*) FROM cursos 
GROUP BY ano 
HAVING COUNT(*) >= 2 
ORDER BY COUNT(*) DESC;


4. Joins (Relacionamentos entre Tabelas)

Comandos para consultar dados distribuídos em múltiplas tabelas conectadas por chaves estrangeiras (Foreign Keys).

-- INNER JOIN: Retorna apenas quando há correspondência em ambas as tabelas
SELECT gafanhotos.nome, cursos.nome, cursos.ano 
FROM gafanhotos 
INNER JOIN cursos 
ON cursos.idcurso = gafanhotos.cursopreferido;

-- LEFT OUTER JOIN: Retorna todos da tabela da esquerda, com ou sem correspondência
SELECT gafanhotos.nome, cursos.nome 
FROM gafanhotos 
LEFT JOIN cursos 
ON cursos.idcurso = gafanhotos.cursopreferido;

-- RIGHT OUTER JOIN: Retorna todos da tabela da direita, com ou sem correspondência
SELECT gafanhotos.nome, cursos.nome 
FROM gafanhotos 
RIGHT JOIN cursos 
ON cursos.idcurso = gafanhotos.cursopreferido;


5. Comandos Utilitários e de Inspeção

Comandos úteis para visualizar metadados e estado do banco de dados.

-- Listar todos os bancos de dados
SHOW DATABASES;

-- Listar todas as tabelas do banco selecionado
SHOW TABLES;

-- Descrever a estrutura de uma tabela (colunas, tipos, chaves)
DESCRIBE pessoas;
-- ou abreviado:
DESC pessoas;

-- Exibir o comando SQL usado para criar a tabela
SHOW CREATE TABLE pessoas;

-- Exibir o comando SQL usado para criar a base de dados
SHOW CREATE DATABASE cadastro;
