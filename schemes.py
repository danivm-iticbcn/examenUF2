def formulari_schema(formulari) -> dict:
    return {"nombre": formulari[0],
            "apellido" : formulari[1],
            "correo" : formulari[2],
            "descripcion": formulari[3],
            "curso": formulari[4],
            "ano": formulari[5],
            "direccion": formulari[6],
            "cp": formulari[7],
            "password": formulari[8]}


def formularis_schema(formularis) -> dict:
    return [formulari_schema(formulari) for formulari in formularis]