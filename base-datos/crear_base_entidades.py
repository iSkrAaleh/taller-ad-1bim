from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from configuracion import Base, engine

class Facultad(Base):
    __tablename__ = 'facultades'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(150), nullable=False, unique=True)
    ubicacion = Column(String(150), nullable=False)
    decano = Column(String(100), nullable=False)
    
    carreras = relationship("Carrera", back_populates="facultad")

class Carrera(Base):
    __tablename__ = 'carreras'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(150), nullable=False)
    codigo = Column(String(50), nullable=False, unique=True)
    facultad_id = Column(Integer, ForeignKey('facultades.id'), nullable=False)
    
    facultad = relationship("Facultad", back_populates="carreras")
    profesores = relationship("Profesor", back_populates="carrera")

class Profesor(Base):
    __tablename__ = 'profesores'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombres_apellidos = Column(String(150), nullable=False)
    correo = Column(String(100), nullable=False, unique=True)
    especialidad = Column(String(100), nullable=False)
    carrera_id = Column(Integer, ForeignKey('carreras.id'), nullable=False)
    
    carrera = relationship("Carrera", back_populates="profesores")
    recursos = relationship("RecursoAcademico", back_populates="profesor")

class RecursoAcademico(Base):
    __tablename__ = 'recursos_academicos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(200), nullable=False)
    fecha_publicacion = Column(Date, nullable=False)
    tipo_recurso = Column(String(50), nullable=False)
    url = Column(String(250), nullable=False)
    profesor_id = Column(Integer, ForeignKey('profesores.id'), nullable=False)
    
    profesor = relationship("Profesor", back_populates="recursos")

if __name__ == "__main__":
#generacion de tablas
    Base.metadata.create_all(bind=engine)
    print("tablas creadas exitosamente")
