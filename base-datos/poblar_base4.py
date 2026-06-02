import json
from datetime import datetime
from configuracion import SessionLocal
from crear_base_entidades import RecursoAcademico, Profesor

def poblar_recursos():
    session = SessionLocal()
    ruta = 'data/datos_universidad/datos/recursos_academicos.json'
    
    try:
        with open(ruta, 'r', encoding='utf-8') as archivo:
            datos = json.load(archivo)
            
            for fila in datos:
                profesor_obj = session.query(Profesor).filter_by(nombres_apellidos=fila['profesor']).first()
                
                if profesor_obj:
                    fecha_obj = datetime.strptime(fila['fecha_publicacion'], '%Y-%m-%d').date()
                    
                    recurso = RecursoAcademico(
                        titulo=fila['titulo'],
                        fecha_publicacion=fecha_obj,
                        tipo_recurso=fila['tipo'], 
                        url=fila['url'],
                        profesor_id=profesor_obj.id 
                    )
                    session.add(recurso)
                else:
                    print(f"no se encontro al profesor '{fila['profesor']}'")
        
        session.commit()
        print("Recursos academicos ingresados exitosamente")
    except Exception as e:
        session.rollback()
        print(f"Error al poblar recursos: {e}")
    finally:
        session.close()

if __name__ == "__main__":
    poblar_recursos()
