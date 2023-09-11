-- criação BD
-- drop database ecommerce;
create database ecommerce;
use ecommerce;

create table client(
	idClient int auto_increment primary key,
	Fname varchar(10),
    Minit char(3),
    Lname varchar(20),
    CPF char(11) not null,
    Address varchar(30),
    constraint unique_cpf_client unique (CPF)
);

desc client;

create table product(
	idProduct int auto_increment primary key,
    Pname varchar(10) not null,
    classification_kids bool default false,
    category enum('Eletrônico', 'Vestimenta', 'Brinquedos', 'Alimentos', 'Móveis') not null,
    avaliacao float default 0,
    size varchar(10)
);

create table payments(
	idClient int,
    idPayment int,
    typePayment enum('Boleto', 'Cartão', 'Dois cartões'),
    limitAvailable float,
    primary key(idClient, idPayment)
);

drop table orders;
-- Pedidos
create table orders(
	idOrder int auto_increment primary key,
    idOrderClient int,
    orderStatus enum('Cancelado', 'Confirmado', 'Em processamento') default 'Em processamento',
    orderDescription varchar(255),
    sendValue float default 10,
    paymentCash boolean default false,
    constraint fk_orders_client foreign key (idOrderClient) references client(idClient)
		on update cascade
);

desc orders;

create table productStorage(
	idProdStorage int auto_increment primary key,
    storageLocation varchar(255),
    quantity int default 0
);

-- Fornecedor
create table supplier(
	idSupplier int auto_increment primary key,
    SocialName varchar(255) not null, 
    CNPJ char(15) not null,
    contact char(11) not null,
    constraint unique_supplier unique (CNPJ)
);

desc supplier;


-- Vendedor
create table seller(
	idSeller int auto_increment primary key,
    SocialName varchar(255) not null, 
    AbstName char(255),
    CNPJ char(15),
    CPF char(9),
    location varchar(255),
    contact char(11) not null,
    constraint unique_cnpj_seller unique (CNPJ),
    constraint unique_cpf_seller unique (CPF)
);

create table productSeller(
	idPseller int,
    idPproduct int,
    prodQuantity int default 1,
    primary key (idPseller, idPproduct),
    constraint fk_product_seller foreign key (idPseller) references seller(idSeller),
    constraint fk_product_product foreign key (idPproduct) references product(idProduct)
);

-- quais produtos estão associados aos vendedores
desc productSeller;


create table productOrder(
	idPOproduct int,
    idPOorder int,
    poQuantity int default 1,
    poStatus enum('Disponível', 'Sem estoque') default 'Disponível',
    primary key (idPOproduct, idPOorder),
    constraint fk_productorder_seller foreign key (idPOproduct) references product(idProduct),
    constraint fk_productorder_product foreign key (idPOorder) references orders(idOrder)
);

create table storageLocation(
	idLproduct int,
    idLstorage int,
    location varchar(255) not null,
    primary key (idLproduct, idLstorage),
    constraint fk_storage_location_product foreign key (idLproduct) references product(idProduct),
    constraint fk_storage_location_storage foreign key (idLstorage) references productStorage(idProdStorage)
);

create table productSupplier(
	idPsSupplier int,
    idPsProduct int,
    quantity int not null,
    primary key (idPsSupplier, idPsProduct),
    constraint fk_product_supplier_supplier foreign key (idPsSupplier) references supplier(idSupplier),
    constraint fk_product_supplier_product foreign key (idPsProduct) references product(idProduct)
);

desc productSupplier;

show tables;

alter table client auto_increment=1;
alter table product auto_increment=1;
alter table orders auto_increment=1;
alter table seller auto_increment=1;
alter table supplier auto_increment=1;

insert into Client (Fname, Minit, Lname, CPF, Address)
		values('Maria', 'M', 'Silva', 123456789, 'Rua Silva 29, Caran - Flores'),
			('Fellipe', 'O', 'Pimentel', 987654321, 'Rua Ala 289, Centro - Flores'),
            ('Roberta', 'G', 'Assis', 147258369, 'Rua Laras 833, Centro - Flores'),
            ('Ricado', 'F', 'Silva', 963258741, 'Avenida JK 19, Clara - SP');

insert into product (Pname, classification_kids, category, avaliacao, size) values
	('Fone', false, 'Eletrônico', '4', null),
    ('Barbie', true, 'Brinquedos', '3', null),
    ('Sofá', false, 'Móveis', '3', '3x57x80'),
    ('Farinha', false, 'Alimentos', '2', null);
    
insert into orders (idOrderClient, orderStatus, orderDescription, sendValue, paymentCash) values
	(13, default, 'compra via app', null,1),
    (14, default, 'compra via app', 50, 0),
    (15, 'Confirmado', null, null, 1),
    (16, default, 'compra via web site', 150, 0);

select * from client;
select * from orders;
select * from product;

insert into productOrder (idPOproduct, idPOorder, poQuantity, poStatus) values
	(1, 9, 2, null),
    (2, 10, 2, null),
    (3, 11, 2, null);
    
insert into productStorage (storageLocation, quantity) values
	('Rio de Janeiro', 1000),
    ('Rio de Janeiro', 500),
    ('São Paulo', 10),
    ('São Paulo', 100),
    ('São Paulo', 10),
    ('Brasília', 60);
    
insert into storageLocation (idLproduct, idLstorage, location) values
	(1, 2, 'RJ'),
    (2, 6, 'GO');
    
insert into supplier (SocialName, CNPJ, contact) values
	('Almeida e filhos', 123456789123456, '21985474'),
    ('Eletrônicos Silva', 854519649143457, '21985484'),
    ('Eletrônicos Valma', 934567893934659, '22485481');
    
select * from supplier;

insert into productSupplier (idPsSupplier, idPsProduct, quantity) values
	(1, 1, 500),
    (1, 2, 400),
    (2, 4, 633),
    (3, 3, 5);
    

insert into seller (SocialName, AbstName, CNPJ, CPF, location, contact)
		values('Tech Eletronics', null, 123456789456321, null, 'Flores', 1258745986),
			('Botique Luiz', null, null, 123456783, 'São Paul', 2154789658),
            ('Kids World', null, 444456789456321, null, 'Rio de Janeiro', 1145789568);

insert into productSeller (idPseller, idPproduct, prodQuantity) values
	(1, 1, 80),
    (2, 2, 10);
    
-- Queries

-- Qtde de clientes
select count(*) from client;

-- 2- Pedidos feitos
select * from client c, orders o where c.idClient = idOrderClient;

select * from orders;
select * from client c inner join orders o on c.idClient = o.idOrderClient
			inner join productOrder p on p.idPOorder = o.idOrder;