import time


my_list = [1, 2, 3, 4, 5]
my_iter = iter(my_list)

# La siguiente sentencia es la implementación interna de un ciclo for en python. Interesante...
while True:
    try:
        elem = next(my_iter)
        print(elem)
    except StopIteration:
        break


# Clase de ejemplo que implementa los métodos de los iteradores __iter__ y __next__
class EvenNumbers:

    def __init__(self, max=None):
        self.max = max

    # Establece las condiciones iniciales para la iteración del objeto
    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        if not self.max or self.num <= self.max:
            current = self.num
            self.num += 2
            return current
        else:
            raise StopIteration


# Ejercicio para implementar iteradores, clase con la sucesión de Fibonacci
class FiboIter:
    def __init__(self, max=None):
        self.max = max

    def __iter__(self):
        self.i = 0
        self.i_up_1 = 1
        return self

    def __next__(self):
        if not self.max or self.i <= self.max:
            to_return = self.i
            next_i = self.i + self.i_up_1
            self.i = self.i_up_1
            self.i_up_1 = next_i
            return to_return
        else:
            raise StopIteration


if __name__ == "__main__":
    evens = EvenNumbers(max=10)
    for even in evens:
        print(even)

    fibo = FiboIter(max=1000)
    for i in fibo:
        print(i)
