# Actividad2_GETporPATHyQUERY

@app.get("/alumnos")
parametros

respuesta:
  {
    "Nombre": "MALDONADO MORALES, ANDREA M.",
    "Matricula": 202233003,
    "Edad": 23,
    "Facultad": "Ciencias de la computación",
    "Grado": "Licenciatura",
    "Carrera": "Ing. Ciencias Computación",
    "Genero": "Femenino",
    "Correo": "andrea.maldonado@alumno.buap.mx",
    "Promedio": 8.3,
    "Semestre": 6
  },


@app.get("/alumno/matricula")
parametros:
matricula(int)

respuesta: 
[
  {
    "Nombre": "MALDONADO MORALES, ANDREA M.",
    "Matricula": 202233003,
    "Edad": 23,
    "Facultad": "Ciencias de la computación",
    "Grado": "Licenciatura",
    "Carrera": "Ing. Ciencias Computación",
    "Genero": "Femenino",
    "Correo": "andrea.maldonado@alumno.buap.mx",
    "Promedio": 8.3,
    "Semestre": 6
  }
]

@app.get("/alumno/nombre")
parametros:
Nombre(string)

respuesta:
  {
    "Nombre": "MALDONADO MORALES, ANDREA M.",
    "Matricula": 202233003,
    "Edad": 23,
    "Facultad": "Ciencias de la computación",
    "Grado": "Licenciatura",
    "Carrera": "Ing. Ciencias Computación",
    "Genero": "Femenino",
    "Correo": "andrea.maldonado@alumno.buap.mx",
    "Promedio": 8.3,
    "Semestre": 6
  }

@app.get("/alumno/edad")
parametros
Edad(int)

respuesta:
  {
    "Nombre": "MALDONADO MORALES, ANDREA M.",
    "Matricula": 202233003,
    "Edad": 23,
    "Facultad": "Ciencias de la computación",
    "Grado": "Licenciatura",
    "Carrera": "Ing. Ciencias Computación",
    "Genero": "Femenino",
    "Correo": "andrea.maldonado@alumno.buap.mx",
    "Promedio": 8.3,
    "Semestre": 6
  }

  @app.get("/alumno/facultad")
  parametros:
  Faculatad(string)

  respuesta:
  {
    "Nombre": "MALDONADO MORALES, ANDREA M.",
    "Matricula": 202233003,
    "Edad": 23,
    "Facultad": "Ciencias de la computación",
    "Grado": "Licenciatura",
    "Carrera": "Ing. Ciencias Computación",
    "Genero": "Femenino",
    "Correo": "andrea.maldonado@alumno.buap.mx",
    "Promedio": 8.3,
    "Semestre": 6
  }

@app.get("/alumno/carrera")
parametros:
Carrera(string)

respuesta:
 {
    "Nombre": "MALDONADO MORALES, ANDREA M.",
    "Matricula": 202233003,
    "Edad": 23,
    "Facultad": "Ciencias de la computación",
    "Grado": "Licenciatura",
    "Carrera": "Ing. Ciencias Computación",
    "Genero": "Femenino",
    "Correo": "andrea.maldonado@alumno.buap.mx",
    "Promedio": 8.3,
    "Semestre": 6
  }

  @app.get("/alumno/genero")
  parametros: 
  Genero(string)

  respuesta:
   {
    "Nombre": "MALDONADO MORALES, ANDREA M.",
    "Matricula": 202233003,
    "Edad": 23,
    "Facultad": "Ciencias de la computación",
    "Grado": "Licenciatura",
    "Carrera": "Ing. Ciencias Computación",
    "Genero": "Femenino",
    "Correo": "andrea.maldonado@alumno.buap.mx",
    "Promedio": 8.3,
    "Semestre": 6
  }

  @app.get("/alumno/promedio")
  parametros:
  Promedio(float)

  respuesta:
    {
    "Nombre": "MALDONADO MORALES, ANDREA M.",
    "Matricula": 202233003,
    "Edad": 23,
    "Facultad": "Ciencias de la computación",
    "Grado": "Licenciatura",
    "Carrera": "Ing. Ciencias Computación",
    "Genero": "Femenino",
    "Correo": "andrea.maldonado@alumno.buap.mx",
    "Promedio": 8.3,
    "Semestre": 6
  }

  @app.get("/alumno/semestre")
  parametros:
  Semestre(int)

  respuesta:
     {
    "Nombre": "MALDONADO MORALES, ANDREA M.",
    "Matricula": 202233003,
    "Edad": 23,
    "Facultad": "Ciencias de la computación",
    "Grado": "Licenciatura",
    "Carrera": "Ing. Ciencias Computación",
    "Genero": "Femenino",
    "Correo": "andrea.maldonado@alumno.buap.mx",
    "Promedio": 8.3,
    "Semestre": 6
  }

  @app.get("/alumno/facultad_carrera")
  parametros:
  Facultad(string)
  Carrera(string)

  respuesta:
      {
    "Nombre": "MALDONADO MORALES, ANDREA M.",
    "Matricula": 202233003,
    "Edad": 23,
    "Facultad": "Ciencias de la computación",
    "Grado": "Licenciatura",
    "Carrera": "Ing. Ciencias Computación",
    "Genero": "Femenino",
    "Correo": "andrea.maldonado@alumno.buap.mx",
    "Promedio": 8.3,
    "Semestre": 6
    }

  @app.get("/alumno/edad_genero")
  parametros: 
  Edad(int)
  Genero(string)

  respuesta:
    {
    "Nombre": "MALDONADO MORALES, ANDREA M.",
    "Matricula": 202233003,
    "Edad": 23,
    "Facultad": "Ciencias de la computación",
    "Grado": "Licenciatura",
    "Carrera": "Ing. Ciencias Computación",
    "Genero": "Femenino",
    "Correo": "andrea.maldonado@alumno.buap.mx",
    "Promedio": 8.3,
    "Semestre": 6
    }
