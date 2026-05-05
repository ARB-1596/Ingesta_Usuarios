import boto3
import pandas as pd
import requests

URL_usuarios = "http://IP_PRIVADA:PUERTO/usuarios"

response = requests.get(URL_vuelos)
data = response.json()

df = pd.DataFrame(data)
df.to_csv("usuarios.csv", index=False)

ficheroUpload = "ingesta/usuarios/usuarios.csv"
nombreBucket = "tickets-aereo"

s3 = boto3.client('s3')
response = s3.upload_file("usuarios.csv",nombreBucket, ficheroUpload)
print(response)
