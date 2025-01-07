class MiArchivo:
    def __init__(self,nombre):
        self.nombre = nombre
    
    def __escribir(self, texto):
        with open(self.nombre,"w") as archivo:
            archivo.write(texto)
    
    def leer(self):
        with open(self.nombre, "r") as archivo:
            return archivo.read()
    
    def product_parse(self) -> list:
        products = self.leer().split("\n")[:-1]
        product_info = []
        for p in products:
            product_info.append(p.split(","))
        
        return product_info

    def eliminar_producto(self, product_name:str) -> None:
        new_catalog = []

        for name,price in self.product_parse():
            if product_name == name:
                continue
            new_catalog.append(f"{name},{price}\n")
        
        self.__escribir("".join(new_catalog))

    def modificar_producto(self, product_name:str,new_price:float) -> None:
        modified_catalog = []

        for name,price in self.product_parse():
            if product_name == name:
                price = new_price
            modified_catalog.append(f"{name},{float(price)}\n")
        
        self.__escribir("".join(modified_catalog))

    def nuevo_producto(self,nombre:str,precio:float) -> None:
        try:
            self.__escribir(f"{self.leer()}{nombre},{precio:.2f}\n")
            print(f"AGREGANDO PRODUCTO: {nombre}: {precio:.2f}")
        except FileNotFoundError:
            print(f"CREANDO CATALOGO: {self.nombre}\nAGREGANDO PRODUCTO: {nombre}: {precio}")
            self.__escribir("")
            self.__escribir(f"{self.leer()}{nombre},{precio:.2f}\n")

mi_archivo = MiArchivo("mi_archivo.txt")

## carga rapida datos test
# mock = {"Melon": 3455.00,
#               "Sandia": 3288.00,
#               "Manzanas": 3200.00,
#               "Tomates": 3300.00}
# for nombre,precio in mock.items(): mi_archivo.nuevo_producto(nombre,precio)

while True:
    menu = input("Menu de opciones:\n1. Agregar producto\n2. Eliminar producto\n3. Modificar Precio de productos\n4. Mostrar productos\n5. Salir\nSeleccione una opcion: ")
    match menu:
        case "1": 
            try:
                nombre = input("nombre del producto: ")
                precio = float(input("precio del producto: "))
                mi_archivo.nuevo_producto(nombre,precio)
            except: print("OCURRIO UN ERROR INTENTA DENUEVO"); continue
        case "2": mi_archivo.eliminar_producto(input("nombre del producto: "))
        case "3":
            try:
                nombre = input("nombre del producto: ")
                nuevo_precio = float(input("nuevo precio del producto: "))
                mi_archivo.modificar_producto(nombre,nuevo_precio)
            except: print("OCURRIO UN ERROR INTENTA DENUEVO"); continue
        case "4":
            try:
                print(mi_archivo.leer())
            except: print("PRIMERO CREA UN CATALGO!")
        case "5": print("chau, cuidate!");break
        case _: print("\n\ningresa una opcion valida!!"); continue