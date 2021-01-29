create table if not exists produtos (
    id int unsigned auto_increment primary key,
    nome varchar(50) not null,
    marca varchar(50) not null,
    tipo varchar(20),
    valor int not null
);