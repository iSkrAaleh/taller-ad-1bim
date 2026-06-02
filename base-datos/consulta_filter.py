from configuracion import SessionLocal
from crear_base_entidades import Profesor

session = SessionLocal()

print("--- Consulta FILTER (profesores de salud comunitaria) ---")
profesores = session.query(Profesor).filter(Profesor.especialidad == 'Salud Comunitaria').all()

for p in profesores:
    print(p)
