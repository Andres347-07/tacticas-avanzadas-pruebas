class Registro:
    def __init__(self, storage, email_service, clock):
        self.storage = storage
        self.email_service = email_service
        self.clock = clock

    def registrar_usuario(self, nombre):
        fecha = self.clock.now()
        self.storage.save(f"{nombre}-{fecha}")
        self.email_service.send("Nuevo usuario")
        return True


# Dependencias reales (ejemplo, no se usan en tests)
import datetime
class RealClock:
    def now(self):
        return datetime.datetime.now()

class FileStorage:
    def __init__(self, filename="usuarios.txt"):
        self.filename = filename
    def save(self, data):
        with open(self.filename, "a") as f:
            f.write(data + "\n")

class SmtpEmailService:
    def send(self, message):
        # Aquí iría un SMTP real
        print("Enviando email:", message)
