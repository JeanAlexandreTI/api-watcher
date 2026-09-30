
class Teste():
    def __init__(self):
        self.__lista_api = [
        {"nome_api":"AIRBNB", "url_api":"api_airbnb", "token":"tokenairbnb"},  
        {"nome_api":"GOOGLE", "url_api":"api_google", "token":"tokengoogle"},
        {"nome_api":"AIRSOFT", "url_api":"api_airsoft", "token":"tokenairsoft"},
        ]


    def exibe_dados(self):

        palavra = input("Palavra: ").upper().strip()

        print([i for i in self.__lista_api if i["nome_api"].count(palavra)])


    def main(self):
        self.exibe_dados()


if __name__ == "__main__":
    Teste().main()