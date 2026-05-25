from fastapi import FastAPI
from pydantic import BaseModel
import time

app = FastAPI()

dados = [{"id": i, "nome": f"item{i}"} for i in range(50000)]

class Recurso(BaseModel):
    nome: str

@app.get("/api/status")
def status():
    return {"status": "ok"}

@app.get("/api/recurso-detalhe/{id}")
def detalhe(id: int):
    for item in dados:
        if item["id"] == id:
            return item
    return {}



cache = [item for item in dados if item["id"] % 100 == 0]

@app.get("/api/recurso-lento")
def lento():
    return cache[:50]

'''
@app.get("/api/recurso-lento")
def lento():
    resultado = []

    for i in range(len(dados)):
        if dados[i]["id"] % 100 == 0:
            resultado.append(dados[i])

    time.sleep(0.2)

    return resultado[:50]
'''


@app.post("/api/recurso")
def criar(recurso: Recurso):
    novo = {"id": len(dados)+1, "nome": recurso.nome}
    dados.append(novo)
    return novo
