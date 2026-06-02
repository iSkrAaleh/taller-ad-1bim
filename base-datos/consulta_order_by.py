from configuracion import SessionLocal
from crear_base_entidades import RecursoAcademico

session = SessionLocal()

print("--- Consulta order by (Recursos ordenados por fecha descendente) ---")
recursos = session.query(RecursoAcademico).order_by(RecursoAcademico.fecha_publicacion.desc()).all()

for r in recursos:
    print(r)
