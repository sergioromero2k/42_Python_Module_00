# 42_Python_Module_00
##  Cultivando Código – Fundamentos de Python  
**Aprendiendo Python mediante datos de huertos comunitarios**

Este proyecto introductorio enseña los conceptos básicos de Python a través de ejercicios prácticos con huertos comunitarios. Cada ejercicio se centra en funciones y operaciones simples, ayudando a entender variables, entradas/salidas, condicionales y bucles.

---

##  Estructura del Proyecto

Cada ejercicio está en su propio directorio (`ex0` a `ex7`) y archivo Python.

---

##  Ejercicio 0 – `ft_hello_garden.py`
**Objetivo:**  
Mostrar un mensaje de bienvenida.

**Requisitos:**
- Función: `ft_hello_garden()`
- Mostrar: `"Hello, Garden Community!"`
- Solo la función, no un programa principal

---

##  Ejercicio 1 – `ft_plot_area.py`
**Objetivo:**  
Calcular el área de una parcela rectangular.

**Requisitos:**
- Función: `ft_plot_area()`
- Solicitar longitud y ancho (`input()`)
- Calcular y mostrar área (`print()`)
- Solo la función, no un programa principal

---

##  Ejercicio 2 – `ft_harvest_total.py`
**Objetivo:**  
Calcular la cosecha total de 3 días.

**Requisitos:**
- Función: `ft_harvest_total()`
- Solicitar peso de cosechas diarias (`input()`)
- Calcular y mostrar total (`print()`)
- Solo la función, no un programa principal

---

##  Ejercicio 3 – `ft_plant_age.py`
**Objetivo:**  
Comprobar si una planta está lista para cosechar.

**Requisitos:**
- Función: `ft_plant_age()`
- Solicitar edad de la planta (`input()`)
- Mostrar mensaje según edad (>60 días)
- Solo la función, no un programa principal

---

##  Ejercicio 4 – `ft_water_reminder.py`
**Objetivo:**  
Recordatorio de riego según días transcurridos.

**Requisitos:**
- Función: `ft_water_reminder()`
- Solicitar días desde último riego (`input()`)
- Mostrar `"Water the plants!"` si >2 días, `"Plants are fine"` si ≤2
- Solo la función, no un programa principal

---

##  Ejercicio 5 – `ft_count_harvest_iterative.py` / `ft_count_harvest_recursive.py`
**Objetivo:**  
Contar días hasta la cosecha usando iteración y recursión.

**Requisitos:**
- Funciones: `ft_count_harvest_iterative()`, `ft_count_harvest_recursive()`
- Solicitar número de días (`input()`)
- Imprimir cada día hasta la cosecha
- Mensaje final: `"Harvest time!"`
- Solo las funciones, no un programa principal

---

##  Ejercicio 6 – `ft_garden_summary.py`
**Objetivo:**  
Mostrar un resumen del huerto.

**Requisitos:**
- Función: `ft_garden_summary()`
- Solicitar nombre del huerto y número de plantas (`input()`)
- Mostrar resumen con mensaje fijo: `"Status: Growing well!"`
- Solo la función, no un programa principal

---

##  Ejercicio 7 – `ft_seed_inventory.py`
**Objetivo:**  
Gestionar inventario de semillas con anotaciones de tipo.

**Requisitos:**
- Función: `ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None`
- Mostrar información de semillas según unidad:
  - `"packets"` → `"X seeds: Y packets available"`
  - `"grams"` → `"X seeds: Y grams total"`
  - `"area"` → `"X seeds: covers Y square meters"`
  - Cualquier otra unidad → `"Unknown unit type"`
- Solo la función, no un programa principal

---

##  Conceptos Clave
- Funciones en Python
- Entrada y salida (`input()`, `print()`)
- Variables y operaciones básicas
- Condicionales (`if`, `else`)
- Bucles (`for`, recursión)
- Tipos de datos y anotaciones de tipo
- Mensajes y formateo de strings

---

✨ *Cada archivo contiene únicamente la función solicitada y está diseñado para ejecutarse correctamente mediante `main.py` de prueba.*
