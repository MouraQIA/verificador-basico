import hashlib

def calcular_hash(caminho):
    h = hashlib.sha256()
    with open(caminho, "rb") as arquivo:
        while True:
            pedaco = arquivo.read(65536)
            if not pedaco:
                break
            h.update(pedaco)

    return (h.hexdigest())

print(calcular_hash("teste.txt"))