def imc():
    pes = int(input("Quant peses? "))
    altura = float(input("Quant medeixes? "))

    estatura = altura ** 2
    imc = pes // estatura

    print("\nEl teu IMC es " + str(imc))