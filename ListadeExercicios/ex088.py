def escreva(msg):
    tam = len(msg.strip())+4
    print("~" * tam)
    print(f"  {msg.capitalize().strip()}")
    print("~" * tam)


while True:
    escreva(str(input("Escreva unma Mensagem: ")))
    while True:
        res = str(input("Quer continuar? ")).upper().strip()[0]
        if res in "SN":
            break
        print("Digite somente Sim ou Não")
    if res == "N":
        break
