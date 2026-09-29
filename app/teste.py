lista_api = [
    {"nome_api":"GOOGLE", "url_api":"api_google", "token":"tokengoogle"},
    {"nome_api":"AIRBNB", "url_api":"api_airbnb", "token":"tokenairbnb"},  
      ]

palavra = input("")
for i in lista_api:
    print(palavra in i["nome_api"])

print([palavra in i["nome_api"] for i in lista_api])

