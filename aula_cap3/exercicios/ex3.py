nome = input("Digite o nome do aluno: ")
media = float(input("Digite a media do aluno: "))

if media >= 60:
    aux = "AP"
else:
    aux = "RP"

dicionario = {
    'nome': nome,
    'media': media,
    'situacao': aux
}

print(dicionario)


