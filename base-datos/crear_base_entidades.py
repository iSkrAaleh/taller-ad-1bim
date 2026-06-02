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

    def __repr__(self):
        return f"<Facultad(id={self.id}, nombre='{self.nombre}', ubicacion='{self.ubicacion}', decano='{self.decano}')>"

class Carrera(Base):
    __tablename__ = 'carreras'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(150), nullable=False)
    codigo = Column(String(50), nullable=False, unique=True)
    facultad_id = Column(Integer, ForeignKey('facultades.id'), nullable=False)
    facultad = relationship("Facultad", back_populates="carreras")
    profesores = relationship("Profesor", back_populates="carrera")

    def __repr__(self):
        return f"<Carrera(id={self.id}, nombre='{self.nombre}', codigo='{self.codigo}', facultad_id={self.facultad_id})>"

class Profesor(Base):
    __tablename__ = 'profesores'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombres_apellidos = Column(String(150), nullable=False)
    correo = Column(String(100), nullable=False, unique=True)
    especialidad = Column(String(100), nullable=False)
    carrera_id = Column(Integer, ForeignKey('carreras.id'), nullable=False)
    carrera = relationship("Carrera", back_populates="profesores")
    recursos = relationship("RecursoAcademico", back_populates="profesor")

    def __repr__(self):
        return f"<Profesor(id={self.id}, nombre='{self.nombres_apellidos}', correo='{self.correo}', especialidad='{self.especialidad}')>"

class RecursoAcademico(Base):
    __tablename__ = 'recursos_academicos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(200), nullable=False)
    fecha_publicacion = Column(Date, nullable=False)
    tipo_recurso = Column(String(50), nullable=False)
    url = Column(String(250), nullable=False)
    profesor_id = Column(Integer, ForeignKey('profesores.id'), nullable=False)
    profesor = relationship("Profesor", back_populates="recursos")

    def __repr__(self):
        return f"<Recurso(id={self.id}, titulo='{self.titulo}', tipo='{self.tipo_recurso}', fecha='{self.fecha_publicacion}')>"

if __name__ == "__main__":
    # generacion de tablas
    Base.metadata.create_all(bind=engine)
    print("tablas creadas exitosamente")
