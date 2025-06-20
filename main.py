#importamos el framework fastapi a nuestro entorno 
from fastapi import FastAPI, HTTPException

#creamos un objeto a partir de la clase FastAPI
app= FastAPI()
#utilizamos la instacion funcion get del framework FastAPI
@app.get("/imprimir")
#creamos la funcion asincrona "imprimir"
async def imprimir():
        return "HOLA ESTUDIANTES"

#creamos la funcion asincrona con formato JSON 
@app.get("/Git")
async def imprimir():
    return {"Git_curso": "https://github.com/AndMargarita2?tab=repositories"}

#Documentacion con swagger

from pydantic import BaseModel
#creamos nuestra lista de entidades con los siguientes atributos
#{"id": 3, "Name": Andrea, "LastName": Maldonado, "Age": 23}
class User(BaseModel):
    id: int
    Name: str
    LastName: str
    Age: int

#creamos un objeto en forma de lista con difererntes usuarios
users_list = [
    User(id=1, Name="Andrea", LastName="Maldonado", Age=23),
    User(id=2, Name="Juan", LastName="Pérez", Age=30),
    User(id=3, Name="María", LastName="Gómez", Age=25),
]
#--get("/users")
@app.get("/usersclass/")
async def usersclass():
    return (users_list)

#ACT. clase 18/06/2025
@app.get("/usersclass/user_id/{id}")
async def usersclass(id:int):
    users=filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No se ha encontrado el usuario"}

#----ACTIVIDAD 01------

from typing import List
import pandas as pd

# Definir el modelo Alumno para los datos del Excel
class Alumno(BaseModel):
    Nombre: str
    Matricula: int
    Edad: int
    Facultad: str
    Grado: str
    Carrera: str
    Genero: str
    Correo: str
    Promedio: float
    Semestre: int

# Cargar los datos del CSV al iniciar la app
try:
    df = pd.read_csv('registros.csv')
    alumnos_excel = [Alumno(**row) for row in df.to_dict(orient='records')]
except Exception as e:
    alumnos_excel = []
    print(f"Error al cargar el archivo CSV: {e}")


# Endpoint: /alumno/edad/genero
#@app.get("/alumno/{Edad}/{Genero}", response_model=List[Alumno])
#async def get_alumnos_by_edad_genero(Edad: int, Genero: str):
#    result = [alumno for alumno in alumnos_excel if alumno.Edad == Edad and alumno.Genero.lower() == Genero.lower()]
#    if not result:
#       raise HTTPException(status_code=404, detail="No se encontraron alumnos con esa edad y género")
#    return result

# Endpoint: /alumno/facultad/carrera/semestre
#@app.get("/alumno/{Facultad}/{Carrera}/{Semestre}", response_model=List[Alumno])
#async def get_alumnos_by_facultad_carrera_semestre(Facultad: str, Carrera: str, Semestre: int):
#    print(f"Facultad recibida: '{Facultad}'")
#    print(f"Carrera recibida: '{Carrera}'")
#    print(f"Semestre recibido: '{Semestre}'")
#    for alumno in alumnos_excel:
#        print(f"Facultad en datos: '{alumno.Facultad}' | Carrera en datos: '{alumno.Carrera}' | Semestre en datos: '{alumno.Semestre}'")
#    result = [alumno for alumno in alumnos_excel if alumno.Facultad.lower() == Facultad.lower() and alumno.Carrera.lower() == Carrera.lower() and alumno.Semestre == Semestre]
#    if not result:
#        raise HTTPException(status_code=404, detail="No se encontraron alumnos con esa facultad, carrera y semestre")
#    return result

# Endpoint: /semestre/promedio/matricula
#@app.get("/semestre/{Semestre}/{Promedio}/{Matricula}", response_model=List[Alumno])
#async def get_alumnos_by_semestre_promedio_matricula(Semestre: int, Promedio: float, Matricula: int):
#    result = [
#        alumno for alumno in alumnos_excel
#        if int(alumno.Semestre) == int(Semestre)
#        and abs(float(alumno.Promedio) - float(Promedio)) < 0.01
#        and int(alumno.Matricula) == int(Matricula)
#    ]
#    if not result:
#        raise HTTPException(status_code=404, detail="No se encontraron alumnos con ese semestre, promedio y matrícula")
#    return result


