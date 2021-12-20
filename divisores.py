def divisores(adiv):
    comprobar = 0
    comprobado = 0
    print("Divisores de {}".format(adiv))
    while comprobar != adiv:
        comprobar = comprobar + 1
        if adiv % comprobar == 0:
            print("El divisor es {}".format(comprobar))
            comprobado = comprobado + 1
    print("El número {} tiene {} divisores".format(adiv, comprobado))
        

divisores(10)