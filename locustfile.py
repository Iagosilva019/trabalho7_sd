from locust import HttpUser, task, between
import random

class ApiUser(HttpUser):
    wait_time = between(1, 2)

    @task(4)
    def lento(self):
        self.client.get("/api/recurso-lento")

    @task(3)
    def detalhe(self):
        x = random.randint(1, 1000)
        self.client.get(f"/api/recurso-detalhe/{x}")

    @task(2)
    def status(self):
        self.client.get("/api/status")

    @task(1)
    def criar(self):
        self.client.post("/api/recurso", json={"nome":"teste"})
