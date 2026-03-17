from No import No

class Lista: 
    
    def __init__(self):
        self.inicio = None

    def add(self, valor):
        nodo = No(valor)
        
        # Caso 1: Lista vazia
        if self.inicio is None:
            self.inicio = nodo
        
        else:
            # Caso 2: Inserção no início (O novo valor é menor que o atual início)
            if nodo.dado < self.inicio.dado:
                nodo.prox = self.inicio
                self.inicio = nodo
            
            else:
                # Caso 3: Inserção no meio ou no fim
                ant = self.inicio
                aux = self.inicio.prox
                
                inseriu = False
                while aux: 
                    if nodo.dado < aux.dado:
                        nodo.prox = aux
                        ant.prox = nodo
                        inseriu = True
                        break
                    else:
                        ant = aux
                        aux = aux.prox
                
                # Caso 4: Se percorreu tudo e não inseriu, ele vai para o fim
                if not inseriu:
                    ant.prox = nodo
        
        # Mensagem de confirmação solicitada:
        print(f"+++ Elemento '{valor}' adicionado à lista +++")
        self.imprimir()

    def imprimir(self):
        print("-" * 10)
        print("Lista Encadeada:")
        if self.inicio is None: 
            print("Lista vazia")
            return
        
        aux = self.inicio
        while aux:
            print(f"-> {aux.dado}")
            aux = aux.prox
        print("-" * 10)

    def remover(self, valor):
            removeu = False 
            
            if self.inicio is None:
                print("Lista vazia")
            else:
                # Caso 1: Remover o primeiro elemento
                if valor == self.inicio.dado:
                    self.inicio = self.inicio.prox
                    removeu = True
                else:
                    # Caso 2: Procurar no restante da lista
                    ant = self.inicio
                    aux = self.inicio.prox
                    
                    while aux:
                        if valor == aux.dado:
                            ant.prox = aux.prox
                            removeu = True
                            break 
                        else:
                            ant = aux
                            aux = aux.prox
                
                if removeu:
                    print(f"--- Elemento {valor} removido! ---")
                else:
                    print(f"--- {valor} não encontrado ---")
                
                self.imprimir()