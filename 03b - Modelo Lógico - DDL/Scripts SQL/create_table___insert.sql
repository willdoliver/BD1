CREATE TABLE pessoa (
	login INTEGER NOT NULL,
	nome VARCHAR(30) NOT NULL,
	cidade VARCHAR(30) NOT NULL,
	PRIMARY KEY(login)
);

CREATE TABLE ator_diretor(
	id_ator_diretor INTEGER NOT NULL,
	nome_ator_diretor VARCHAR(30) NOT NULL,
	telefone VARCHAR(20),
	rua VARCHAR(30),
	cidade VARCHAR(30),
	estado VARCHAR(30),
	PRIMARY KEY(id_ator_diretor)
);

CREATE TABLE musico(
	nome_real VARCHAR(30) NOT NULL,
	estilo VARCHAR(30),
	data_nasc DATE,
	PRIMARY KEY(nome_real)
);

CREATE TABLE artista(
	id_artista INTEGER NOT NULL,
	nome_artista VARCHAR(60) NOT NULL,
	pais VARCHAR(30),
	genero VARCHAR(30),
	PRIMARY KEY(id_artista)
);

CREATE TABLE banda(
	id_artista INTEGER NOT NULL,
	PRIMARY KEY(id_artista),
	FOREIGN KEY(id_artista) REFERENCES Artista(id_artista)
);

CREATE TABLE cantor(
	id_artista INTEGER NOT NULL,
	nome_real VARCHAR(30) NOT NULL,
	PRIMARY KEY(id_artista),
	FOREIGN KEY(id_artista) REFERENCES Artista(id_artista),
	FOREIGN KEY(nome_real) REFERENCES Musico(nome_real)
);

CREATE TABLE categoria(
	nome_categoria VARCHAR(60) NOT NULL,
	nome_subcategoria VARCHAR(60),
	PRIMARY KEY(nome_categoria),
	FOREIGN KEY(nome_subcategoria) REFERENCES Categoria(nome_categoria)
);

CREATE TABLE ator(
	id_ator_diretor INTEGER NOT NULL,
	PRIMARY KEY(id_ator_diretor),
	FOREIGN KEY(id_ator_diretor) REFERENCES Ator_diretor(id_ator_diretor)
);

CREATE TABLE diretor(
	id_ator_diretor INTEGER NOT NULL,
	PRIMARY KEY(id_ator_diretor),
	FOREIGN KEY(id_ator_diretor) REFERENCES Ator_diretor(id_ator_diretor)
);

CREATE TABLE banda_musico(
	id_artista INTEGER NOT NULL,
	nome_real VARCHAR(30) NOT NULL,
	PRIMARY KEY(id_artista,nome_real),
	FOREIGN KEY(id_artista) REFERENCES Banda(id_artista),
	FOREIGN KEY(nome_real) REFERENCES Musico(nome_real)
);

CREATE TABLE bloqueia (
	login Integer NOT NULL,
	login_bloqueado Integer NOT NULL,
	razao VARCHAR(30) NOT NULL,
	PRIMARY KEY(login,login_bloqueado,razao),
    FOREIGN KEY(login) REFERENCES Pessoa(login),
	FOREIGN KEY(login_bloqueado) REFERENCES Pessoa(login)
);

CREATE TABLE gosta_artista(
	login INTEGER NOT NULL,
	id_artista INTEGER NOT NULL,
	nota INTEGER NOT NULL,
	PRIMARY KEY(login, id_artista, nota),
	FOREIGN KEY(login) REFERENCES Pessoa(Login),
	FOREIGN KEY(id_artista) REFERENCES Artista(id_artista)
);

CREATE TABLE registra(
	login INTEGER NOT NULL,
	login_amigo INTEGER NOT NULL,
	PRIMARY KEY(login,login_amigo),
	FOREIGN KEY(login) REFERENCES pessoa(login),
	FOREIGN KEY(login_amigo) REFERENCES pessoa(login)
);

CREATE TABLE filmes(
	id_filme INTEGER NOT NULL,
	nome_filme VARCHAR(30) NOT NULL,
	data_lancamento DATE NOT NULL,
	nome_categoria VARCHAR(20) NOT NULL,
	diretor INTEGER NOT NULL,
	PRIMARY KEY(id_filme),
	FOREIGN KEY(nome_categoria) REFERENCES Categoria(nome_categoria),
	FOREIGN KEY(diretor) REFERENCES diretor(id_ator_diretor)
);

