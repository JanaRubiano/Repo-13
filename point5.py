import json
import requests

url1 = 'https://api.genderize.io?name=luc'
url2 = 'https://api.agify.io?name=meelad'
url3 = 'https://api.nationalize.io?name=nathaniel'

def apiInfo(direction:int):
  print(direction)
  peticion = requests.get(direction)
  print(peticion.status_code)
  j = json.loads(peticion.content)
  print(j) 
  return list(j.items())

if __name__ == "__main__":
  respuesta1 = apiInfo(url1)
  print(*respuesta1)
  respuesta2 = apiInfo(url2)
  print(*respuesta2)
  respuesta3 = apiInfo(url3)
  print(*respuesta3)