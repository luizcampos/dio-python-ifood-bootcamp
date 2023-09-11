create schema if not exists company;
use company;

create table employee(
	Fname varchar(15) NOT NULL,
    Minit char,
    Lname varchar(15) NOT NULL,
    Ssn char(9) NOT NULL,
    Bdate DATE,
    Address varchar(30),
    sex char,
    Salary decimal(10, 2),
    Super_ssn char(9),
    Dno int NOT NULL,
    constraint chk_salary_employee check (Salary > 2000.0),
    constraint pk_employee primary key (Ssn)
);

create table department(
	Dname varchar(15) NOT NULL,
    Dnumber int NOT NULL,
    Mgr_ssn char(9),
    Mgr_start_date DATE,
    Dept_create_date date,
    constraint chk_date_dept check (Dept_create_date < Mgr_start_date),
    constraint pk_dept primary key (Dnumber),
    constraint unique_name_dept Unique (Dname),
    foreign key (Mgr_ssn) references employee(Ssn)
);

create table dept_locations(
	Dnumber int NOT NULL,
    Dlocation varchar(15) NOT NULL,
    constraint pk_dept_locations primary key (Dnumber, Dlocation),
    constraint fk_dept_locations foreign key (Dnumber) references department(Dnumber)
);

alter table dept_locations drop constraint fk_dept_locations;

alter table dept_locations
	add constraint fk_dept_locations foreign key (Dnumber) references department(Dnumber) on delete cascade
    on update cascade;

create table project(
	Pname varchar(15) NOT NULL,
    Pnumber int NOT NULL, 
    Plocation varchar(15),
    Dnum int NOT NULL,
    primary key(Pnumber),
    constraint unique_project unique (Pname),
    constraint fk_project foreign key (Dnum) references department(Dnumber)
);

create table works_on(
	Essn char(9) NOT NULL, 
    Pno int NOT NULL,
    Hours decimal (3,1) NOT NULL,
    primary key(Essn, Pno),
    constraint fk_works_on foreign key (Essn) references employee (Ssn),
    constraint fk_works_on foreign key (Pno) references project (Pnumber)
);

drop table dependent;
create table dependent(
	Essn char(9) NOT NULL,
    Dependent_name varchar(15) NOT NULL,
    Sex char,
    Bdate Date,
    Relationship varchar(8),
    -- Age int NOT NULL,
    -- constraint chk_age_dependent check (Age < 21),
    constraint pk_dept primary key (Essn, Dependent_name),
    constraint fk_dependent foreign key (Essn) references employee(Ssn)
);

show tables;
desc employee;
desc works_on;

insert into employee values ('John', 'B', 'Smith', 123456789, '1965-01-09', '731-Fondren-Houston-TX', 'M', 30000, null, 5), ('Franklin', 'T', 'Wong', 3334445555, '1955-12-08', '638-Voss-Houston-TX', 'M', 40000, 1234568798, 5), ('Maria', 'T', 'Wong', 333444555, '1955-12-08', '638-Voss-Houston-TX', 'F', 40000, 123457798, 5);

desc dependent;
insert into dependent values (333444555, 'Alice', 'F', '1986-04-05', 'Daughter'), (333444555, 'Joy', 'F', '1999-04-05', 'Daughter'), (123456789, 'Michael', 'M', '1999-08-15', 'Son');

desc department;
select * from department;
insert into department values ('Research', 5, 333444555, '1988-05-22'), ('Administration', 4, 123456789, '1995-01-01');

desc dept_locations;
insert into dept_locations values (4, 'Stafford'), (5, 'Bellaire');

desc project;
insert into project values ('ProductX', 1, 'Bellaire', 5), ('ProductY', 2, 'Houston', 5), ('ProductZ', 3, 'Houston', 4);

select Fname, Lname, Salary, Salary*0.011 from employee;

-- recuperando infos dos departamentos presentes em Stafford
select Dname as Department_Name, Mgr_ssn as Manager from department d, dept_locations l, employee e where d.Dnumber = l.Dnumber and Dlocation='Stafford'; -- Dnumber é igual, por isso usa o Alias

-- recuperando todos os gerentes que trabalham em Stafford
select Dname as Department_Name, concat(Fname, ' ', Lname) as Manager from department d, dept_locations l, employee e where d.Dnumber = l.Dnumber and Dlocation='Stafford' and Mgr_ssn = e.Ssn; -- Dnumber é igual, por isso usa o Alias

-- usando Like
select concat(Fname, ' ', Lname) Complete_Name, Address from employee where (Address like '%Houston%');

-- usando Between
select Fname, Lname from employee where (Salary between 20000 and 40000);


-- operadores lógicos (and, or, =)

select Fname, Lname from employee, department where Dname = 'Research' and Dnumber=Dno;


-- EXISTS and UNIQUE com Nested Query (query aninhada)

select e.Fname, e.Lname from employee as e 
	where exists (select * from dependent as d 
					where e.Ssn = d.Essn);
                    
select Fname as Nome from employee;

-- ORDER BY
select * from employee order by Fname asc;
select * from employee order by Fname desc;


-- COUNT
select count(*) from employee;

-- GROUP BY
select Dno, count(*) as Number_of_employees, round(avg(Salary),2) as Salary_avg from employee group by Dno;

select Pnumber, Pname, count(*)
	from project, works_on
	where Pnumber = Pno
	group by Pnumber, Pname;
    
    select sum(Salary) as total_sal, max(Salary) as Max_sal, min(Salary) as Min_sal, round(avg(Salary),2) as Avg_sal from employee;
    
    
-- HAVING e GROUP BY
-- Ex: só vai exibir se houver registros >2 no GROUP BY
select Pnumber, Pname, count(*)
from project, works_on
where Pnumber = Pno
group by Pnumber, Pname
having count(*) > 2;

select Dno, count(*)
from employee
where salary > 30000
group by Dno
having count(*)>=1;

-- CASE Statement

select* from employee;

update employee set Salary = 
	case
		when Dno=5 then Salary+2000
        when Dno=4 then Salary+3000
        else Salary+0
	end;
    
    
-- JOIN / CROSS JOIN
select * from employee JOIN department;

-- INNER JOIN
select * from employee JOIN department on Ssn = Mgr_ssn;

select Dname, Dept_create_date, Dlocation
	from department JOIN dept_locations using(Dnumber)
    order by Dept_create_date;
    
-- INNER JOIN c/ + de 2 tabelas
-- tabelas: employee, works_on e project
select * from employee
	inner join works_on on Ssn = Essn
    inner join project on Pno = Pnumber
    order by Pnumber;
    
select Dnumber, Dname, concat(Fname, ' ', Lname) as Manager, Salary, round(Salary*0.05,2) as Bonus from department
	inner join dept_locations using(Dnumber)
	inner join (dependent inner join employee on Ssn = Essn) on Ssn = Mgr_ssn
    group by Dnumber;
    
    
-- OUTER JOIN
select * from employee left outer join dependent on Ssn = Essn;