Create Database PortalDeFestas;

Create Table Empresa(
    cod_emp int not null primary key,
    nome_emp varchar(30) not null,
    telefone_emp varchar(11),
    endereco varchar(30)
);

Create Table Cliente(
    cod_cli int not null primary key,
    nome_cli varchar(30) not null,
    cpf_cli varchar(30) not null,
    telefone_cli varchar(11),
    endereco varchar(30)
);

Create Table Funcionario(
    cod_fun int not null primary key,
    nome_fun varchar(30) not null,
    telefone_fun varchar(11),
    endereco_fun varchar(30),
    disp_fun varchar(20),
    cod_emp int not null,
    equip_fun varchar(30),
    constraint foreign key (cod_emp) references Empresa(cod_emp)
);

Create Table Extra(
    cod_ext int not null primary key,
    nome_ext varchar(30),
    preco_ext int not null,
    disp_ext varchar(20),
    hora_ext int,
    tipo_ext varchar(30)
);

Create Table Festa(
    cod_fes int not null primary key,
    preco_fes int not null,
    tipo_fes varchar(30) not null,
    nome_fes varchar(30) not null,
    status_fes varchar(5),
    duracao_fes int,    
    cod_cli int not null,
    cod_emp int not null,
    constraint foreign key (cod_emp) references Empresa(cod_emp),
    constraint foreign key (cod_cli) references Cliente(cod_cli)
);

Create Table Servico(
    cod_fes int not null,
    cod_ext int not null,
    primary key(cod_fes, cod_ext),
    constraint foreign key (cod_fes) references Festa(cod_fes),
    constraint foreign key (cod_ext) references Extra(cod_ext)
);


create function fn_Conta (a int)
returns varchar(500) deterministic
return(
    select sum(preco_ext) + preco_fes as Total
    from Festa f inner join Cliente c on f.cod_cli= c.cod_cli
    inner join Servico s on s.cod_fes = f.cod_fes
    inner join Extra e on e.cod_ext = s.cod_ext
    where f.cod_fes = a
    group by f.cod_fes
);

delimiter $$
create procedure pro_ExtrasFesta(inout a int)
begin
    select e.nome_ext as "Tipo de Extra"
    from Extra e inner join Servico s on e.cod_ext= s.cod_ext
    inner join Festa f on f.cod_fes= s.cod_fes
    where f.cod_fes = a;
    select e.cod_ext as "Código do Extra"
    from Extra e inner join Servico s on e.cod_ext= s.cod_ext
    inner join Festa f on f.cod_fes= s.cod_fes
    where f.cod_fes = a;
end $$
delimiter ;

delimiter $$
create procedure pro_FestaRealizada (in a int)
begin
    select f.nome_fes as "Nome da Festa"
    from Festa f 
    where f.cod_fes = a;
    select c.nome_cli as "Nome do Cliente"
    from Cliente c inner join Festa f on c.cod_cli= f.cod_cli
    where f.cod_fes = a;
    select e.nome_emp as "Nome da Empresa"
    from Empresa e inner join Festa f on e.cod_emp= f.cod_emp
    inner join Cliente c on c.cod_cli= f.cod_cli
    where f.cod_fes = a;
end $$
delimiter ;

delimiter $$
create trigger tr_DisponibilidadeExtra after insert
on Festa for each row
begin
    update Extra set disp_ext = "Indisponível"
    where disp_ext = "Disponível";
end $$
delimiter ;

delimiter $$
create trigger tr_IndisponibilidadeExtra before delete
on Festa for each row
begin
    update Extra set disp_ext = "Disponível"
    where disp_ext = "Indisponível";
end $$
delimiter ;

delimiter $$
create trigger tr_DisponibilidadeFuncionario after insert
on Festa for each row
begin
    update Funcionario set disp_fun = "Indisponível"
    where disp_fun = "Disponível";
end $$
delimiter ;

delimiter $$
create trigger tr_IndisponibilidadeFuncionario before delete
on Festa for each row
begin
    update Funcionario set disp_fun = "Disponível"
    where disp_fun = "Indisponível";
end $$
delimiter ;