f = open ('fibonacci.txt','r')
numero = int(f.read())
f.close()

def fib(numero):
    a = 0
    b = 1
    
    for k in range(numero):
        c = b+a
        a = b
        b = c
        
    return a

