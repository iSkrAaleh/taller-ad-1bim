### Resumen de Consultas

* **1. ALL (`consulta_all.py`):** Trae absolutamente todos los datos de una tabla aqui simplemente listamos a todos los profesores registrados
* **2. FILTER (`consulta_filter.py`):** Busca registros que cumplan una condición exacta lo usamos para encontrar profesores de una especialidad en específico
* **3. ORDER_BY (`consulta_order_by.py`):** Sirve para ordenar los resultados aqui listamos los recursos académicos por fecha, del más nuevo al más antiguo
* **4. AND (`consulta_and.py`):** Obliga a que se cumplan **dos condiciones a la vez** filtramos a los profesores que tienen un correo válido (contiene `@`) y que pertenecen a "Salud Comunitaria"
* **5. OR (`consulta_or.py`):** Trae resultados si se cumple **al menos una** condición lo  usamos para buscar recursos que sean exclusivamente tipo "Libro" o "Video"
* **6. JOIN / Consulta Nueva (`consulta_nueva.py`):** Permite cruzar múltiples tablas conectadas entre sí (Recurso -> Profesor -> Carrera -> Facultad) lo usamos para listar todos los recursos académicos que pertenecen a una facultad en específico
