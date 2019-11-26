"""
print()-> comando para imprimir na tela
Ex:
print("Olá Mundo!!")
print('Olá Mundo!!')

/n -> quebra de linha 

Variáveis no python tem tipagem dinâmica, ou 
seja seu tipo e definido em tempo de compilação.
Declaração de Variáveis:
idade = 10
nome = "João"
salario = 10000.00
type() -> diz a qual classe a variável pertence
Ex:
print(type(idade))
print(type(nome))
print(type(salario))
input()-> comando de entrada de dados no python
Ex:
nome = input('Qual é o seu nome ?')

python por padrão recebe só variaveis do tipo str(String),
para receber valores reais(float) e inteiro(int)mé neces-
sario fazer um cast. 
Ex :
sou_inteiro = int(input())
sou_real = float(input())

Como imprimir uma variável em python seguida de uma frase:
nome = "vagabundo"

print("Eu sou {}".format(nome))

E como imprimir mais de uma:

print("{} sou {}".format(nome, nome))

Há outras maneiras de se imprimir uma variável seguida do texto,
mas atualmente e feita da forma que está mostrada acima.


Operadores aritméticos:
+ soma
- subtração
* multiplicação
/ divisão
** exponenciação
% resto da divisão

"""