from configuracion import SessionLocal
from crear_base_entidades import RecursoAcademico, Profesor, Carrera, Facultad

session = SessionLocal()

#definimos la facultad aca
facultad_buscar = 'Facultad de Ingeniería'

print(f"---consulta nueva recursos de la {facultad_buscar} ---")


recursos = session.query(RecursoAcademico)\
    .join(Profesor)\
    .join(Carrera)\
    .join(Facultad)\
    .filter(Facultad.nombre == facultad_buscar)\
    .all()

# Verificamos si encontró algo para imprimirlo
if recursos:
    for r in recursos:
        print(r)
else:
    print(f"no se encontraron recursos para la {facultad_buscar}")