# Tácticas Avanzadas de Pruebas de Software

Este repositorio contiene la implementación y solución de **tres ejercicios prácticos** de pruebas de software, aplicando conceptos avanzados como transacciones, refactorización para testeabilidad e implementación de Test Doubles (Mock, Spy y Fake).


## Estructura del Proyecto
tacticas-avanzadas-pruebas/
├── Ejercicio1/
│ ├── app.py
│ └── test_ejercicio1.py
├── Ejercicio2/
│ ├── app_refactor.py
│ └── test_ejercicio2.py
└── Ejercicio3/
├── pagos.py
└── test_ejercicio3.py


---

##  Ejercicio 1: Pruebas de BD transaccionales
- **Objetivo**: Validar operaciones de base de datos dentro de una transacción.
- **Lo que se implementó**:
  - Inserciones con `commit` y `rollback`.
  - Restricciones como cliente inexistente.
  - Simulación de transacciones complejas con envío de correo.
- **Pruebas realizadas**:
  ```bash
  py -m unittest -v test_ejercicio1.py

# Ejercicio 2: Refactoring para testeabilidad

Objetivo: Refactorizar código para hacerlo más testeable usando inyección de dependencias.

- **Lo que se implementó**:
  - FakeClock, FakeStorage y FakeEmailService para simular dependencias.
  - Servicio principal desacoplado para facilitar pruebas unitarias.

- **Pruebas realizadas**:
  - py -m unittest -v test_ejercicio2.py


# Ejercicio 3: Test Doubles avanzados (Mock, Spy, Fake)

Objetivo: Aplicar diferentes tipos de Test Doubles en un sistema de pagos.

- **Lo que se implementó**:
  - Fake → Gateway de pagos que acepta pagos < 1000 y rechaza ≥ 1000.
  - Mock → Servicio de correo que guarda mensajes enviados para validación.
  - Spy → Servicio de notificaciones que registra llamadas.

- **Pruebas realizadas**:
  - py -m unittest -v test_ejercicio3.py


# Cómo ejecutar las pruebas

- **Clonar el repositorio**:
  - git clone https://github.com/Andres347-07/tacticas-avanzadas-pruebas.git

  - cd tacticas-avanzadas-pruebas

- **Entrar a la carpeta del ejercicio deseado.**

- **Ejecutar las pruebas**:
  - py -m unittest -v test_<archivo>.py

Autor: Diego Andrés Peñaranda Soto