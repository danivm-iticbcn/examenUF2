from typing import List

from fastapi import FastAPI
from accesData import read

import connection
import schemes
from exercici1 import Formulari

app = FastAPI()
conn = connection.createConection()
print(conn)

@app.get("/users", response_model=List[dict])
async def rebreUsuaris():
    usuaris = read.read_all(connection)
    return schemes.usuaris_schema(usuaris)