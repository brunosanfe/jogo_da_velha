item={
      'tv': 1200,
      'cama':700,
      'videogame':500
}
#print(item['cama'])
for elemento in item.items():
    print(elemento)
    
# Criando um dicionário com alguns dados de exemplo
pessoa = {
    'nome': 'João',
    'idade': 30,
    'cidade': 'São Paulo',
    'profissao': 'Engenheiro'
}

# Acessando valores do dicionário
print("Nome:", pessoa['nome'])
print("Idade:", pessoa['idade'])
print("Cidade:", pessoa['cidade'])
print("Profissão:", pessoa['profissao'])

# Adicionando um novo par chave-valor ao dicionário
pessoa['email'] = 'joao@example.com'

# Modificando um valor existente no dicionário
pessoa['idade'] = 32

# Removendo um par chave-valor do dicionário
del pessoa['cidade']

# Verificando se uma chave existe no dicionário
if 'profissao' in pessoa:
    print("Profissão de João:", pessoa['profissao'])

# Iterando sobre as chaves do dicionário
print("\nChaves do dicionário:")
for chave in pessoa:
    print(chave)

# Iterando sobre os valores do dicionário
print("\nValores do dicionário:")
for valor in pessoa.values():
    print(valor)

# Iterando sobre os pares chave-valor do dicionário
print("\nPares chave-valor do dicionário:")
for chave, valor in pessoa.items():
    print(chave, ":", valor)