CREATE TABLE gosta_filme(
	login INTEGER NOT NULL,
	id_filme INTEGER NOT NULL,
	nota INTEGER NOT NULL,
	PRIMARY KEY(login, id_filme),
	FOREIGN KEY(login) REFERENCES Pessoa(Login),
	FOREIGN KEY(id_filme) REFERENCES Filmes(id_filme)
);

CREATE TABLE ator_filmes(
	id_filme INTEGER NOT NULL,
	id_ator_diretor INTEGER NOT NULL,
	PRIMARY KEY(id_filme, id_ator_diretor),
	FOREIGN KEY(id_filme) REFERENCES Filmes(id_filme),
	FOREIGN KEY(id_ator_diretor) REFERENCES ator(id_ator_diretor)

);


------------------------------------------------------------------------------
------------------------------------------------------------------------------
------------------------------------------------------------------------------


INSERT INTO pessoa (login, nome, cidade) VALUES ('1', 'Patriky Galvão', 'Piên');
INSERT INTO pessoa (login, nome, cidade) VALUES ('2', 'Gabriel Loyola', 'Curitiba');
INSERT INTO pessoa (login, nome, cidade) VALUES ('3', 'Mozart Neto', 'Curitiba');
INSERT INTO pessoa (login, nome, cidade) VALUES ('4', 'William Souza', 'Piraquara');
INSERT INTO pessoa (login, nome, cidade) VALUES ('5', 'Tom Souza', 'Piraquara');
INSERT INTO pessoa (login, nome, cidade) VALUES ('6', 'Henrique Fejao', 'Piên');


INSERT INTO artista (id_artista, nome_artista, pais, genero) VALUES ('1', 'The Beatles', 'USA', 'Rock');
INSERT INTO artista (id_artista, nome_artista, pais, genero) VALUES ('2', 'Xuxa', 'Brasil', 'Infantil');
INSERT INTO artista (id_artista, nome_artista, pais, genero) VALUES ('3', 'Cazuza', 'Brasil', 'MPB');
INSERT INTO artista (id_artista, nome_artista, pais, genero) VALUES ('4', 'Racionais', 'Brasil', 'Rap');
INSERT INTO artista (id_artista, nome_artista, pais, genero) VALUES ('5', 'Ozuna', 'Porto Rico', 'Reggaeton');
INSERT INTO artista (id_artista, nome_artista, pais, genero) VALUES ('6', 'Pedro Paulo e Alex', 'Brasil', 'Sertanejo Universitário');
INSERT INTO artista (id_artista, nome_artista, pais, genero) VALUES ('7', 'Exaltasamba', 'Brasil', 'Pagode');


INSERT INTO gosta_artista (login, id_artista, nota) VALUES ('4', '4', '5');
INSERT INTO gosta_artista (login, id_artista, nota) VALUES ('4', '5', '4');
INSERT INTO gosta_artista (login, id_artista, nota) VALUES ('4', '6', '4');
INSERT INTO gosta_artista (login, id_artista, nota) VALUES ('1', '2', '5');
INSERT INTO gosta_artista (login, id_artista, nota) VALUES ('1', '3', '4');
INSERT INTO gosta_artista (login, id_artista, nota) VALUES ('1', '1', '3');
INSERT INTO gosta_artista (login, id_artista, nota) VALUES ('4', '2', '5');

-- Nome das pessoas que gostam da Xuxa;
--SELECT p.nome 
--FROM pessoa as p, artista as a, gosta_artista as g
--WHERE p.login = g.login and g.id_artista = a.id_artista and a.nome_artista = 'Xuxa'


INSERT INTO banda (id_artista) VALUES ('1');
INSERT INTO banda (id_artista) VALUES ('4');
INSERT INTO banda (id_artista) VALUES ('6');


