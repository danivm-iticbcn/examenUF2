from fastapi import FastAPI

import connection
from accesData import add_user
from exercici1 import Formulari

app = FastAPI()
conn = connection.createConection()
print(conn)

@app.post("/grabar/{formulari}")
async def grabarFormulari(formulari: Formulari):
    resultat = add_user.add_user(conn, formulari)
    return resultat
