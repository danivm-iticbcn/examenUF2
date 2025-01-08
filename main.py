from fastapi import FastAPI
import connection

app = FastAPI()
conn = connection.createConection()
print(conn)