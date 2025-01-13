from fastapi import FastAPI

import connection
from exercici1 import Formulari

app = FastAPI()
conn = connection.createConection()
print(conn)

def usuari3_schema(usuari: Formulari) -> dict:
    # Jo crec que la contrasenya i direccio no haurien de estar per que son dades molt sensibles
    return {"nombre": usuari.nombre,
            "apellido" : usuari.apellido,
            "password" : usuari.password,
            "email": usuari.correo,
            "direcion": usuari.direccion,
            "cp": usuari.correo,
            "age": usuari.ano}