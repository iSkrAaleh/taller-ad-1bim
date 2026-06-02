import json
from configuracion import SessionLocal
from crear_base_entidades import Carrera, Facultad

def poblar_carreras():
    session = SessionLocal()
    ruta = 'data/datos_universidad/datos/carreras.json'
    try:
        with open(ruta, 'r', encoding='utf-8') as archivo:
            datos = json.load(archivo)
            
            for fila in datos:
                facultad_obj = session.query(Facultad).filter_by(nombre=fila['facultad']).first()
                
                if facultad_obj:
                    carrera = Carrera(
                        nombre=fila['nombre'],
                        codigo=fila['codigo'],
                        facultad_id=facultad_obj.id                     )
                    session.add(carrera)
                else:
                    print(f"no se encontro la facultad '{fila['facultad']}'")
        
        session.commit()
        print("carreras ingresadas exitosamente")
    except Exception as e:
        session.rollback()
        print(f"Error al poblar carreras: {e}")
    finally:
        session.close()

if __name__ == "__main__":
    poblar_carreras()
