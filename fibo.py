"""
Suite de fibonacci
"""

def fibonacci(nombre, fibo=1, fibo1=1)->int:
    """
    Fonction récursive qui simule la suite de Fibonacci
    """
    return fibonacci(nombre-1, fibo1, fibo1+fibo) if nombre else fibo

#Appel de la fonction
print(fibonacci(15))
