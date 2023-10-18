# Exercício Python 10: faça um algoritimo que receba a velocidade em Km/h de um veiculo e:
# se maior que 60km/h aplicar multa de 7 vezes a da velocidade permitida
print('Qual o valor da sua multa')
vel= float(input("digite a velocidade:"))
ece= (vel-60) * 7 
if vel < 60:
    print('você não tem multa')
else:
    print(f"o valor da sua multa é:{ece}R$")