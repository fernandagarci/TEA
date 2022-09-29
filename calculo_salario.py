# Tendencias e Innovación en Tecnología Agrícola (TEA)

def calcularSalario(horas, tarifa):
    MAX_HORAS_SEMANALES = 40
    horas_extras = 0
    horas_extras = horas - MAX_HORAS_SEMANALES     
    if (horas_extras > 0): 
        salario = (MAX_HORAS_SEMANALES * int((tarifa))) + (horas_extras * (int(tarifa) * 1.5))
    else:
        salario = horas * tarifa
    return salario

try:
    horas = int(input("Ingrese número de horas: "))          
    tarifa = float(input("Ingrese tarifa por horas: "))       
    pago = calcularSalario(horas, tarifa)
    print(pago)
except:
    print("Error, debe ingresar un valor númerico")