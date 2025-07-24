print("Quadro de horários funcionários")

funcionarios = set(['João', 'Pedro', 'Marcio','Karina', 'Josefa', 'Linda','Nathaly', 'Luan', 'Felipe'])

turnoDia= set(['João', 'Pedro','Karina', 'Josefa', 'Linda'])

turnoNoite  = set(['Marcio','Nathaly', 'Luan', 'Felipe'])

temCarro = set(['João', 'Josefa', 'Luan'] )

print(f"Funcionários que trabalham a noite e tem carro: {temCarro & turnoNoite}")

print(f"Funcionários que tem carro e trabalham durante o dia: {temCarro & turnoDia}")

print(f"Funcionários que não tem carro: {funcionarios - temCarro}")
