# Continuando no estudo de OO 
#%%

class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title() # somente um _, ainda serve para o mesmo propósito. Porém isso evita problemas nas classes filhos
        self.ano = ano
        self._likes = 0 
    
    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def __str__(self): # metodo pythonica de imprimir os atributos de uma classe
        return f'Nome: {self.nome} Likes: {self.likes}'   
 
class Filme(Programa): #Filme(Programa) indica que a classe Filme é filha da classe programa 
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano) # chamando os atributos da classe mae para esta classe
        self.duracao = duracao

    def __str__(self):
        return f'Nome: {self.nome} - {self.duracao} min - Likes: {self.likes}'    

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'Nome: {self.nome} - {self.temporadas} temporadas - Likes: {self.likes}'    

class Playlist():
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__ (self, item): # metodo built in, nos ajuda a iterar sobre a classe
        return self._programas[item]
    
    @property
    def listagem(self):
        return self._programas

    def __len__(self):
        return len(self._programas)

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
tmep = Filme('todo mundo em panico', 1999, 100)
demolidor = Serie('demolidor', 2016, 2)

vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()
atlanta.dar_likes()
atlanta.dar_likes()
tmep.dar_likes()
tmep.dar_likes()
demolidor.dar_likes()
demolidor.dar_likes()

listinha = [atlanta, vingadores, demolidor, tmep]
minha_playlist = Playlist('fim de semana', listinha)

print(f'Tamanho: {len(minha_playlist.listagem)}') # método __len_- atua aqui, permitindo usarmos len direto sobre a playlist

print(minha_playlist[0]) # aqui já é usada o metodo __getitem__

#for programa in listinha:
    #print(programa) # através dos novos métodos __str__ implementados, a próprio objeto ja sabe a qual classe pertence e imprime seus atributos próprios

