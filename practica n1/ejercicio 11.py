# Una empresa telefonica debe facturar el costo de las llamadas telefonicas a sus clientes para esto les cobra por un tiempo de llamada
# (por minutos pero ademas le adiccna un 0.25% del monto total de la llamada)

costo_minuto = 50
adicional = 1.5

minutos_llamadas = int (input('ingrese los minutos de la llamada:'))

costo = minutos_llamadas * costo_minuto * adicional
print ('costo del servicio :', costo)
