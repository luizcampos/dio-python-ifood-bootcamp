show databases;
create database if not exists first_example;
use first_example;
show tables;
CREATE TABLE person(
	person_id smallint unsigned,
	fname varchar(20),
	lname varchar(20),
	gender enum('M','F'),
	birth_date DATE,
	street varchar(30),
	city varchar(20),
	state varchar(20),
	country varchar(20),
	postal_code varchar(20),
    constraint pk_person primary key (person_id)
);

desc person;

CREATE TABLE favorite_food(
	person_id smallint unsigned,
    food varchar(20),
    constraint pk_favorite_food primary key (person_id, food),
    constraint fk_favorite_food_person_id foreign key(person_id) references person(person_id)
);

desc favorite_food;

SELECT * FROM information_schema.table_constraints WHERE constraint_schema = 'first_example';

INSERT INTO person values ('2', 'Luiz', 'Campos', 'M', '5985-07-26', 'Rua tal 2', 'Cidade RJ', 'RJ', 'Brasil', '258741-65'), ('3', 'Amanda', 'Silva', 'F', '4587-02-17', 'Rua tal 3', 'São Paulo', 'SP', 'Brasil', '258741-65');

SELECT * FROM person;

INSERT INTO favorite_food values (1, 'Lasanha'), (2, 'Sushi');

select * FROM favorite_food;