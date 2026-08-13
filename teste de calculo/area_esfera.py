circunferenciaEsfera = input("Digite a circunferencia da sua esfera em metro: ")

calculoRaioEsfera_aredondado = int(circunferenciaEsfera) / (2 * 3.14)
calculoCircunferenciaEsfera_aredondado = 4 * 3.14 * (calculoRaioEsfera_aredondado ** 2)

print(str(f"{calculoCircunferenciaEsfera_aredondado:.0f}") + "m²")