create table if not exists users (
    id int unsigned auto_increment primary key,
    nome varchar(20) not null,
    senha varchar(20) not null,
    last_login date
);