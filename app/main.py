import os
from time import sleep

class ApiWatcher():
    def __init__(self):
        self.__lista_api = [{"nome_api":"GOOGLE", "url_api":"api_google", "token":"tokengoogle"}]


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
        self.limpar_visao()
        sleep(1)

        input("\nSelecione Alguma Tecla Para Retornar ao Menu: ")
        
        print("Redirecionando Para Menu...")
        sleep(2)


    def cadastro(self):
        self.titulo("| CADASTRO |")
        dados = {
            "nome_api": input("Nome: ").upper().strip(),
            "url_api": input("Url: ").strip(),
            "token_api": input("Token: ").strip()
        }

        self.__lista_api.append(dados)
        print(f"\n{dados['nome_api']} cadastrado(a) com sucesso.")

        self.pausa_redireciona_menu()


    def listar_api(self):
        nome_procurado = input("Informe o Nome da Api Procurada: ").upper().strip()

        if [i for i in self.__lista_api if i["nome_api"] == nome_procurado] == []:
            print("\nNome Procurado Inexistente.")
        else:
            print([i for i in self.__lista_api if i["nome_api"] == nome_procurado])
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