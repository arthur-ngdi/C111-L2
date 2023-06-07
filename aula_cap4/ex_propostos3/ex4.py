import numpy as np

arr = np.loadtxt('aula_cap4/files/space.csv', 
                 delimiter=';', 
                 encoding='utf-8', 
                 dtype=str)

empresa = arr[0:,1] #Seleciona da primeira linha até ultima os elementos da primeira coluna. Esta se refere ao nome da empresa
missoes = arr[empresa == "SpaceX"] #Dentro array principal (arr) seleciona-se as informações onde o nome da empresa é SpaceX
custo = missoes[0:,6] #Seleciona-se dentro do array de missoes apenas o custo das missoes feitas pela SpaceX

print(custo) #Printa o máximo dos custo selecionados





