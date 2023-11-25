def sum(a: int, b: int):
    return a+b

def substraction(a: int, b:int):
    return a-b

def multiplication(a, b):
    return a*b

def division(a, b):
    #Se verifica que el dividendo sea diferente de cero, en ccaso de que este sea cero devolveremos un error
    if b == 0:
        #Se utiliza el raise para demostrar que se dio un error.
        return "Cannot divide by zero"
    return a / b