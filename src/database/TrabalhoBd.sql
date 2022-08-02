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
    disp_fun int,
    cod_emp int not null,
    equip_fun varchar(30),
    constraint foreign key (cod_emp) references Empresa(cod_emp)
);

Create Table Extra(
    cod_ext int not null primary key,
    nome_ext varchar(30),
    preco_ext int not null,
    disp_ext int,
    hora_ext int,
    tipo_ext varchar(30)
);

Create Table Festa(
    cod_fes int not null primary key,
    preco_fes int not null,
    tipo_fes varchar(30) not null,
    nome_fes varchar(30) not null,
    duracao_fes int,
    status_fes varchar(5),
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
create view Conta as
select f.nome_fes as "Nome Da Festa", c.nome_cli as "Comprador" , sum(preco_ext) + preco_fes as Total
from Festa f inner join Cliente c on f.cod_cli= c.cod_cli
inner join Servico s on s.cod_fes = f.cod_fes
inner join Extra e on e.cod_ext = s.cod_ext
group by f.nome_fes, c.nome_cli;
