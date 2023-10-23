# Exercício Python 17: Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com a sua idade, se
#  ele ainda vai se alistar ao serviço militar, se é a hora exata
# de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar
# o tempo que falta ou que passou do prazo.

print("Saiba quanto tempo falta para você se alistar")
idade = int(input("Digite sua idade: "))

if idade > 18:
    print(f"O alistamento obrigatório deve ser feito com 18 anos. Você está a {idade-18} anos atrasado.")
elif idade == 18:
    print("Você está com a idade exata para se alistar, acesse o site alistamento.eb.mil.br para mais informações.")
elif idade < 18:
    print(f"Você ainda não está na idade para se alistar. O alistamento obrigatório só acontece quando você completa 18 anos, espere mais {18-idade}anos atrasados")