# El tema es que se usa mypy (instalado en el entorno virtual) para comprobar que los argumentos de las funciones
# correspondan con los tipos establecidos. Esto me parece tedioso, hasta este punto del curso.
# PyCharm señala los errores de tipos con subrayado rojo.

# Función para comprobar si una cadena es palíndromo con tipado estático
def is_palindrome(in_str: str) -> bool:
    in_str = in_str.replace(" ", "").lower()
    return in_str == in_str[::-1]


if __name__ == "__main__":
    print(is_palindrome(1000))
