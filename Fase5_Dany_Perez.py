# Fase 5 - Evaluación Final POA
# Problema 3: Inventario - Reabastecimiento
# Autor: Dany Yeferson Perez Castillo
# Grupo: 213022_1060
# Programa: Ingeniería de Sistemas - CEAD Fusagasugá
# Curso: Fundamentos de Programación - 213022

# Matriz: [Codigo, Nombre, Stock actual, Stock minimo]
inventario = [
    ["A001", "Arroz", 5, 20],
    ["A002", "Aceite", 30, 15],
    ["A003", "Azucar", 8, 25],
    ["A004", "Sal", 50, 30],
    ["A005", "Frijoles", 12, 12],
]

# Función que calcula cuánto pedir
def cantidad_a_pedir(stock_actual, stock_minimo):
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    else:
        return 0

# Programa principal - Recorre la matriz
print("===== INVENTARIO - REABASTECIMIENTO =====")
for articulo in inventario:
    codigo = articulo[0]
    nombre = articulo[1]
    actual = articulo[2]
    minimo = articulo[3]
    pedir = cantidad_a_pedir(actual, minimo)
    print(f"{nombre} | Stock actual: {actual} | Minimo: {minimo} | Pedir: {pedir}")