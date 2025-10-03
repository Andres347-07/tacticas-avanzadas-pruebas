# test_ejercicio3.py
import unittest
from pagos import PagoService

# Doubles 
class FakeGateway:
    def pagar(self, monto):
        return monto < 1000  

class MockEmail:
    def __init__(self):
        self.sent = []
    def send(self, to, subject, body):
        self.sent.append((to, subject, body))

class SpyNotificador:
    def __init__(self):
        self.llamadas = []
    def notificar(self, mensaje):
        self.llamadas.append(mensaje)

#  Tests 
class TestEjercicio3(unittest.TestCase):
    def test_pago_exitoso(self):
        gateway = FakeGateway()
        email = MockEmail()
        spy = SpyNotificador()
        service = PagoService(gateway, email, spy)

        result = service.procesar_pago(500, "cliente@test.com")

        
        self.assertTrue(result)
        
        self.assertEqual(len(email.sent), 1)
        self.assertIn("Pago exitoso", email.sent[0][1])
        
        self.assertIn("Pago procesado", spy.llamadas)

    def test_pago_rechazado(self):
        gateway = FakeGateway()
        email = MockEmail()
        spy = SpyNotificador()
        service = PagoService(gateway, email, spy)

        result = service.procesar_pago(1500, "cliente@test.com")

        
        self.assertFalse(result)
        
        self.assertEqual(len(email.sent), 0)
        
        self.assertIn("Pago rechazado", spy.llamadas)


if __name__ == "__main__":
    unittest.main(verbosity=2)
