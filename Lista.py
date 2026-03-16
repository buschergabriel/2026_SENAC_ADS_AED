from No import No

class Lista: # Por convenção, usamos inicial maiúscula para classes
    
    def __init__(self):
        self.inicio = None

    def add(self, valor):
        nodo = No(valor)
        
        # Caso 1: Lista vazia
        if self.inicio is None:
            self.inicio = nodo
        
        else:
            # Caso 2: Inserção no início (O erro estava aqui: compare com self.inicio.dado)
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