import string
import random

def genPassword():
    password=''
    char_randlist=[]
    #for com range do numero de caracteres escolhido pelo usuario para a anexação na lista(char_randlist) com strings 'aleatórias'.
    for i in range(nchar):
        char_randlist.append(random.SystemRandom().choice(string.ascii_letters+string.digits*5+'!+-_@#?'))
        password+=char_randlist[i]#lista para a string
    print(password)

nchar=int(input('\nDigite a quantidade de caracteres a serem gerados: '))

if nchar < 8:
	print('\nPor motivos de segurança, recomenda-se acima de 7 caracteres\n')
else:
	genPassword()

