from exercici1 import Formulari

def usuari_schema(usuari) -> dict:
    # Jo crec que la contrasenya i direccio no haurien de estar per que son dades molt sensibles
    return {"nombre": usuari[0],
            "apellido" : usuari[1],
            "correo" : usuari[2],
            "descripcion": usuari[3],
            "curso": usuari[4],
            "ano": usuari[5],
            "direccion": usuari[6],
            "cp": usuari[7],
            "password": usuari[8]
            }


def usuaris_schema(usuaris) -> dict:
    return [usuari_schema(usuari) for usuari in usuaris]