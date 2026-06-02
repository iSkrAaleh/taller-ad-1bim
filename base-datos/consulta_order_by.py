from configuracion import SessionLocal
from crear_base_entidades import RecursoAcademico

session = SessionLocal()

print("---Consulta order_by---")
#ordena los recursos por fecha descendente
ordenados = session.query(RecursoAcademico).order_by(RecursoAcademico.fecha_publicacion.desc()).all()

for o in ordenados:
    print(f"Recurso: {o.titulo} | Fecha: {o.fecha_publicacion}")

session.close()
