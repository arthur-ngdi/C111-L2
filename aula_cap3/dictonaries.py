# DICTIONARIES
# POSSUI CHAVES E VALORES (INDICES CUSTOMIZAVEIS)
# MUTAVEL

pessoa = {
            'nome': 'Goku', 
            'idade': 42
        }
print(pessoa)

# INSERT
pessoa['sexo'] = 'M'
print(pessoa)

#UPDATE
pessoa['idade'] = 40
print(pessoa)

#DELETE
pessoa.pop('nome')
print(pessoa)
