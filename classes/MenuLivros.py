from classes.LivroDAO import LivroDAO
class MenuLivros:
    def __init__(self):
        self.dao = LivroDAO()
    
    def exibir_menu(self):
        print("---MENU---")
        print("1. Listar os Livros")
        print("2. Buscar os Livro")
        print("3. Inserir  Livro")
        print("4. Atualizar os Livro")
        print("5. Excluir  Livro")
        print("0. Sair do programa")
    
    def listar(self):
        livros = self.dao.listar()
        if livros:
            print("Livros:")
            for livro in livros:
                print(f"Código: {livro[0]}, Nome: {livro[1]}, Ano:{livro[2]}, Data/Hora do Cadatro: {livro[3]}")
        else:
            print("Nnehum livro encontrado")
    
    def buscar(self):
        codLivro = input("Digite o código do livro que deseja buscar: ")
        livro = self.dao.buscar(codLivro)
        if livro:
           print(f"Código: {livro[0]}, Nome: {livro[1]}, Ano:{livro[2]}, Data/Hora do Cadatro: {livro[3]}")
        else:
            print("Livro não encontrado")
    
    def inserir(self):
        nomeLivro = input("Digite o nome do livro: ")
        anoLivro = input("Digite o ano do livro: ")
        self.dao.inserir(nomeLivro, anoLivro)
        print("Livro inserido com sucesso")
    
    def atualizar(self):
        codLivro = input("Digite o código do livro que deseja atualizar: ")
        nomeLivro = input("Digite o novo nome do livro: ")
        anoLivro = input("Digite o novo ano do livro: ")
        self.dao.atualizar(codLivro, nomeLivro, anoLivro)
        print("Livro atualizado com sucesso.")
    
    def excluir_livro(self):
        codLivro = input("Digite o código do livro que deseja excluir: ")
        self.dao.delete(codLivro)
        print("Livro excluído com sucesso.")
        
    
    def executar(self):
        while True:
            self.exibir_menu()
            opcao = input("Digite a opção desejada: ")
            if opcao == "1":
                self.listar()
            elif opcao == "2":
                self.buscar()
            elif opcao == "3":
                self.inserir()
            elif opcao == "4":
                self.atualizar()
            elif opcao == "5":
                self.excluir_livro
            elif opcao == "0":
                print("Encerrando o programa")
                print("Obrigado por usa-lo")
                break
            else:
                print("Opção inválida. Digite novamente.")