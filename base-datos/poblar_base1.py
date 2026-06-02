import json
from configuracion import SessionLocal
from crear_base_entidades import Facultad

def poblar_facultades():
    session = SessionLocal()
    ruta = 'data/datos_universidad/datos/facultades.json'
    
    try:
        with open(ruta, 'r', encoding='utf-8') as archivo:
            datos = json.load(archivo)
            
            for fila in datos:
                facultad = Facultad(
                    nombre=fila['nombre'],
                    ubicacion=fila['ubicacion'],
                    decano=fila['decano']
                )
                session.add(facultad)
        
        session.commit()
        print("facultades ingresadas exitosamente")
    except Exception as e:
        session.rollback()
        print(f"Error al poblar facultades: {e}")
    finally:
        session.close()

if __name__ == "__main__":
    poblar_facultades()
