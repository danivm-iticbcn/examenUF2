from fastapi import FastAPI

import connection
import schemes
from exercici1 import Formulari

app = FastAPI()
conn = connection.createConection()
print(conn)

@app.get("/user/{formulari}")
async def mostrarFormulari(formulari: Formulari):
    return schemes.formulari_schema(formulari)
