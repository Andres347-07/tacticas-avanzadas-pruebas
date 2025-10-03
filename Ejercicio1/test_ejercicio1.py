import sqlite3
import unittest
from app import setup_schema, insert_cliente, perform_complex_transaction

class DummyEmailService:
    def __init__(self):
        self.sent = []

    def send(self, to, subject, body):
        self.sent.append((to, subject, body))
        return True

class FailingEmailService:
    def send(self, to, subject, body):
        raise RuntimeError("Simulated SMTP failure")

class TestEjercicio1(unittest.TestCase):
    def setUp(self):
        self.conn = sqlite3.connect(":memory:")
        self.conn.execute("PRAGMA foreign_keys = ON")
        setup_schema(self.conn)
        self.cliente_id = insert_cliente(self.conn, "Cliente Prueba")

    def tearDown(self):
        self.conn.close()

    def test_insert_and_rollback(self):
        cur = self.conn.cursor()
        self.conn.execute("BEGIN")
        cur.execute("INSERT INTO citas (cliente_id, fecha) VALUES (?, ?)", (self.cliente_id, "2025-10-02"))
        self.conn.rollback()

        cur.execute("SELECT COUNT(*) FROM citas")
        count = cur.fetchone()[0]
        self.assertEqual(count, 0, "Después del rollback no debe haber citas")

    def test_constraint_cliente_inexistente(self):
        cur = self.conn.cursor()
        with self.assertRaises(sqlite3.IntegrityError):
            cur.execute("INSERT INTO citas (cliente_id, fecha) VALUES (?, ?)", (9999, "2025-10-02"))
            self.conn.commit()

    def test_complex_transaction_commit_and_email_sent(self):
        email_service = DummyEmailService()
        email_to = "cliente@example.com"
        cita_id, factura_id = perform_complex_transaction(self.conn, self.cliente_id, "2025-10-02", 150.0, email_service, email_to)

        cur = self.conn.cursor()
        cur.execute("SELECT COUNT(*) FROM citas WHERE id = ?", (cita_id,))
        self.assertEqual(cur.fetchone()[0], 1)

        cur.execute("SELECT COUNT(*) FROM facturas WHERE id = ?", (factura_id,))
        self.assertEqual(cur.fetchone()[0], 1)

        self.assertEqual(len(email_service.sent), 1)
        sent_to, subj, body = email_service.sent[0]
        self.assertEqual(sent_to, email_to)
        self.assertIn("Factura", subj)

    def test_complex_transaction_rollback_on_email_failure(self):
        failing_email = FailingEmailService()
        email_to = "cliente@example.com"
        with self.assertRaises(RuntimeError):
            perform_complex_transaction(self.conn, self.cliente_id, "2025-10-02", 200.0, failing_email, email_to)

        cur = self.conn.cursor()
        cur.execute("SELECT COUNT(*) FROM citas")
        self.assertEqual(cur.fetchone()[0], 0)
        cur.execute("SELECT COUNT(*) FROM facturas")
        self.assertEqual(cur.fetchone()[0], 0)
