# Sucesión de fibonacci con generadores
import time


# Generador para la serie de Fibonacci
def fibo_gen(max=None):
    i_m_1 = 0
    i = 1
    while not max or i_m_1 <= max:
        to_return = i_m_1
        next_i = i_m_1 + i
        i_m_1 = i
        i = next_i
        yield to_return


if __name__ == "__main__":
    fibonacci = fibo_gen(1000)
    for i in fibonacci:
        print(i)
        time.sleep(0.5)