# pagos.py

class PagoService:
    def __init__(self, gateway, email_service, notificador):
        self.gateway = gateway
        self.email_service = email_service
        self.notificador = notificador

    def procesar_pago(self, monto, correo):
        if self.gateway.pagar(monto):
            self.email_service.send(correo, "Pago exitoso", f"Se procesó un pago de {monto}")
            self.notificador.notificar("Pago procesado")
            return True
        else:
            self.notificador.notificar("Pago rechazado")
            return False
