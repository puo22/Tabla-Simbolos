# TABLA DE SIMBOLOS.

### **EDTS sobre una Gramática Simplificada de Python**

Este proyecto implementa un **EDTS (Esquema de Traducción Dirigido por la Sintaxis)** que analiza asignaciones y expresiones aritméticas en un subconjunto de Python.
A partir de una entrada en texto, el sistema produce:

* ✔ Árbol Sintáctico Abstracto (AST / ETDS)
* ✔ Tabla de Símbolos
* ✔ Código Intermedio en Tres Direcciones

La salida se guarda automáticamente en **`salida.txt`**.

---

## 📄 1. Gramática Usada

> **Nota:** La gramática NO aparece en `salida.txt`.
> Solo se documenta aquí para referencia del proyecto.

```
program     -> stmt_list

stmt_list   -> stmt (NEWLINE stmt)*

stmt        -> ID "=" expr
             | expr

expr        -> term ((PLUS | MINUS) term)*

term        -> factor ((TIMES | DIV) factor)*

factor      -> NUMBER
             | ID
             | "(" expr ")"

Tokens:
NUMBER   = dígitos (con o sin decimal)
ID       = letra o "_" seguido de letras, dígitos o "_"
PLUS     = "+"
MINUS    = "-"
TIMES    = "*"
DIV      = "/"
EQ       = "="
LPAREN   = "("
RPAREN   = ")"
NEWLINE  = "\n"
```

---

## 2. Estructura del Proyecto

```
/Tabla_Sim/
├── main.py                 # Controlador principal
├── funciones.py            # Lexer, parser, AST
├── gramatica.py            # Archivo de gramática (solo documentación)
├── entrada.py              # Entrada a analizar
├── salida.txt              # Salida generada automáticamente
└── README.md               # Este documento
```

---

## Ejemplo de Entrada (`entrada.py`)

```
x = 3 + 4 * 2
y = x - 1
z = (x + y) * 2
```

---

## 4. Ejecución

Ejecuta el programa desde consola:

```bash
python main.py
```

o indicando un archivo de entrada:

```bash
python main.py entrada.py
```

Esto genera automáticamente **`salida.txt`** con la información procesada.

---

## 5. Formato de `salida.txt`

El archivo contiene:

### 🔷 **1. AST (ETDS)**

Representación estructurada del árbol sintáctico.

### 🔷 **2. Tabla de Símbolos**

Identificadores presentes y su tipo o rol.

### 🔷 **3. Código Intermedio (Tres Direcciones)**

Traducción lineal del AST a instrucciones tipo:

```
t0 = 4 * 2
t1 = 3 + t0
x = t1
```

---

---

## 👤 7. Autor

Paula Alejandra Ortiz Salon

---
