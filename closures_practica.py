# Función con closures al que se le ingresa un string y lo imprime n veces el string
# Ejemplo: Danilo y 4 -> DaniloDaniloDaniloDanilo

def n_times(n: int):
    # Le he agregado un pequeño espacio entre palabras
    def string_n_times(string: str):
        assert type(string) == str, "Solo puedes ingresar cadenas de texto"
        return n * (string + " ")

    return string_n_times


# Reto del curso: implementar la siguiente función con closures
def make_division_by(n: int):
    """This closure returns a function that returns the division
       of an x number by n
    """
    def division_x_n(x: int):
        return x / n

    return division_x_n


if __name__ == "__main__":
    string_5 = n_times(5)
    print(string_5("Danilo"))

    # Comprobación del closure del reto
    division_by_3 = make_division_by(3)
    print(division_by_3(18))

    division_by_5 = make_division_by(5)
    print(division_by_5(100))

    division_by_18 = make_division_by(18)
    print(division_by_18(54))
