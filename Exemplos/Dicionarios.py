#Utiliza index no formato no formate de keys e values.

aluno = {'nome': 'Felipe',
         'idade':  20,
         'curso': 'Ciências da computação',
         'notaFinal': 14000,
         'aprovação' :  True,
         'materias' : ['Matematica', 'Português','Fisíca']}# É possível adicionar lista de values como neste caso

# aluno.update({'nome': "José", 'notaFinal': 10000, 'endereco':'Rua A'}) #atuliza mais de um campo ao mesmo tempo
print(aluno.get('materias'))

print(len(aluno))

print(aluno.items())

print(aluno.keys())

print(aluno.values())

# del aluno ['idade'] # del deleta uma key


print(aluno)

