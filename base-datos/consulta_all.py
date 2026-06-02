from configuracion import SessionLocal
from crear_base_entidades import Profesor

session = SessionLocal()

print("---Consulta all----")
# traemos a todos los profesores
todos = session.query(Profesor).all()

for p in todos:
    print(f"Profesor: {p.nombres_apellidos}")

session.close()
