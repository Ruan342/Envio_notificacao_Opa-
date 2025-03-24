import requests
import json
from dotenv import load_dotenv
import os

url = os.getenv("Url_notificacao")
token=os.getenv("Token")
def enviar_notificaçao(nome, descriçao, user_id, link=""):
  payload = json.dumps({
    "users":[user_id],
    "type": "news",
    "title": f"{nome}",
    "description": f"{descriçao}",
    "link": f"{link}"
  })
  headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'
  }

  response = requests.request("POST", url, headers=headers, data=payload)

  print(response.text)
