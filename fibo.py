"""
Suite de fibonacci
"""

def fibonacci(n, un=1, un1=1)->int:
    """
    Fonction récursive qui simule la suite de Fibonacci
    """
    return fibonacci(n-1, un1, un1+un) if n else un

#Appel de la fonction
print(fibonacci(15))