
create database teste;
use teste;

create table R(
	A char(2)
);
    
create table S(
	A char(2)
);
    
insert into R(A) values('a1'),('a2'),('a2'),('a3');
insert into S(A) values('a1'),('a1'),('a2'),('a3'),('a4'),('a5');

select * from R;

-- tudo que está em S e não está em R (EXCEPT)
select * from S where A not in (select A from R);

-- UNION
(select distinct R.A from R) UNION (select distinct S.A from S);

-- INTERSECT
select R.A from R where R.A in (select S.A from S); 

-- INTERSECT - tira as redundâncias
select distinct R.A from R where R.A in (select S.A from S); 


