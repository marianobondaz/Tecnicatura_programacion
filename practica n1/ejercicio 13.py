# Un supermercado esta estableciendo el precio de venta para nuevos productos, de estos poductos desean generar el 27% de ganancia.

ganancia_porcentaje = 27
producto            = float(input('ingrese el monto del producto:'))

ganancia            = producto *(ganancia/100)
monto_producto      = producto + ganancia

print('Este producto costara: ',monto_producto)
