#Alejandro Daniel de León González 
#Activida 9 
#Biblioteca Virtual + Git y GitHub


biblioteca = []

def agregar_libros(*titulos):
    for titulo in titulos:
        libro = {
            "titulo": titulo,
            "autor": None,
            "genero": None,
            "año": None
        }
        biblioteca.append(libro)

def asignar_detalles(titulo, autor, genero, año):
    for libro in biblioteca:
        if libro["titulo"] == titulo:
            libro["autor"] = autor
            libro["genero"] = genero
            libro["año"] = año
            return
    print(f"No se encontró el libro: '{titulo}'.")

def mostrar_biblioteca():
    if not biblioteca:
        print("La biblioteca está vacía.")
    else:
        for libro in biblioteca:
            print(f"Título: {libro['titulo']}, Autor: {libro['autor']}, Género: {libro['genero']}, Año: {libro['año']}")

def buscar_libros(**filtros):
    resultados = biblioteca
    if "genero" in filtros:
        resultados = [libro for libro in resultados if libro["genero"] == filtros["genero"]]
    if "autor" in filtros:
        resultados = [libro for libro in resultados if libro["autor"] == filtros["autor"]]
    if "año_max" in filtros:
        resultados = [libro for libro in resultados if libro["año"] is not None and libro["año"] <= filtros["año_max"]]

    if resultados:
        for libro in resultados:
            print(f"Título: {libro['titulo']}, Autor: {libro['autor']}, Género: {libro['genero']}, Año: {libro['año']}")
    else:
        print("No se encontraron libros que coincidan con los filtros.")

agregar_libros("1984", "Rayuela", "Los juegos del hambre")
asignar_detalles("1984", "George Orwell", "Distopía", 1949)
asignar_detalles("Rayuela", "Julio Cortázar", "Realismo mágico", 1963)
asignar_detalles("Los juegos del hambre", "Suzanne Collins", "Ciencia ficción", 2008)


buscar_libros(autor="Julio Cortázar")
buscar_libros(año_max=1970)
buscar_libros(genero="Distopía")
buscar_libros(genero="Ciencia ficción", año_max=2010)
