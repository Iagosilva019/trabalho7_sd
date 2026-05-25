# Benchmark e Otimização de API REST

## Sobre o Projeto

Este projeto apresenta a análise de desempenho e otimização de uma API REST utilizando testes de carga e benchmark.

O objetivo principal foi identificar e otimizar um endpoint crítico responsável pelo principal gargalo da aplicação.

---

# Cenário da Aplicação

A aplicação possui os seguintes endpoints:

| Endpoint                        | Descrição                          | Percentual de Acessos |
| ------------------------------- | ---------------------------------- | --------------------- |
| `GET /api/recurso-lento`        | Endpoint com gargalo de desempenho | 40%                   |
| `GET /api/recurso-detalhe/{id}` | Consulta simples indexada          | 30%                   |
| `GET /api/status`               | Healthcheck da aplicação           | 20%                   |
| `POST /api/recurso`             | Cadastro de novos dados            | 10%                   |

O foco principal da análise foi o endpoint:

```bash
GET /api/recurso-lento
```

---

# Objetivos

* Realizar testes de carga na API;
* Identificar gargalos de desempenho;
* Comparar métricas antes e após otimizações;
* Avaliar latência, throughput e estabilidade;
* Produzir relatórios de benchmark.

---

# Tecnologias Utilizadas

* Python
* FastAPI / Flask (dependendo da implementação)
* Locust
* CSV Reports
* LaTeX (Overleaf)

---

# Estrutura dos Testes

Os testes foram executados simulando múltiplos acessos simultâneos aos endpoints da API.

Métricas analisadas:

* Tempo médio de resposta;
* Percentis de latência;
* Throughput;
* Número de erros;
* Estabilidade sob carga.

---

# Resultados Antes da Otimização

## Endpoint Crítico

| Métrica     | Valor      |
| ----------- | ---------- |
| Tempo médio | ~220 ms    |
| Throughput  | ~597 req/s |
| Erros       | 0          |

O endpoint apresentava alta latência e impactava diretamente a média geral da aplicação.

---

# Resultados Após a Otimização

## Endpoint Crítico

| Métrica     | Valor      |
| ----------- | ---------- |
| Tempo médio | ~5 ms      |
| Throughput  | ~626 req/s |
| Erros       | 0          |

---

# Comparação

| Métrica        |     Antes |    Depois |
| -------------- | --------: | --------: |
| Latência média |    220 ms |      5 ms |
| Throughput     | 597 req/s | 626 req/s |
| Erros          |         0 |         0 |

---

# Ganho de Desempenho

A redução percentual da latência foi de aproximadamente:

```math
((220 - 5) / 220) * 100 ≈ 97.7%
```

---

# Principais Melhorias Implementadas

As otimizações aplicadas removeram o principal gargalo da aplicação.

Possíveis melhorias realizadas:

* Redução de operações bloqueantes;
* Otimização de consultas;
* Uso de cache;
* Redução de I/O desnecessário;
* Melhor gerenciamento de processamento.

---

# Relatório Completo

O relatório completo em LaTeX/Overleaf contém:

* Tabelas detalhadas;
* Gráficos comparativos;
* Análise estatística;
* Resultados dos benchmarks.

---

# Resultados

Os resultados demonstraram:

* Redução significativa da latência;
* Maior estabilidade;
* Melhor desempenho geral da API;
* Remoção efetiva do gargalo principal.

---

## Como Executar

### 1. Clonar o repositório

```bash
git clone https://github.com/Iagosilva019/trabalho7_sd
cd trabalho7_sd/
```
### 2. Instale as dependências
```bash
pip install -r requirements.txt
```

### 3. Executar a aplicação

A API deve ser iniciada escutando em `0.0.0.0` para permitir acesso externo e integração correta com o Locust.

```bash
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

A aplicação ficará disponível em:

```text
http://0.0.0.0:8000
```

---

### 4. Executar o Locust

Inicie o Locust também utilizando `0.0.0.0`:

```bash
locust -f locustfile.py --host http://0.0.0.0:8000
```

Interface web do Locust:

```text
http://0.0.0.0:8089
```

