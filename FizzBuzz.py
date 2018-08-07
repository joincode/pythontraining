import os 
os.system('cls')
# O %s é utilizado como marcador de posicao
#https://docs.python.org/3.4/library/string.html
print ("Criar um Programa Teste FizzBuzz!!!")
line = 0
while (line < 100):
    line += 1
    if (line % 3 == 0 ) and (line % 5 == 0):
        print ("%s - FizzBuzz!!!" % line )
        
    elif (line % 3 == 0):
        print ("%s - Fizz!!" % line)
    
    elif (line % 5 == 0):
        print ("%s - Buzz!!" % line)
    
    else:
        print (line)