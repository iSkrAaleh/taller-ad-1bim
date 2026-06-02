from sqlalchemy import and_
from configuracion import SessionLocal
from crear_base_entidades import Profesor

session = SessionLocal()

print("--- Consulta: AND ---")
# profesores que tienen un correo institucional y que tegan un @ y son de la especialidad 'Seguridad'
con_and = session.query(Profesor).filter(
    and_(
        Profesor.correo.like('%@%'),
        Profesor.especialidad == 'Seguridad'
    )
).all()

for a in con_and:
    print(f"Cumple AND: {a.nombres_apellidos}")

session.close()
