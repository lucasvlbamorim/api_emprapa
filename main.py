from fastapi import FastAPI, HTTPException
import requests
from bs4 import BeautifulSoup
import json
app = FastAPI()

@app.get("/producao/{ano}")
def consultarProducao(ano: int = 2023):
    url = f"http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_02&ano={ano}"
    response = requests.get(url)
    if(response.status_code == 200):
        soup = BeautifulSoup(response.text, 'html.parser')
        tabela_html = soup.find('table', {'class': 'tb_base tb_dados'})
        if tabela_html:
            resultado_json = {}
            current_item = None

            # Iterando sobre as linhas da tabela
            for linha in tabela_html.find_all('tr'):
                celulas = linha.find_all('td')
                if len(celulas) == 2:
                    # Verifica a classe para classificar como 'tb_item' ou 'tb_subitem'
                    classe_celula = celulas[0].get("class", [None])[0]
                    if classe_celula == 'tb_item':
                        # Novo item principal
                        current_item = celulas[0].text.strip()
                        resultado_json[current_item] = {}
                        quantidade = celulas[1].text.strip()
                        resultado_json[current_item]["total"] = quantidade
                        
                    elif classe_celula == 'tb_subitem' and current_item:
                        # Subitem do item atual
                        subitem_nome = celulas[0].text.strip()
                        subitem_quantidade = celulas[1].text.strip()
                        resultado_json[current_item][subitem_nome] = subitem_quantidade

            # Convertendo o resultado para JSON
            resultado_json_str = json.dumps(resultado_json, ensure_ascii=False, indent=2)

            print(resultado_json_str)
            return resultado_json_str
        else:
            return {"error":"Erro no servidor, por favor tentar novamente mais tarde"}
    else:    
        return {"message": response.status_code}
    

@app.get("/processamento/{tipo}/{ano}")
def consultarProducao(ano: int = 2023,tipo: int = 1):
    url = f"http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_03&subopcao=subopt_0{tipo}&ano={ano}"
    response = requests.get(url)
    if(response.status_code == 200):
        soup = BeautifulSoup(response.text, 'html.parser')
        tabela_html = soup.find('table', {'class': 'tb_base tb_dados'})
        if tabela_html:
            resultado_json = {}
            current_item = None

            # Iterando sobre as linhas da tabela
            for linha in tabela_html.find_all('tr'):
                celulas = linha.find_all('td')
                if len(celulas) == 2:
                    # Verifica a classe para classificar como 'tb_item' ou 'tb_subitem'
                    classe_celula = celulas[0].get("class", [None])[0]
                    if classe_celula == 'tb_item':
                        # Novo item principal
                        current_item = celulas[0].text.strip()
                        resultado_json[current_item] = {}
                        quantidade = celulas[1].text.strip()
                        resultado_json[current_item]["total"] = quantidade
                        
                    elif classe_celula == 'tb_subitem' and current_item:
                        # Subitem do item atual
                        subitem_nome = celulas[0].text.strip()
                        subitem_quantidade = celulas[1].text.strip()
                        resultado_json[current_item][subitem_nome] = subitem_quantidade

            # Convertendo o resultado para JSON
            resultado_json_str = json.dumps(resultado_json, ensure_ascii=False, indent=2)

            print(resultado_json_str)
            return resultado_json_str
        else:
            return {"error":"Erro no servidor, por favor tentar novamente mais tarde"}
    else:    
        return {"message": response.status_code}

@app.get("/comercializacao/{ano}")
def consultarProducao(ano: int = 2023):
    url = f"http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_04&ano={ano}"
    response = requests.get(url)
    if(response.status_code == 200):
        soup = BeautifulSoup(response.text, 'html.parser')
        tabela_html = soup.find('table', {'class': 'tb_base tb_dados'})
        if tabela_html:
            resultado_json = {}
            current_item = None

            # Iterando sobre as linhas da tabela
            for linha in tabela_html.find_all('tr'):
                celulas = linha.find_all('td')
                if len(celulas) == 2:
                    # Verifica a classe para classificar como 'tb_item' ou 'tb_subitem'
                    classe_celula = celulas[0].get("class", [None])[0]
                    if classe_celula == 'tb_item':
                        # Novo item principal
                        current_item = celulas[0].text.strip()
                        resultado_json[current_item] = {}
                        quantidade = celulas[1].text.strip()
                        resultado_json[current_item]["total"] = quantidade
                        
                    elif classe_celula == 'tb_subitem' and current_item:
                        # Subitem do item atual
                        subitem_nome = celulas[0].text.strip()
                        subitem_quantidade = celulas[1].text.strip()
                        resultado_json[current_item][subitem_nome] = subitem_quantidade

            # Convertendo o resultado para JSON
            resultado_json_str = json.dumps(resultado_json, ensure_ascii=False, indent=2)

            print(resultado_json_str)
            return resultado_json_str
        else:
            return {"error":"Erro no servidor, por favor tentar novamente mais tarde"}
    else:    
        return {"message": response.status_code}


@app.get("/importacao/{tipo}/{ano}")
def consultarProducao(ano: int = 2023,tipo: int = 1):
    url = f"http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_05&subopcao=subopt_0{tipo}&ano={ano}"
    response = requests.get(url)
    if(response.status_code == 200):
        soup = BeautifulSoup(response.text, 'html.parser')
        tabela_html = soup.find('table', {'class': 'tb_base tb_dados'})
        if tabela_html:
            resultado_json = {}
            # Iterando sobre as linhas da tabela
            for linha in tabela_html.find_all('tr'):
                celulas = linha.find_all('td')
                if len(celulas) == 3:
                    resultado_json[celulas[0].text.strip()] = {}
                    resultado_json[celulas[0].text.strip()]['KG'] = celulas[1].text.strip()
                    resultado_json[str(celulas[0].text.strip())]['valor'] = celulas[2].text.strip()
            # Convertendo o resultado para JSON
            resultado_json_str = json.dumps(resultado_json, ensure_ascii=False, indent=2)

            return resultado_json_str
        else:
            return {"error":"Erro no servidor, por favor tentar novamente mais tarde"}
    else:    
        return {"message": response.status_code}
    


@app.get("/exportacao/{tipo}/{ano}")
def consultarProducao(ano: int = 2023,tipo: int = 1):
    url = f"http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_06&subopcao=subopt_0{tipo}&ano={ano}"
    response = requests.get(url)
    if(response.status_code == 200):
        soup = BeautifulSoup(response.text, 'html.parser')
        tabela_html = soup.find('table', {'class': 'tb_base tb_dados'})
        if tabela_html:
            resultado_json = {}
            # Iterando sobre as linhas da tabela
            for linha in tabela_html.find_all('tr'):
                celulas = linha.find_all('td')
                if len(celulas) == 3:
                    resultado_json[celulas[0].text.strip()] = {}
                    resultado_json[celulas[0].text.strip()]['KG'] = celulas[1].text.strip()
                    resultado_json[str(celulas[0].text.strip())]['valor'] = celulas[2].text.strip()
            # Convertendo o resultado para JSON
            resultado_json_str = json.dumps(resultado_json, ensure_ascii=False, indent=2)

            return resultado_json_str
        else:
            return {"error":"Erro no servidor, por favor tentar novamente mais tarde"}
    else:    
        return {"message": response.status_code}