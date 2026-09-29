# CADASTRAR API: Nome e URL
# LISTAR API: Informar todas as API
import os
import polars as pl
from time import sleep

class ApiWatcher():
    def __init__(self):
        self.__lista_api = []


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


    # def retornar_menu(self):
    #     input("\nSelecione alguma tecla para retornar ao menu: ")
    #     print()
    #     self.selecionar_menu()


    def cadastro(self):
        self.titulo("| CADASTRO |")
        dados = {
            "nome_api": input("Nome: ").upper().strip(),
            "url_api": input("Url: ").strip(),
            "token_api": input("Token: ").strip()
        }

        self.__lista_api.append(dados)
        print(f"\n{dados['nome_api']} cadastrado(a) com sucesso.")

        self.selecionar_menu()


    def listar_api(self):
        nome_procurado = input("Informe o Nome da Api Procurada: ").upper().strip()
        if nome_procurado != "":
            print(pl.DataFrame(self.__lista_api).filter(pl.col("nome_api").str.contains(nome_procurado)))
        else:
            print(pl.DataFrame(self.__lista_api))

        self.selecionar_menu()


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

            except ValueError:
                print("ERRO! Por Favor, Informe um Valor Inteiro.")
                sleep(1)
                print("Redirecionando Para Menu...")
                sleep(3)


    def main(self):
        self.selecionar_menu()


if __name__ == "__main__":
    ApiWatcher().main()