class MiArchivo:
    def __init__(self,nombre):
        self.nombre = nombre
    
    def escribir(self, texto):
        with open(self.nombre,"w") as archivo:
            archivo.write(texto)
    
    def leer(self):
        with open(self.nombre, "r") as archivo:
            return archivo.read()

mi_archivo = MiArchivo("mi_archivo.txt")

mi_archivo.escribir("Hola, Estudiantes!")

print(MiArchivo.leer())