# Calcular el promedio de temperatura y presion recolectado por una estacion metereologica en una semana, 
# considerando que realiza soloa una medida por dia.

temp_lunes              = 30
temp_martes             = 29.5
temp_miercoles          = 28.5
temp_jueves             = 25.9
temp_viernes            = 24.5
temp_sabado             = 23.5
temp_domingo            = 23

pres_lunes              = 1000
pres_martes             = 1050
pres_miercoles          = 1100
pres_jueves             = 1150
pres_viernes            = 1120
pres_sabado             = 1100
pres_domingo            = 1080


calculo_promedio_temp   = (temp_domingo + temp_sabado + temp_viernes + temp_jueves + temp_miercoles + temp_martes + temp_lunes)/7

calculo_promedio_pres   = (pres_domingo + pres_sabado + pres_viernes + pres_jueves + pres_miercoles + pres_martes + pres_lunes)/7

print('Promedio de temperaturas: ',calculo_promedio_temp)
print('Promedio de presiones: ',calculo_promedio_pres)
