import json
from configuracion import SessionLocal
from crear_base_entidades import Profesor, Carrera

def poblar_profesores():
    session = SessionLocal()
    ruta = 'data/datos_universidad/datos/profesores.json'
    
    try:
        with open(ruta, 'r', encoding='utf-8') as archivo:
            datos = json.load(archivo)
            
            for fila in datos:
                carrera_obj = session.query(Carrera).filter_by(nombre=fila['carrera']).first()
                
                nombres = fila.get('nombres', '')
                apellidos = fila.get('apellidos', '')
                nombre_completo = f"{nombres} {apellidos}".strip()
                
                if carrera_obj:
                    profesor = Profesor(
                        nombres_apellidos=nombre_completo,
                        correo=fila['correo'],
                        especialidad=fila['especialidad'],
                        carrera_id=carrera_obj.id 
                    )
                    session.add(profesor)
                else:
                    print(f"no se encontró la carrera para el profesor {nombre_completo}")
        
        session.commit()
        print("Profesores ingresados exitosamente")
    except Exception as e:
        session.rollback()
        print(f"Error al poblar profesores: {e}")
    finally:
        session.close()

if __name__ == "__main__":
    poblar_profesores()
