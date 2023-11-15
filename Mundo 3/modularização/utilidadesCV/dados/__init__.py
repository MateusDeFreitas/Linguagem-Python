def leiaDinheiro(msg):
    while True:
        v = str(input(msg)).replace(",",".")
        try:
            if float(v):
                return float(v)
                break
        except:
            print(f"erro dígite um valor valido")
