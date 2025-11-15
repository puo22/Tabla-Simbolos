# -------------------------
#     AST NODE
# -------------------------
class Nodo:
    def __init__(self, tipo, valor=None, hijos=None):
        self.tipo = tipo
        self.valor = valor
        self.hijos = hijos if hijos else []

    def __repr__(self, nivel=0):
        s = "  " * nivel + f"{self.tipo}: {self.valor}\n"
        for h in self.hijos:
            s += h.__repr__(nivel + 1)
        return s


# -------------------------
#     TOKENIZER SIMPLE
# -------------------------
def tokenizar(codigo):
    tokens = []
    actual = ""

    for c in codigo:
        if c.isspace():
            if actual:
                tokens.append(actual)
                actual = ""
        elif c in "=+-*/()":
            if actual:
                tokens.append(actual)
                actual = ""
            tokens.append(c)
        else:
            actual += c

    if actual:
        tokens.append(actual)
    return tokens


tokens = []
pos = 0


def token_actual():
    return tokens[pos] if pos < len(tokens) else None


def consumir(t):
    global pos
    if token_actual() == t:
        pos += 1
    else:
        raise Exception(
            f"Error: se esperaba '{t}', llegó '{token_actual()}'"
        )


# -------------------------
#     PARSER GRAMMAR
# -------------------------

def parse_factor():
    tok = token_actual()

    if tok is None:
        raise Exception("Error inesperado: fin de entrada")

    if tok.isdigit():
        consumir(tok)
        return Nodo("NUM", tok)

    if tok.isidentifier():
        consumir(tok)
        return Nodo("ID", tok)

    if tok == "(":
        consumir("(")
        nodo = parse_expr()
        consumir(")")
        return nodo

    raise Exception(f"Token inválido en factor: {tok}")


def parse_term_prime(nodo):
    tok = token_actual()

    if tok == "*":
        consumir("*")
        der = parse_factor()
        nuevo = Nodo("*", None, [nodo, der])
        return parse_term_prime(nuevo)

    if tok == "/":
        consumir("/")
        der = parse_factor()
        nuevo = Nodo("/", None, [nodo, der])
        return parse_term_prime(nuevo)

    return nodo


def parse_term():
    izq = parse_factor()
    return parse_term_prime(izq)


def parse_expr_prime(nodo):
    tok = token_actual()

    if tok == "+":
        consumir("+")
        der = parse_term()
        nuevo = Nodo("+", None, [nodo, der])
        return parse_expr_prime(nuevo)

    if tok == "-":
        consumir("-")
        der = parse_term()
        nuevo = Nodo("-", None, [nodo, der])
        return parse_expr_prime(nuevo)

    return nodo


def parse_expr():
    izq = parse_term()
    return parse_expr_prime(izq)


def parse_assignment():
    nombre = token_actual()
    consumir(nombre)
    consumir("=")
    expr = parse_expr()
    return Nodo("=", None, [Nodo("ID", nombre), expr])


def parse_stmt():
    tok = token_actual()
    if tok is None:
        return None

    if tok.isidentifier() and tokens[pos + 1] == "=":
        return parse_assignment()

    return parse_expr()


def parse_stmt_list():
    lista = []
    while token_actual() is not None:
        lista.append(parse_stmt())
    return Nodo("program", None, lista)


def parsear(codigo):
    global tokens, pos
    tokens = tokenizar(codigo)
    pos = 0
    return parse_stmt_list()


# -------------------------
#   SYMBOL TABLE
# -------------------------
def tabla_simbolos(ast):
    tabla = {}

    def recorrer(n):
        if n.tipo == "=":
            tabla[n.hijos[0].valor] = "variable"
        for h in n.hijos:
            recorrer(h)

    recorrer(ast)
    return tabla


# -------------------------
#  THREE ADDRESS CODE
# -------------------------

temp_count = 0
codigo3d = []


def nueva_temp():
    global temp_count
    t = f"t{temp_count}"
    temp_count += 1
    return t


def gen3d(nodo):
    if nodo.tipo in ("NUM", "ID"):
        return nodo.valor

    if nodo.tipo in ("+", "-", "*", "/"):
        izq = gen3d(nodo.hijos[0])
        der = gen3d(nodo.hijos[1])
        t = nueva_temp()
        codigo3d.append(f"{t} = {izq} {nodo.tipo} {der}")
        return t

    if nodo.tipo == "=":
        val = gen3d(nodo.hijos[1])
        codigo3d.append(f"{nodo.hijos[0].valor} = {val}")
        return nodo.hijos[0].valor


def generar_codigo_3d(ast):
    global codigo3d, temp_count
    codigo3d = []
    temp_count = 0
    for s in ast.hijos:
        gen3d(s)
    return codigo3d
