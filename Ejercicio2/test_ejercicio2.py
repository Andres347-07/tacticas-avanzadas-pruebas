import unittest
from app_refactor import Registro

class FakeClock:
    def now(self):
        return "2025-10-02 10:00:00"

class FakeStorage:
    def __init__(self):
        self.data = []
    def save(self, data):
        self.data.append(data)

class FakeEmailService:
    def __init__(self):
        self.sent = []
    def send(self, message):
        self.sent.append(message)

class TestEjercicio2(unittest.TestCase):
    def test_registro_usuario(self):
        clock = FakeClock()
        storage = FakeStorage()
        email = FakeEmailService()
        registro = Registro(storage, email, clock)

        result = registro.registrar_usuario("Diego")

        # Verificar que se guardó en el storage
        self.assertIn("Diego-2025-10-02 10:00:00", storage.data[0])
        # Verificar que se envió el email
        self.assertIn("Nuevo usuario", email.sent[0])
        # Verificar que devolvió True
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main(verbosity=2)
