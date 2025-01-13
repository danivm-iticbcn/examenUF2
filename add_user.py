from matplotlib.backend_tools import cursors

from exercici1 import Formulari


def add_user(connection, formulari: Formulari):
    conn = connection
    cursor = conn.cursor()

    try:
        query = f"INSERT INTO users VALUES('{formulari.nombre}', '{formulari.apellido}', '{formulari.password}', '{formulari.correo}', '{formulari.curso}', {formulari.cp}, '{formulari.direccion}', '{formulari.descripcion}', {formulari.ano}' "
        cursor.execute(query)
        conn.commit()
        conn.close()
        return "Correcte"
    except:
        conn.rollback()
        cursor.close()
        return "Incorrecte"

