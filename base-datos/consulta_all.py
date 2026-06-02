from configuracion import SessionLocal
from crear_base_entidades import Profesor

session = SessionLocal()

print("--- Consulta all (tpdps los profesores) ---")
profesores = session.query(Profesor).all()

for p in profesores:
    print(p)
