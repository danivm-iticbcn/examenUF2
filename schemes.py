from exercici1 import Formulari


def usuari_schema(usuari) -> dict:
    # Jo crec que la contrasenya i direccio no haurien de estar per que son dades molt sensibles
    return {"nombre": usuari[0],
            "apellido" : usuari[1],
            "password" : usuari[2],
            "email": usuari[3],
            "direcion": usuari[4],
            "cp": usuari[5],
            "age": usuari[6]}


def usuaris_schema(usuaris) -> dict:
    return [usuari_schema(usuari) for usuari in usuaris]