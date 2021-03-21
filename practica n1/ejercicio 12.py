# Una empresa distribuidora de energia le cobra a sus abonados el consumo de KW por
# hora pero ademas debe sumarle el 0.21% de impuesto, pero actualmente todos los clientes
# estan dentro de un plan de promocion que les descuenta el 3.7% del monto total a pagar

kw_hora_precio          = 1
impuesto                = 0.21
descuento               = 3.7

kw_consumidos           = int(input('ingrese los KW/h consumidos: '))

aumento                 = kw_consumidos * (impuesto/100)
precio_con_aumento      = kw_consumidos + aumento

promocion               = precio_con_aumento * (3.7/100)
precio_cliente          = precio_con_aumento - promocion

print('monto del servicio,  ', precio_con_aumento,' - bonificacion, total a pagar:',precio_cliente)