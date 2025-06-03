# 🍇 API Vitivinicultura - Embrapa (Web Scraping + FastAPI)

Este projeto é uma API desenvolvida com **FastAPI** que realiza **web scraping** do site da Embrapa (Vitibrasil), extraindo dados públicos relacionados à produção, processamento, comercialização, importação e exportação de uvas no Brasil. 

---

## 🚀 Funcionalidades

A API fornece os seguintes endpoints:

| Rota                                    | Descrição                                                 |
|-----------------------------------------|------------------------------------------------------------|
| `/producao/{ano}`                       | Retorna os dados de produção de uvas por ano              |
| `/processamento/{tipo}/{ano}`          | Dados de processamento por tipo e ano                     |
| `/comercializacao/{ano}`               | Informações sobre comercialização nacional                |
| `/importacao/{tipo}/{ano}`             | Dados de importação por tipo e ano                        |
| `/exportacao/{tipo}/{ano}`             | Dados de exportação por tipo e ano                        |

> Os dados são extraídos diretamente do portal: http://vitibrasil.cnpuv.embrapa.br

---

## ⚙️ Pré-requisitos

Para executar este projeto localmente, é **obrigatório** ter instalado:

- **[Docker](https://docs.docker.com/get-docker/)** – ferramenta de criação e gerenciamento de containers
- **[Docker Compose](https://docs.docker.com/compose/install/)** – ferramenta para orquestrar múltiplos containers

> Verifique se ambos estão funcionando corretamente com os comandos:

```bash
docker --version
docker-compose --version
---

## 🛠 Como rodar o projeto

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/seu-usuario/sua-api-vitibrasil.git
   cd sua-api-vitibrasil


2. **Execute o comando:**

   ```bash
   docker-compose up --build -d
