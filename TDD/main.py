#%%

from bytebank_corrigido import Funcionario

# lucas = Funcionario('Lucas Carvalho', '12/04/2000', 1000)
# print(lucas.idade())


def teste_idade():
    funcionario_teste = Funcionario('Teste', '13/03/2000', 1111)
    print(f'Teste = {funcionario_teste.idade()}')

    funcionario_teste1 = Funcionario('Teste', '13/03/2008', 1111)
    print(f'Teste = {funcionario_teste1.idade()}')

    funcionario_teste2 = Funcionario('Teste', '31/05/1999', 1111)
    print(f'Teste = {funcionario_teste2.idade()}')

teste_idade()    