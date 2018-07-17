# 1. Qual é a média e desvio padrão dos ratings para artistas musicais e filmes?
select movieUri 'artistas musicais e filmes', avg(rating) 'media', STDDEV(rating) 'desvio'
	from likesmovie
group by movieUri
UNION
select bandUri 'artistas musicais e filmes', avg(rating) 'media', STDDEV(rating) 'desvio padrao'
	from likesmusic
group by bandUri;


# 2. Quais são os artistas e filmes com o maior rating médio curtidos por pelo menos duas pessoas? Ordenados por rating médio
select movieUri 'artistas musicais e filmes', avg(rating) 'media', STDDEV(rating) 'desvio padrao'
	from likesmovie
group by movieUri
having count(movieUri)>1
UNION
select bandUri 'artistas musicais e filmes', avg(rating) 'media', STDDEV(rating) 'desvio padrao'
	from likesmusic
group by bandUri
having count(bandUri)>1
order by 2 desc;


# 3. Quais são os 10 artistas musicais e filmes mais populares? Ordenados por popularidade
select movieUri 'artistas musicais e filmes', count(*) total
	from likesmovie
group by movieUri
UNION
select bandUri 'artistas musicais e filmes', count(*) total
	from likesmusic
group by bandUri
order by 2 desc
limit 10;


# 4. Crie uma view chamada ConheceNormalizada que represente simetricamente os relacionamentos de conhecidos da turma. Por exemplo, 
# se a conhece b mas b não declarou conhecer a, a view criada deve conter o relacionamento (b,a) além de (a,b).

create view conhecidos as
select distinct k1.person a, k2.person b
from knows k1
	left join knows k2 on k1.person = k2.colleague
having a <> b
UNION
select distinct  k1.person a, k2.person b
from knows k1
	right join knows k2 on k1.person = k2.colleague
having a <> b
order by 2 desc,1 desc;


# 5. Quais são os conhecidos (duas pessoas ligadas na view ConheceNormalizada) que compartilham o maior numero de filmes curtidos?
# 6. Qual o número de conhecidos dos conhecidos (usando ConheceNormalizada) para cada integrante do seu grupo?

# 7. Construa um gráfico para a função f(x) = (número de pessoas que curtiram exatamente x filmes)
SELECT p.name, lm.movieUri, COUNT(*) 
FROM persons p
	LEFT JOIN likesmovie lm ON lm.person = p.uri
GROUP BY p.name
ORDER BY COUNT(*) DESC;
    
# 8. Construa um gráfico para a função f(x) = (número de filmes curtidos por exatamente x pessoas)
SELECT lm.movieUri, COUNT(*) 
FROM likesmovie lm 
	LEFT JOIN persons p ON lm.person = p.uri
GROUP BY lm.movieUri
ORDER BY COUNT(*) DESC;

# 9. Defina duas outras informações (como as anteriores) que seriam úteis para compreender melhor a rede

# 9.1 A disposicao de filmes por cidade natal dos alunos
SELECT hometown, COUNT(*)
FROM persons
GROUP BY hometown
ORDER BY COUNT(*) DESC;

SELECT p.hometown, COUNT(*)
FROM persons p
	LEFT JOIN likesmovie lm ON lm.person = p.uri
GROUP BY p.hometown
ORDER BY COUNT(*) DESC;

# 9.2 disposicao de filmes melhores avaliados por cidade
SELECT p.hometown, AVG(lm.rating)
FROM persons p
	LEFT JOIN likesmovie lm ON lm.person = p.uri
GROUP BY p.hometown
ORDER BY AVG(lm.rating) DESC;
