import mysql.connector
# ================
# CONEXIÓN A MYSQL
# ================
def f_conectar():
    conexion = mysql.connector.connect(
        host="localhost",
        user="rootuser",
        password="rootpass",
        database="comercio"
    )
    return conexion

# ===============
# AGREGAR CLIENTE
# ===============
def f_agregar_registro(
    nombre,
    apellido_paterno,
    apellido_materno,
    fecha_nacimiento,
    genero,
    correo,
    telefono,
    estado,
    ciudad,
    codigo_postal,
    tipo_cliente,
    intereses,
    limite_credito,
    observaciones
):
    conexion = f_conectar()
    cursor = conexion.cursor()

    sql="""
    CREATE TABLE clientes (
id_cliente INT AUTO_INCREMENT PRIMARY KEY,
nombre VARCHAR(50) NOT NULL,
apellido_paterno VARCHAR(50) NOT NULL,
apellido_materno VARCHAR(50),
fecha_nacimiento DATE,
genero VARCHAR(15),
correo VARCHAR(100) NOT NULL,
telefono VARCHAR(20),
estado VARCHAR(50),
ciudad VARCHAR(50),
codigo_postal VARCHAR(10),
tipo_cliente VARCHAR(20),
intereses VARCHAR(200),
limite_credito DECIMAL(10,2),
observaciones VARCHAR(250)
);
    """
    cursor.execute(sql)
    conexion.commit()
    
    sql = """
        INSERT INTO clientes
        (
            nombre,
            apellido_paterno,
            apellido_materno,
            fecha_nacimiento,
            genero,
            correo,
            telefono,
            estado,
            ciudad,
            codigo_postal,
            tipo_cliente,
            intereses,
            limite_credito,
            observaciones
        )
        VALUES
        (
            %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s, %s
        )
    """
    valores = (
        nombre,
        apellido_paterno,
        apellido_materno,
        fecha_nacimiento,
        genero,
        correo,
        telefono,
        estado,
        ciudad,
        codigo_postal,
        tipo_cliente,
        intereses,
        limite_credito,
        observaciones
    )

    cursor.execute(sql, valores)
    conexion.commit()
    cursor.close()
    conexion.close()

# ===============
# LISTAR CLIENTES
# ===============
def f_listar_clientes():

    conexion = f_conectar()

    cursor = conexion.cursor()

    sql = """
        SELECT
            id_cliente,
            nombre,
            apellido_paterno,
            apellido_materno,
            fecha_nacimiento,
            genero,
            correo,
            telefono,
            estado,
            ciudad,
            codigo_postal,
            tipo_cliente,
            intereses,
            limite_credito,
            observaciones
        FROM clientes
        ORDER BY id_cliente
    """
    cursor.execute(sql)

    clientes = cursor.fetchall()
    cursor.close()
    conexion.close()
    return clientes
