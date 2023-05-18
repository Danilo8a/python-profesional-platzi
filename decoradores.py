from datetime import datetime


# Ejemplo de decoradores en la clase 10
def mayusculas(func):
    def rapper(txt: str):
        return func(txt).upper()
    return rapper


# Sin la sugar syntax para decoradores
def mensaje(name: str) -> str:
    return f"{name}, recibiste un mensaje!"


# Ejercicio de la clase 11: decorador que mide el tiempo que tarda una función en ejecutarse
def execution_time(func):
    def rapper(*args, **kwargs):
        init = datetime.now()
        func(*args, **kwargs)
        final = datetime.now()
        delta_time = final - init
        print(f"Pasaron {delta_time.total_seconds()} segundos")
    return rapper


@execution_time
# Función de prueba
def random_func(i: int):
    for _ in range(1, i):
        pass


@execution_time
def suma(a: int, b: int) -> int:
    return a + b


@execution_time
def saludo(nombre="Pepe"):
    print(f"Hola {nombre}!")


if __name__ == "__main__":
    # saludo = mayusculas(mensaje)
    # print(saludo("Danilo"))

    random_func(1000000)
    suma(5, 5)
    saludo("Danilo")
