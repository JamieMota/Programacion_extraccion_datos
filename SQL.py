from mysql.connector import connect, Error

try:
    dbconexion=connect(host="localhost", user="root",
                        password="12345",database="olimpiadas")
    cursor=dbconexion.cursor()
    #sql= "INSERT INTO GENERO(nombre) VALUES (%s)"
    #sql= "UPDATE GENERO SET NOMBRE = %s WHERE ID= %s"
    sql="Select * from Genero"
    valores=[("FEMENINO",12), ("Maculino",)]













    """""
    cursor.executemany(sql,valores[0])
    lista_datos = cursor.fetchall()
    for item in lista_datos:
        print(item)
    """

    #cursor.execute(sql)
    #dbconexion.commit()
    print(cursor.lastrowid)
    """""
    sql = "show databases"
    cursor.execute(sql)
    lista_datos= cursor.fetchall()
    for item in lista_datos:
        print(item)
    """
except Error as e:
    print(e)