#----ACTIVIDAD 02 ENDPOINTS POR QUERY------

@app.get("/alumnos")
async def listar_alumnos():
    alumnos = filter(lambda a: True, alumnos_excel)  # Devuelve todos los alumnos
    try:
        return list(alumnos)
    except:
        return {"error": "No se encontraron alumnos"}

@app.get("/alumno/matricula")
async def alumno_by_matricula(Matricula: int):
    alumnos = filter(lambda a: int(a.Matricula) == int(Matricula), alumnos_excel)
    try:
        return list(alumnos)
    except:
        return {"error": "No se ha encontrado el alumno con esa matrícula"}

@app.get("/alumno/nombre")
async def alumno_by_nombre(Nombre: str):
    alumnos = filter(lambda a: a.Nombre.lower() == Nombre.lower(), alumnos_excel)
    try:
        return list(alumnos)
    except:
        return {"error": "No se ha encontrado el alumno con ese nombre"}

@app.get("/alumno/edad")
async def alumno_by_edad(Edad: int):
    alumnos = filter(lambda a: int(a.Edad) == int(Edad), alumnos_excel)
    try:
        return list(alumnos)
    except:
        return {"error": "No se ha encontrado el alumno con esa edad"}

@app.get("/alumno/facultad")
async def alumno_by_facultad(Facultad: str):
    alumnos = filter(lambda a: a.Facultad.lower() == Facultad.lower(), alumnos_excel)
    try:
        return list(alumnos)
    except:
        return {"error": "No se ha encontrado el alumno con esa facultad"}

@app.get("/alumno/carrera")
async def alumno_by_carrera(Carrera: str):
    alumnos = filter(lambda a: a.Carrera.lower() == Carrera.lower(), alumnos_excel)
    try:
        return list(alumnos)
    except:
        return {"error": "No se ha encontrado el alumno con esa carrera"}

@app.get("/alumno/genero")
async def alumno_by_genero(Genero: str):
    alumnos = filter(lambda a: a.Genero.lower() == Genero.lower(), alumnos_excel)
    try:
        return list(alumnos)
    except:
        return {"error": "No se ha encontrado el alumno con ese género"}

@app.get("/alumno/promedio")
async def alumno_by_promedio(Promedio: float):
    alumnos = filter(lambda a: abs(float(a.Promedio) - float(Promedio)) < 0.01, alumnos_excel)
    try:
        return list(alumnos)
    except:
        return {"error": "No se ha encontrado el alumno con ese promedio"}

@app.get("/alumno/semestre")
async def alumno_by_semestre(Semestre: int):
    alumnos = filter(lambda a: int(a.Semestre) == int(Semestre), alumnos_excel)
    try:
        return list(alumnos)
    except:
        return {"error": "No se ha encontrado el alumno con ese semestre"}

@app.get("/alumno/facultad_carrera")
async def alumno_by_facultad_carrera(Facultad: str, Carrera: str):
    alumnos = filter(lambda a: a.Facultad.lower() == Facultad.lower() and a.Carrera.lower() == Carrera.lower(), alumnos_excel)
    try:
        return list(alumnos)
    except:
        return {"error": "No se ha encontrado el alumno con esa facultad y carrera"}

@app.get("/alumno/edad_genero")
async def alumno_by_edad_genero(Edad: int, Genero: str):
    alumnos = filter(lambda a: int(a.Edad) == int(Edad) and a.Genero.lower() == Genero.lower(), alumnos_excel)
    try:
        return list(alumnos)
    except:
        return {"error": "No se ha encontrado el alumno con esa edad y género"}



#levantamos el server Uvicornuvicorn main:app --reload
#con uvicorn main:app --reload

#http..... /imprimir