INSERT INTO musico (nome_real, estilo, data_nasc) VALUES ('Agenor de Miranda Araújo Neto', 'MPB', '1970-01-01');
INSERT INTO musico (nome_real, estilo, data_nasc) VALUES ('John Lennon', 'Rock', '1940-10-09');
INSERT INTO musico (nome_real, estilo, data_nasc) VALUES ('Paul McCartney', 'Rock', '1942-06-18');
INSERT INTO musico (nome_real, estilo, data_nasc) VALUES ('George Harrison', 'Rock', '1943-02-25');
INSERT INTO musico (nome_real, estilo, data_nasc) VALUES ('Ringo Starr', 'Rock', '1940-07-07');
INSERT INTO musico (nome_real, estilo, data_nasc) VALUES ('Maria da Graça Meneghel', 'Infantil', '1963-03-27');
INSERT INTO musico (nome_real, estilo, data_nasc) VALUES ('Juan Carlos Ozuna Rosado', 'Reggaeton', '1992-03-13');
INSERT INTO musico (nome_real, estilo, data_nasc) VALUES ('Mano Brown', 'Rap', '1970-04-22');
INSERT INTO musico (nome_real, estilo, data_nasc) VALUES ('Edi Rock', 'Rap', '1968-09-20');
INSERT INTO musico (nome_real, estilo, data_nasc) VALUES ('Ice Blue', 'Rap', '1969-03-16');
INSERT INTO musico (nome_real, estilo, data_nasc) VALUES ('KL Jay', 'Rap', '1969-08-10');
INSERT INTO musico (nome_real, estilo, data_nasc) VALUES ('Alex Stella', 'Sertanejo', '1980-01-01');
INSERT INTO musico (nome_real, estilo, data_nasc) VALUES ('Pedro Paulo Santos', 'Sertanejo', '1980-01-01');


INSERT INTO banda_musico (id_artista, nome_real) VALUES ('1', 'John Lennon');
INSERT INTO banda_musico (id_artista, nome_real) VALUES ('1', 'Paul McCartney');
INSERT INTO banda_musico (id_artista, nome_real) VALUES ('1', 'George Harrison');
INSERT INTO banda_musico (id_artista, nome_real) VALUES ('1', 'Ringo Starr');
INSERT INTO banda_musico (id_artista, nome_real) VALUES ('4', 'Mano Brown');
INSERT INTO banda_musico (id_artista, nome_real) VALUES ('4', 'Edi Rock');
INSERT INTO banda_musico (id_artista, nome_real) VALUES ('4', 'Ice Blue');
INSERT INTO banda_musico (id_artista, nome_real) VALUES ('4', 'KL Jay');
INSERT INTO banda_musico (id_artista, nome_real) VALUES ('6', 'Alex Stella');
INSERT INTO banda_musico (id_artista, nome_real) VALUES ('6', 'Pedro Paulo Santos');


INSERT INTO cantor (id_artista, nome_real) VALUES ('2', 'Maria da Graça Meneghel');
INSERT INTO cantor (id_artista, nome_real) VALUES ('3', 'Agenor de Miranda Araújo Neto');
INSERT INTO cantor (id_artista, nome_real) VALUES ('5', 'Juan Carlos Ozuna Rosado');


INSERT INTO ator_diretor (id_ator_diretor, nome_ator_diretor, telefone, rua, cidade, estado) VALUES ('1', 'Ator1', '111-111', 'Rua Atlântica', 'São Francisco do Sul', 'Santa Catarina');
INSERT INTO ator_diretor (id_ator_diretor, nome_ator_diretor, telefone, rua, cidade, estado) VALUES ('2', 'Ator2', '111-222', 'Av. 7 de setembro', 'Curitiba', 'Paraná');
INSERT INTO ator_diretor (id_ator_diretor, nome_ator_diretor, telefone, rua, cidade, estado) VALUES ('3', 'Diretor1', '222-111', 'Rua Treze', 'São Paulo','São Paulo');
INSERT INTO ator_diretor (id_ator_diretor, nome_ator_diretor, telefone, rua, cidade, estado) VALUES ('4', 'Diretor2', '123-321', 'Rua Amarela', 'Piraquara do Acre', 'Acre');
INSERT INTO ator_diretor (id_ator_diretor, nome_ator_diretor, telefone, rua, cidade, estado) VALUES ('5', 'Ator3', '123-123', 'Rua dos indígenas', 'Piraquara', 'Paraná');
INSERT INTO ator_diretor (id_ator_diretor, nome_ator_diretor, telefone, rua, cidade, estado) VALUES ('6', 'Ator4', '321-321', 'Rua 25', 'Não Me Toque', 'Rio Grande do Sul');


INSERT INTO ator (id_ator_diretor) VALUES ('1');
INSERT INTO ator (id_ator_diretor) VALUES ('2');
INSERT INTO ator (id_ator_diretor) VALUES ('5');
INSERT INTO ator (id_ator_diretor) VALUES ('6');

INSERT INTO diretor(id_ator_diretor) VALUES ('3');
INSERT INTO diretor(id_ator_diretor) VALUES ('4');


