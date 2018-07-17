CREATE TABLE persons (
  uri varchar(150) NOT NULL,
  name varchar(80) NOT NULL,
  hometown varchar(50) NOT NULL,
  PRIMARY KEY (uri)
);

CREATE TABLE knows (
  person varchar(150) NOT NULL,
  colleague varchar(150) NOT NULL,
  PRIMARY KEY (person,colleague),
  KEY colleague (colleague),
  FOREIGN KEY (person) REFERENCES persons (uri),
  FOREIGN KEY (colleague) REFERENCES persons (uri)
);

CREATE TABLE bloqueia (
	person varchar(150) NOT NULL,
	blocked_person varchar(150) NOT NULL,
	reason VARCHAR(30) NOT NULL,
	PRIMARY KEY(person,blocked_person,reason),
    FOREIGN KEY(person) REFERENCES persons(uri),
	FOREIGN KEY(blocked_person) REFERENCES persons(uri)
);


CREATE TABLE likes_movie (
  person varchar(150) NOT NULL,
  rating int(11) NOT NULL,
  movieUri varchar(150) NOT NULL,
  PRIMARY KEY (person,movieUri),
  FOREIGN KEY (person) REFERENCES persons(uri)
);

CREATE TABLE likes_music (
  person varchar(150) NOT NULL,
  rating int(11) NOT NULL,
  bandUri varchar(150) NOT NULL,
  PRIMARY KEY (person,bandUri),
  FOREIGN KEY (person) REFERENCES persons (uri)
);

CREATE TABLE categoria(
	nome_categoria VARCHAR(60) NOT NULL,
	nome_subcategoria VARCHAR(60),
	PRIMARY KEY(nome_categoria),
	FOREIGN KEY(nome_subcategoria) REFERENCES Categoria(nome_categoria)
);


CREATE TABLE musico(
	nome_real VARCHAR(30) NOT NULL,
	estilo VARCHAR(30),
	data_nasc DATE,
	PRIMARY KEY(nome_real)
);

CREATE TABLE artista(
	bandUri varchar(150) NOT NULL,
	nome_artista VARCHAR(60) NOT NULL,
	pais VARCHAR(30),
	genero VARCHAR(30),
	PRIMARY KEY(bandUri)
);


CREATE TABLE banda(
	bandUri varchar(150) NOT NULL,
	PRIMARY KEY(bandUri),
	FOREIGN KEY(bandUri) REFERENCES artista(bandUri)
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


CREATE TABLE cantor(
	bandUri varchar(150) NOT NULL,
	nome_real VARCHAR(30) NOT NULL,
	PRIMARY KEY(bandUri),
	FOREIGN KEY(bandUri) REFERENCES artista(bandUri),
	FOREIGN KEY(nome_real) REFERENCES Musico(nome_real)
);

CREATE TABLE ator(
	id_ator_diretor INTEGER NOT NULL,
	PRIMARY KEY(id_ator_diretor),
	FOREIGN KEY(id_ator_diretor) REFERENCES Ator_diretor(id_ator_diretor)
);


CREATE TABLE filmes(
	movieUri varchar(150) NOT NULL,
	nome_filme VARCHAR(30) NOT NULL,
	data_lancamento DATE NOT NULL,
	nome_categoria VARCHAR(20) NOT NULL,
	diretor INTEGER NOT NULL,
	PRIMARY KEY(movieUri),
	FOREIGN KEY(nome_categoria) REFERENCES Categoria(nome_categoria),
	FOREIGN KEY(diretor) REFERENCES diretor(id_ator_diretor)
);

CREATE TABLE diretor(
	id_ator_diretor INTEGER NOT NULL,
	PRIMARY KEY(id_ator_diretor),
	FOREIGN KEY(id_ator_diretor) REFERENCES Ator_diretor(id_ator_diretor)
);


CREATE TABLE ator_filmes(
	movieUri varchar(150) NOT NULL,
	id_ator_diretor INTEGER NOT NULL,
	PRIMARY KEY(movieUri, id_ator_diretor),
	FOREIGN KEY(movieUri) REFERENCES filmes(movieUri),
	FOREIGN KEY(id_ator_diretor) REFERENCES ator(id_ator_diretor)
);


CREATE TABLE banda_musico(
	bandUri varchar(150) NOT NULL,
	nome_real VARCHAR(30) NOT NULL,
	PRIMARY KEY(bandUri,nome_real),
	FOREIGN KEY(bandUri) REFERENCES banda(bandUri),
	FOREIGN KEY(nome_real) REFERENCES musico(nome_real)
);
