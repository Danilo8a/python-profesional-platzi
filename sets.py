# Operaciones con conjuntos


if __name__ == "__main__":
    # Unión de conjuntos
    s_1 = {3, 4, 5}
    s_2 = {5, 6, 7}

    s_1_u_2 = s_1 | s_2
    print(f"Unión: {s_1_u_2}")

    # Intersección de conjuntos
    s_1_i_2 = s_1 & s_2
    print(f"Intersección: {s_1_i_2}")

    # Diferencia
    s_1_d_2 = s_1 - s_2
    print(f"Diferencia s1 - s2: {s_1_d_2}")
    s_2_d_1 = s_2 - s_1
    print(f"Diferencia s2 - s1: {s_2_d_1}")

    # Diferencia simétrica
    s_1_ds_2 = s_1 ^ s_2
    print(f"Diferencia simétrica: {s_1_ds_2}")
