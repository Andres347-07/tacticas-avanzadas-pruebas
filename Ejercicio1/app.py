import sqlite3

def setup_schema(conn):
    conn.execute("PRAGMA foreign_keys = ON")
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS clientes (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       nombre TEXT NOT NULL
                   )""")
    cur.execute("""CREATE TABLE IF NOT EXISTS citas (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       cliente_id INTEGER NOT NULL,
                       fecha TEXT,
                       FOREIGN KEY(cliente_id) REFERENCES clientes(id) ON DELETE RESTRICT
                   )""")
    cur.execute("""CREATE TABLE IF NOT EXISTS facturas (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       cita_id INTEGER NOT NULL,
                       total REAL,
                       FOREIGN KEY(cita_id) REFERENCES citas(id) ON DELETE CASCADE
                   )""")
    conn.commit()

def insert_cliente(conn, nombre):
    cur = conn.cursor()
    cur.execute("INSERT INTO clientes (nombre) VALUES (?)", (nombre,))
    conn.commit()
    return cur.lastrowid

def insert_cita(conn, cliente_id, fecha):
    cur = conn.cursor()
    cur.execute("INSERT INTO citas (cliente_id, fecha) VALUES (?, ?)", (cliente_id, fecha))
    return cur.lastrowid

def insert_factura(conn, cita_id, total):
    cur = conn.cursor()
    cur.execute("INSERT INTO facturas (cita_id, total) VALUES (?, ?)", (cita_id, total))
    return cur.lastrowid

def perform_complex_transaction(conn, cliente_id, fecha, total, email_service, email_to):
    try:
        conn.execute("BEGIN")
        cita_id = insert_cita(conn, cliente_id, fecha)
        factura_id = insert_factura(conn, cita_id, total)
        email_service.send(email_to, f"Factura #{factura_id}", f"Su cita #{cita_id} fue creada. Total: {total}")
        conn.commit()
        return cita_id, factura_id
    except Exception:
        conn.rollback()
        raise
