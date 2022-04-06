from classroom.asignatura import Asignatura
from classroom.asignatura import Asignatura


class Grupo:

    grado = "Grado 12"

    def __init__(self, grupo="grupo predeterminado", asignaturas=None, estudiantes=None):
        if(estudiantes is None):
            estudiantes = []

        if(asignaturas is None):
            asignaturas = []    

        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = estudiantes

    def listadoAsignaturas(self, **kwargs):
        for x in kwargs.values():
            self._asignaturas.append(Asignatura(x))

    def agregarAlumno(self, alumno, lista=None):
        if(lista is None):
            lista = []
            lista.append(alumno)
            self.listadoAlumnos = self.listadoAlumnos + lista
        else:
            self.listadoAlumnos = self.listadoAlumnos + lista + [alumno]


    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre    

    def __str__(self) -> str:
        return "Grupo de estudiantes: " + self._grupo   