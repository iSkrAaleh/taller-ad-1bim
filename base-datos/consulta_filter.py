from configuracion import SessionLocal
from crear_base_entidades import Profesor

session = SessionLocal()

print("----Consulta filter----")
#filtramos profesores que tengan una especialidad exacta
filtrados = session.query(Profesor).filter(Profesor.especialidad == 'Ingeniería de Software').all()

for f in filtrados:
    print(f"Profesor de Software: {f.nombres_apellidos}")

session.close()
