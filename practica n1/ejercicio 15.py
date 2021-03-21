# Un grupo de amigos se hospedan en un hotel, y al momento de pagar se dividen los gastos de la seguiendte manera:
# Ivan paga el 40%
# German paga el 33%
# Esteban paga el 55% de lo que pago Ivan
# Hernan paga el resto

porcentaje_ivan     = 40
porcentaje_german   = 33
porcentaje_esteban  = 55


costo_hotel         = float(input('Ingrese el monto del hotel a pagar: '))

parte_ivan          = costo_hotel * (porcentaje_ivan/100)
monto_ivan          = costo_hotel - parte_ivan

parte_german        = costo_hotel * (porcentaje_german/100)
monto_german        = costo_total - parte_german

parte_esteban       = monto_ivan * (porcentaje_esteban/100)
monto_esteban       = monto_ivan - parte_esteban

monto_hernan        = costo_hotel -(monto_ivan + monto_german + monto_esteban)

print('Ivan:', monto_ivan)
print('German:', monto_german)
print('Esteban:', monto_esteban)
print('Hernan:', monto_hernan)