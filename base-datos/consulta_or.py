from configuracion import SessionLocal
from crear_base_entidades import RecursoAcademico
from sqlalchemy import or_

session = SessionLocal()

print("--- Consulta OR (Recursos que son Libro o Video) ---")
recursos = session.query(RecursoAcademico).filter(
    or_(
        RecursoAcademico.tipo_recurso == 'Libro',
        RecursoAcademico.tipo_recurso == 'Video'
    )
).all()

for r in recursos:
    print(r)
