#!usr/bin/env python
# -*- coding: latin1 -*-

#Exercicio 1 - Faça um programa que leia a idade de uma pessoa expressa em dias e mostre-a expressa em anos, meses e dias.
# --coding:latin1--
from datetime import date
current_date = date.today()
data_nascimento= int(input("Seu ano de nascimento: "))
data_actual = current_date.year
idade =data_actual-data_nascimento
mes = idade * 12
dias = idade * 365

print(idade,"ano(s)")
print(mes,"Meses" )
print (dias,"Dias")

# Exercicio 2 - Elaborar um programa que lê 3 valores a,b,c e verifica se eles formam
# ou não um triângulo. Supor que os valores lidos são inteiros e positivos. Caso
# os valores formem um triângulo, calcular e escrever a área deste triângulo. Se
# não formam triângulo escrever os valores lidos. (Se a &gt; b + c não formam
# triângulo algum, se a é o maior).20

r1= float(input('primeiro lado: '))
r2 = float(input('segundo lado: '))
r3 = float(input('terceiro lado: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Forma triangulo')
else:
   print('Nao forma')

#Exercico 3 - Faça um programa que leia 3 números inteiros e mostre o menor deles.

primeiro = int(input('Primeiro numero: '))
segundo = int(input('Segundo numero : '))
terceiro = int(input('Terceiro numero: '))

menor = primeiro

if (segundo < menor):
    menor = segundo
if (terceiro < menor):
    menor = terceiro

print('Menor: ', menor)

#Exercicio 4 - ? Implementar uma função que retorne verdadeiro se o número for primo
#(falso caso contrário). Testar de 1 a 100.

def is_prime(n):

    if n < 2:
        return False

    for i in range(2, n):
        if not n % i:
            return False
    else:
        return True

# Para x de 1 a 100
for x in range(1, 101):
    if is_prime(x):
        print x

#Exercicio 5 - Escreva uma função que:
#a) Receba uma frase como parâmetro.
# b) Retorne uma nova frase com cada palavra com as letras invertidas.

def reverse1(t):
    r = t.split()
    for i in xrange(len(r)):
        r[i] = r[i][::-1]
    return ' '.join(r)


def reverse2(t):
    return ' '.join(s[::-1] for s in t.split())

f = 'Eu estudo Phyton'
print reverse1(f)
print reverse2(f)




