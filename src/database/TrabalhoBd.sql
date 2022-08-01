Create Database PortalDeFestas;

Create Table Empresa(
    cod_emp int NOT NULL,
    nome_emp varchar(30) not null,
    telefone_emp varchar(11),
    endereco varchar(30),
    primary key (cod_emp)
);

Create Table Cliente(
    cod_cli int not null,
    nome_cli varchar(30) not null,
    cpf_cli varchar(30) not null,
    login_cli varchar(30) not null,
    senha_cli varchar(30) not null,
    telefone_cli varchar(11),
    endereco varchar(30),
    primary key (cod_cli)
);

Create Table Festa(
    cod_fes int not null,
    preco_fes int not null,
    tipo_fes varchar(30) not null,
    nome_fes varchar(30) not null,
    duracao_fes int,
    Extra_fes varchar(30),
    primary key (cod_fes)
);

Create Table Funcionario(
    cod_fun int not null,
    nome_fun varchar(30) not null,
    telefone_fun varchar(11),
    endereco_fun varchar(30),
    empresa_fun varchar(30),
    equip_fun varchar(30),
    primary key (cod_fun)
);

Create Table Extra(
    cod_ext int not null,
    preco_ext int not null,
    hora_ext,
    tipo_ext,
    primary key (cod_ext)
);

Create Table Historico(
    cod_hist int not null,
    cod_emp int not null,
    cod_fes int not null,
    cod_cli int not null,
    avaliacao_hist varchar(30) not null,
    foreign key (cod_emp, cod_fes, cod_cli),
    primary key (cod_hist, cod_emp, cod_fes, cod_cli)
);