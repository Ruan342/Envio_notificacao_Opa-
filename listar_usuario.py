import requests
import json
from dotenv import load_dotenv
import os

url = os.getenv("Url_user")
token=os.getenv("Token")
def ext_id_usr(usuario):
  payload=json.dumps ({
        "filter": {
            "nome":f"{usuario}"
        }
    })
  headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
  response = requests.request("GET", url, headers=headers, data=payload)

  if response.status_code == 200:
        retorno_dados = response.json()
        if retorno_dados.get("status") == "success" and retorno_dados.get("data"):
            id=retorno_dados["data"][0].get("_id")
            #print(f"O id desse usuario é: {id}")
            return id 
