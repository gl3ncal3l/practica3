GO
CREATE DATABASE practica3;
GO
USE practica3;
GO
CREATE TABLE usuario(
	codigoUsuario INTEGER,
	nombre VARCHAR(200),
	userName VARCHAR(50),
	correo VARCHAR(128),
	contrasenia VARCHAR(128),
	CONSTRAINT usuario_pk PRIMARY KEY ( codigoUsuario )
);
GO
CREATE TABLE cuenta(
	codigoCuenta INTEGER,
	codigoUsuario INTEGER,
	cantidad DECIMAL(10,2),
	CONSTRAINT cuenta_pk PRIMARY KEY ( codigoCuenta ),
	CONSTRAINT cu_fk FOREIGN KEY ( codigoUsuario ) REFERENCES usuario ( codigoUsuario ) ON DELETE CASCADE
);
GO
CREATE TABLE tipo(
	codTipo INTEGER IDENTITY(1,1),
	descripcion VARCHAR(128),
	CONSTRAINT tipo_pk PRIMARY KEY ( codTipo ),
);
GO
CREATE TABLE transaccion(
	codigoCuenta INTEGER,
	fecha DATE,
	monto DECIMAL(10,2),
	descripcion VARCHAR(128),
	codTipo INTEGER,
	CONSTRAINT transaccion_pk PRIMARY KEY ( codigoCuenta, fecha, monto, codTipo ),
	CONSTRAINT tc_fk FOREIGN KEY ( codigoCuenta ) REFERENCES cuenta ( codigoCuenta ) ON DELETE CASCADE,
	CONSTRAINT tt_fk FOREIGN KEY ( codTipo ) REFERENCES tipo ( codTipo ) ON DELETE CASCADE
);
GO
CREATE TABLE transferencia(
	codigoCuentaOrigen INTEGER,
	codigoCuentaDestino INTEGER,
	fecha DATE,
	monto DECIMAL(10,2),
	CONSTRAINT transferencia_pk PRIMARY KEY ( codigoCuentaOrigen, codigoCuentaDestino, fecha ),
	CONSTRAINT tc1_fk FOREIGN KEY ( codigoCuentaOrigen ) REFERENCES cuenta ( codigoCuenta ) ON DELETE CASCADE ON UPDATE CASCADE,
	CONSTRAINT tc2_fk FOREIGN KEY ( codigoCuentaDestino ) REFERENCES cuenta ( codigoCuenta )
);

INSERT INTO tipo
VALUES ('Crédito');

INSERT INTO tipo
VALUES ('Débito');

INSERT INTO usuario
VALUES(1000,'Carlos Peralta', 'CPeralta2019', 'carloperalta@gmail.com', 'C@rl0sP3ralta');

INSERT INTO cuenta
VALUES(10000,1000,1000);
