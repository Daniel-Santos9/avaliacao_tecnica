class Funcionario:

    # O atributo nivel conterá a informação se o funcionário será atendente, gerente ou diretor
    # O atributo status conterá a informação se o funcionário estará disponível ou não. 
    # Caso status seja igual a True o funcionário estará disponível, caso seja False o funcionário não estará disponível

    def __init__(self, cpf=None,nome=None, nivel=None, status=None):
        self.cpf = cpf
        self.nome = nome
        self.nivel = nivel
        self.status = status

    def add_func(self, func):
        
        func_all = []
        for f in func:
            func = Funcionario()
            func.cpf = f[0]
            func.nome = f[1]
            func.nivel = f[2] 
            func.status = f[3]   
            func_all.append(func)

        return func_all


    def dispatchCall(self, func):

        flag = 0

        for f in func:

            if f.nivel.lower() == "atendente" and f.status == True:
                return "O(a) atendente " + f.nome + " está disponível"
            
            elif f.nivel.lower() == "gerente" and f.status == True:
                return "O(a) gerente " + f.nome + " está disponível" 
            
            elif f.nivel.lower() == "diretor" and f.status == True:
                return "O(a) diretor(a) " + f.nome + " está disponível"
            else:
               flag += 1

        if flag == len(func):
             return "Não possui funcionário disponível no momento. Por favor, aguarde."


funcionario1 = ["000.000.000-0", "Daniel", "atendente", False]
funcionario2 = ["111.111.111-1", "Evilasio", "gerente", False]
funcionario3 = ["222.222.222-2", "Bruno", "diretor", True]

func = [funcionario1, funcionario2, funcionario3]

funcionario = Funcionario()
func_all = funcionario.add_func(func)
infor = funcionario.dispatchCall(func_all)

print(infor)

        

