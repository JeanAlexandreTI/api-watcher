import os
from time import sleep

class ApiWatcher():
    def __init__(self):
        self.__lista_de_api = [
            {"nome_api":"AIRBNB", "url_api":"api_airbnb", "token":"tokenairbnb"},  
            {"nome_api":"GOOGLE", "url_api":"api_google", "token":"tokengoogle"},
            {"nome_api":"AIRSOFT", "url_api":"api_airsoft", "token":"tokenairsoft"},
            ]


    def menu(self):
        print("""
        [1] - CADASTRAR API
        [2] - LISTAR APIs
        [3] - SAIR
        """)


    def limpar_visao(self):
        os.system("cls" if os.name != "posix" else "clear")


    def titulo(self, texto):
        self.limpar_visao()
        print(texto,"\n")


    def pausa_redireciona_menu(self):
        sleep(1)
        input("\nSelecione Alguma Tecla Para Retornar ao Menu: ")
        self.limpar_visao()
        
        print("Redirecionando Para Menu...")
        sleep(2)


    def cadastro(self):
        self.titulo("| CADASTRO |")
        dados = {
            "nome_api": input("Nome: ").upper().strip(),
            "url_api": input("Url: ").strip(),
            "token_api": input("Token: ").strip()
        }

        self.__lista_de_api.append(dados)
        print(f"\n{dados['nome_api']} cadastrado(a) com sucesso.")

        self.pausa_redireciona_menu()


    def listar_api(self):
        nome_procurado = input("\nInforme o Nome da Api Procurada ou Tecle Enter Para Listar Diversas: ").upper().strip()
        resultado_busca = [i for i in self.__lista_de_api if nome_procurado in i["nome_api"]]

        if not self.__lista_de_api == False: 
            if nome_procurado == "":
                print("\n", self.__lista_de_api)
            elif resultado_busca == []:
                print("Api Procurada Fora do Catalogo.")
            else:
                print(resultado_busca)
       
        else:
            print("\nNenhuma Api Cadastrada em Sistema.")
       
        self.pausa_redireciona_menu()


    def selecionar_menu(self):
    
        while True:
            try:

                self.titulo("| MENU |")
                self.menu()

                opcao = int(input("Opcao: "))

                if opcao == 1:
                    self.cadastro()
                    
                elif opcao == 2:
                    self.listar_api()
                                   
                elif opcao == 3:
                    self.titulo("Sistema Encerrado.")
                    break

                else:
                    print("Por Favor, Informe um Dos Valores Exibidos no Menu.")
                    self.pausa_redireciona_menu()

            except ValueError:
                print("ERRO! Por Favor, Informe um Valor Inteiro.")
                self.pausa_redireciona_menu()


    def main(self):
        self.selecionar_menu()


if __name__ == "__main__":
    ApiWatcher().main()