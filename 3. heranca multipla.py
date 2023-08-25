class Funcionario:
    def __init__(self, nome):
        self._nome = nome

    def registra_horas(self, horas):
        print('Horas registradas...')

    def mostrar_tarefas(self):
        print('Fez muita coisa...')

class Caelum(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Caelumer')

    def busca_cursos_do_mes(self, mes=None):
        print(f'Mostrando cursos - {mes}' if mes else 'Mostrando cursos desse mês')

class Alura(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Alurete!')

    def busca_perguntas_sem_resposta(self):
        print('Mostrando perguntas não respondidas do fórum')

class Hipster: # classe Mixin, usada para compartilhar um comportamento que não é o core da classe mais relevante de um obj
    def __str__(self):
        return f'Hipster, {self._nome}'



class Junior (Alura):
    pass

class Pleno (Alura, Caelum): # aplicação da herança multipla 
    pass

class Senior(Alura, Caelum, Hipster):
    pass 

jose = Junior('Jose')
jose.busca_perguntas_sem_resposta()

luan = Pleno('Luan') #ordem de busca de metodos do python(Method Resolution Order): Pleno > Alura > Caelum > Funcionario
luan.busca_cursos_do_mes()
luan.busca_perguntas_sem_resposta()
luan.mostrar_tarefas()

Mateus = Senior('Mateus')
print(Mateus)