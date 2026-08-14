circunferencia_circulo = int(input("digite a circunferencia do circulo: "))
calculo_raio_circulo = (circunferencia_circulo/3.14)/2
calculo_area_circulo = 3.14*(calculo_raio_circulo**2)

print(str(f"{calculo_area_circulo:.0f}") + "m²")