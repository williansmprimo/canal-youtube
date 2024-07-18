import random

# Definição da classe para o nó da fila
class Node:
    def __init__(self, nome, senha, prioridade):
        self.nome = nome
        self.senha = senha
        self.prioridade = prioridade
        self.proximo = None

# Definição da classe para a fila
class FilaComPrioridade:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.fim_prioridade = None
        self.qtd_prioridades = 0

    # Método para verificar se a fila está vazia
    def esta_vazia(self):
        return self.inicio is None

    # Método para inserir uma pessoa na fila
    def inserir(self, nome, prioridade):
        senha = random.randint(1000, 9999)  # Gera uma senha aleatória de 4 dígitos
        novo_no = Node(nome, senha, prioridade)

        if self.esta_vazia():
            self.inicio = novo_no
            self.fim = novo_no
            
            #isso é importante para tratar um caso de borda
            if prioridade:
                self.fim_prioridade = novo_no
        else:
            # Verifica se a pessoa tem prioridade ou não
            if prioridade:
                temp = self.fim_prioridade #Pega o ultimo nó com prioridade
                self.fim_prioridade = novo_no

            	#Caso o bloco chegue no limite pula 2, ou 1 caso só tenha mais um na fila
                if self.qtd_prioridades == 2:
                    # Se o tamanho do bloco fosse maior poderiamos for
                    if temp.proximo:
                        temp = temp.proximo # pula 1
                    if temp.proximo:
                        temp = temp.proximo # pula 2
                        
                if temp is None:
                    novo_no.proximo = self.inicio
                    self.inicio = novo_no
                else:
                    novo_no.proximo = temp.proximo
                    temp.proximo = novo_no

                # Caso de borda
                if novo_no.proximo is None:
                    self.fim = novo_no
                
                if self.qtd_prioridades >= 2 and temp.prioridade:
                		self.qtd_prioridades = 2
                else:
                		self.qtd_prioridades = (self.qtd_prioridades % 2) + 1
            else:
            	# Quando é sem prioridade, simplesmente adiciona
                self.fim.proximo = novo_no
                self.fim = novo_no

    # Método para remover a próxima pessoa da fila
    def remover(self):
        if self.esta_vazia():
            return None
        else:
            pessoa_atendida = self.inicio
            
            # Caso de borda
            if pessoa_atendida == self.fim_prioridade:
                self.fim_prioridade = None
                self.qtd_prioridades = 0
            	
            self.inicio = self.inicio.proximo
            if not self.inicio:
                self.fim = None
            return pessoa_atendida

    # Método para imprimir a fila (para fins de depuração)
    def imprimir_fila(self):
        temp = self.inicio
        while temp:
            print(f"Nome: {temp.nome}, Senha: {temp.senha}, Prioridade: {temp.prioridade}")
            temp = temp.proximo
        print()

# Exemplo de utilização do sistema
fila = FilaComPrioridade()

# Menu interativo
while True:
    print("Menu")
    print("1 - Inserir")
    print("2 - Imprimir fila")
    print("3 - Remover")
    print("4 - Sair")
    
    opcao = input("Digite a opção: ")
    
    if opcao == '1':
        nome = input("Digite o nome: ")
        prioridade = input("Possui prioridade? (S/N): ").upper() == 'S'
        fila.inserir(nome, prioridade)
    elif opcao == '2':
        print("Fila atual:")
        fila.imprimir_fila()
    elif opcao == '3':
        pessoa = fila.remover()
        if pessoa:
            print(f"Próxima pessoa a ser atendida: {pessoa.nome}, senha: {pessoa.senha}")
        else:
            print("Fila vazia.")
    elif opcao == '4':
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")
