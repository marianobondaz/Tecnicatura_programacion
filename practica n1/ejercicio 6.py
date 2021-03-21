# Una pintureria debe elaborar el presupuesto para un cliente y nececita calcular el costo
# total, este se deriva de la cantidad de pintura requeido y de la mano de obra, teniendo en cuenta
# lo siguiente: se requiera 1L de pintura por 1m2 y el costo de mano de obra es del 45% del precio total de pintura. 

ganancia_MO             = 0.45
costo_m2                = 1
metros_2                = int(input('ingrese la cantidad de metros2 a presupuestar :'))
Costo_litro_pintura     = int(input('ingrese el costo x litro de pintura :'))

litros_pintura          = metros_2 
costo                   = metros_2 * litros_pintura
mano_obra               = (costo * ganancia_MO) /100

print('se requieren :', litros_pintura, 'litros de pintura')

costo_total             = (metros_2 * Costo_litro_pintura) + mano_obra

print('presupuesto :', costo_total)
