import os
from time import sleep

class ApiWatcher():
    def __init__(self):
        self.__lista_de_api = [
            {"nome_api":"AIRBNB", "url_api":"api_airbnb"},  
            {"nome_api":"GOOGLE", "url_api":"api_google"},
            {"nome_api":"AIRSOFT", "url_api":"api_airsoft"},
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
        input("\nSelecione Enter Para Retornar ao Menu: ")
        self.limpar_visao()
        
        print("Redirecionando Para Menu...")
        sleep(2)


    def cadastro(self):
        self.titulo("| CADASTRO |")

        dados = {
            "nome_api": input("Nome: ").upper().strip(),
            "url_api": input("Url: ").strip(),
        }

        if not dados["nome_api"]:
            print(f"\nCadastrado Com Falta de Nome. Nome Obrigatorio Para Sucesso de Cadastro.")
        elif not dados["url_api"]:
            print("\nCadastro Com Falta de Url. Url Obrigatoria Para Sucesso de Cadastro.")
        else:
            verifica_cadastro_existente = [dados["nome_api"] == i["nome_api"] or dados["url_api"] == i["url_api"] for i in self.__lista_de_api]
            
            if any(verifica_cadastro_existente):
                print("\nNome ou Url de Api Existente. Verifique '[2] - LISTAR APIs'.")
            else:
                self.__lista_de_api.append(dados)
                print(f"\n{dados['nome_api']} cadastrado(a) com sucesso.")

        self.pausa_redireciona_menu()


    def listar_api(self):
        if not self.__lista_de_api:
            print("\nNenhuma Api Cadastrada em Sistema.")
        else:
            nome_procurado = input("\nInforme o Nome da Api Procurada ou Tecle Enter Para Listar Diversas: ").upper().strip()

            if nome_procurado == "":
                print("\n", self.__lista_de_api)
            else:
                resultado_busca = [i for i in self.__lista_de_api if nome_procurado in i["nome_api"]]
                if resultado_busca:
                    print(resultado_busca)
                
                else:
                    print("Api Procurada Fora do Catalogo.")
        
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