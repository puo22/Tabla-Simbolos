# main.py

from entrada import ENTRADA
from funciones import parsear, tabla_simbolos, generar_codigo_3d
from gramatica import GRAMATICA

def main():
    ast = parsear(ENTRADA)
    tabla = tabla_simbolos(ast)
    codigo3d = generar_codigo_3d(ast)

    with open("salida.txt", "w") as f:
        f.write("=== AST (ETDS) ===\n")
        f.write(ast.__repr__() + "\n")

        f.write("\n=== TABLA DE SÍMBOLOS ===\n")
        for nombre, tipo in tabla.items():
            f.write(f"{nombre} : {tipo}\n")

        f.write("\n=== CÓDIGO DE TRES DIRECCIONES ===\n")
        for linea in codigo3d:
            f.write(linea + "\n")

    print("Archivo generado: salida.txt")

main()
