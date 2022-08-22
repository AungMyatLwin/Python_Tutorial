
def f(n):
    if n==0:
        return print("*"*15)
    
    for i in range(n):
        
        f(n-1)



f(3)