from fastapi import FastAPI
from pydantic import BaseModel

import connection
import schemes

app = FastAPI()
conn = connection.createConection()
print(conn)

class Formulari(BaseModel):
    nombre: str
    apellido: str
    correo: str
    descripcion: str | None = None
    curso: str
    ano: int
    direccion: str
    cp: int | None = None
    password: str

@app.post("/grabarForm")
async def grabarFormulari(formulari: Formulari):
    return schemes.formularis_schema(formulari)