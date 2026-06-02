from sqlalchemy import or_
from configuracion import SessionLocal
from crear_base_entidades import RecursoAcademico

session = SessionLocal()

print("--- Consulta or ---")
#recursos que son del tipo 'libro' o del tipo 'video'
con_or = session.query(RecursoAcademico).filter(
    or_(
        RecursoAcademico.tipo_recurso == 'Libro',
        RecursoAcademico.tipo_recurso == 'Video'
    )
).all()

for r in con_or:
    print(f"Cumple OR: {r.titulo} | Tipo: {r.tipo_recurso}")

session.close()
