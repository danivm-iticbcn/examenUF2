from typing import List

from fastapi import FastAPI

import connection
import schemes
from exercici1 import Formulari

app = FastAPI()
conn = connection.createConection()
print(conn)

@app.get("/user", response_model=List[dict])
async def mostrarFormulari(formulari: Formulari):
    return schemes.usuari3_schema(formulari)