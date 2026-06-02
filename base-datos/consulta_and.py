from configuracion import SessionLocal
from crear_base_entidades import Profesor
from sqlalchemy import and_

session = SessionLocal()

print("--- Consulta and (Correo con @ Y de Salud Comunitaria) ---")
profesores = session.query(Profesor).filter(
    and_(
        Profesor.correo.like('%@%'),
        Profesor.especialidad == 'Salud Comunitaria'
    )
).all()

for p in profesores:
    print(p)
