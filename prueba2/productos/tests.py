import unittest
from productos.models import Producto


class testProductos(unittest.TestCase):

    def test_crear_producto(self):
        producto = Producto.objects.create(codigo = '99999',
                                           nombre_producto = 'ProductoTest',
                                           descripcion_producto = 'Prueba de agregar producto',
                                           precio = '19950',
                                           stock = '27',
                                           foto_producto = ''
                                           )
        producto.save()

        self.assertTrue(producto, True)

    def test_eliminar_producto(self):
        producto = Producto.objects.get(codigo='99999')
        if producto.codigo != "":
                producto = Producto()
                producto = Producto.objects.get(codigo='99999')
                if producto is not None:
                    print("Producto=", producto)
                    producto.delete()

        self.assertEquals(producto.codigo, '99999')
