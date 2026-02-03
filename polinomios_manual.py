# Función para sumar dos polinomios manualmente
# Los polinomios se representan como listas de coeficientes (desde grado más bajo a más alto)
def add_polynomials_manual(p1, p2):
    # Asegurarse de que p1 sea el más largo
    if len(p1) < len(p2):
        p1, p2 = p2, p1
    result = p1[:]
    for i in range(len(p2)):
        result[i] += p2[i]
    return result

# Ejemplo con coeficientes numéricos
poly1 = [1, 2, 3]  # 1 + 2x + 3x^2
poly2 = [4, 5]     # 4 + 5x

print("Polinomio 1:", poly1)
print("Polinomio 2:", poly2)

suma_manual = add_polynomials_manual(poly1, poly2)
print("Suma manual:", suma_manual)

# Para coeficientes simbólicos, se necesitarían librerías como SymPy.
# Aquí un ejemplo simple con strings (no algebraico real):
poly1_sym = ["a", "b", "c"]  # Representación simplificada
poly2_sym = ["d", "e"]

print("Polinomio 1 simbólico (simplificado):", poly1_sym)
print("Polinomio 2 simbólico (simplificado):", poly2_sym)

# Suma simplificada (solo concatena, no opera algebraicamente)
suma_sym_simple = [f"{poly1_sym[i]}+{poly2_sym[i]}" if i < len(poly2_sym) else poly1_sym[i] for i in range(len(poly1_sym))]
print("Suma simbólica simplificada:", suma_sym_simple)