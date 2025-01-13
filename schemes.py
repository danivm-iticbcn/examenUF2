from exercici1 import Formulari


def formulari_schema(formulari: Formulari) -> dict:
    # Jo crec que la contrasenya i direccio no haurien de estar per que son dades molt sensibles
    return {"nombre": formulari.nombre,
            "apellido" : formulari.apellido,
            "password" : formulari.password,
            "email": formulari.correo,
            "direcion": formulari.direccion,
            "cp": formulari.cp,
            "age": formulari.ano}