INSERT INTO bloqueia (login, login_bloqueado, razao) VALUES ('1', '3', 'Span');
--INSERT INTO bloqueia (login, login_bloqueado, razao) VALUES ('1', '3', 'Cara chato'); ## ERROR:  duplicate key value violates unique constraint "bloqueia_pkey" Detail: Key (login, login_bloqueado)=(1, 3) already exists.
INSERT INTO bloqueia (login, login_bloqueado, razao) VALUES ('2', '4', 'Nao conheco');
INSERT INTO bloqueia (login, login_bloqueado, razao) VALUES ('4', '3', 'Span');


INSERT INTO registra (login, login_amigo) VALUES ('1', '2');
INSERT INTO registra (login, login_amigo) VALUES ('1', '3');
INSERT INTO registra (login, login_amigo) VALUES ('1', '4');
INSERT INTO registra (login, login_amigo) VALUES ('2', '1');
INSERT INTO registra (login, login_amigo) VALUES ('2', '3');
INSERT INTO registra (login, login_amigo) VALUES ('5', '1');
INSERT INTO registra (login, login_amigo) VALUES ('5', '6');
INSERT INTO registra (login, login_amigo) VALUES ('3', '2');
INSERT INTO registra (login, login_amigo) VALUES ('6', '1');
INSERT INTO registra (login, login_amigo) VALUES ('6', '4');
INSERT INTO registra (login, login_amigo) VALUES ('4', '2');
INSERT INTO registra (login, login_amigo) VALUES ('4', '3');


INSERT INTO categoria (nome_categoria) VALUES ('Espionagem');
INSERT INTO categoria (nome_categoria, nome_subcategoria) VALUES ('Romance', 'Espionagem');
INSERT INTO categoria (nome_categoria, nome_subcategoria) VALUES ('Guerra', 'Romance');
INSERT INTO categoria (nome_categoria, nome_subcategoria) VALUES ('Ficção', 'Guerra');
INSERT INTO categoria (nome_categoria, nome_subcategoria) VALUES ('Ação', 'Ficção');
INSERT INTO categoria (nome_categoria, nome_subcategoria) VALUES ('Policial', 'Ação');
INSERT INTO categoria (nome_categoria, nome_subcategoria) VALUES ('Comédia', 'Romance');
INSERT INTO categoria (nome_categoria, nome_subcategoria) VALUES ('Terror', 'Comédia');

INSERT INTO filmes (id_filme, nome_filme, data_lancamento, nome_categoria, diretor) VALUES ('1', 'Harry Potter 1', '2000-01-01', 'Ficção', '3');
INSERT INTO filmes (id_filme, nome_filme, data_lancamento, nome_categoria, diretor) VALUES ('2', 'Harry Potter 2', '2001-01-01', 'Ficção', '3');
INSERT INTO filmes (id_filme, nome_filme, data_lancamento, nome_categoria, diretor) VALUES ('3', 'Lagoa Azul', '1990-01-01', 'Romance', '4');
INSERT INTO filmes (id_filme, nome_filme, data_lancamento, nome_categoria, diretor) VALUES ('4', 'Bethoven', '1989-01-10', 'Comédia', '4');
INSERT INTO filmes (id_filme, nome_filme, data_lancamento, nome_categoria, diretor) VALUES ('5', 'X Man', '2010-10-10', 'Ação', '3');


INSERT INTO gosta_filme (login, id_filme, nota) VALUES ('1', '2', '4');
INSERT INTO gosta_filme (login, id_filme, nota) VALUES ('1', '5', '5');
INSERT INTO gosta_filme (login, id_filme, nota) VALUES ('3', '1', '3');
INSERT INTO gosta_filme (login, id_filme, nota) VALUES ('3', '5', '3');
INSERT INTO gosta_filme (login, id_filme, nota) VALUES ('4', '1', '5');
INSERT INTO gosta_filme (login, id_filme, nota) VALUES ('4', '2', '5');
INSERT INTO gosta_filme (login, id_filme, nota) VALUES ('6', '3', '4');
INSERT INTO gosta_filme (login, id_filme, nota) VALUES ('6', '4', '2');


INSERT INTO ator_filmes (id_filme, id_ator_diretor) VALUES ('1', '1');
INSERT INTO ator_filmes (id_filme, id_ator_diretor) VALUES ('3', '2');
INSERT INTO ator_filmes (id_filme, id_ator_diretor) VALUES ('4', '5');
INSERT INTO ator_filmes (id_filme, id_ator_diretor) VALUES ('5', '6');
INSERT INTO ator_filmes (id_filme, id_ator_diretor) VALUES ('5', '1');
INSERT INTO ator_filmes (id_filme, id_ator_diretor) VALUES ('3', '1');