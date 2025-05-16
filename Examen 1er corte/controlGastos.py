class ControlGastos:
    def __init__(self):
        self.categorias = []
        self.gastos = []

    def agregarCategoria(self, categoria):
        if categoria not in self.categorias:
            self.categorias.append(categoria)
            print("Categoría agregada exitosamente!")
        else:
            print("La categoría ya existe.")
    
    def mostrarCategoria(self):
        if not self.categorias:
            print("No hay categoías registradas.")
        else:
            print("Categorías registradas: ")
            for catego in self.categorias:
                print("-", catego)
    
    def agregarGasto(self, fecha, categoria, monto, descripcion):
        if categoria in self.categorias:
            self.gastos.append([fecha, categoria, monto, descripcion])
            print("El gasto ha sido registrado!")
        else:
            print("Categoría no registrada.")
    
    def listarGastos(self):
        if not self.gastos:
            print("No hay gastos.")
        else:
            for g in self.gastos:
                print(f"{g[0]} - {g[1]} - C${g[2]} - {g[3]}")

    def total_gastos(self):
        total = 0
        for g in self.gastos:
            total += g[2]
        print(f"Total gastado: C${total:.2f}")

    def totalPorCategoria(self):
        for catego in self.categorias:
            total = 0
            for g in self.gastos:
                if g[1] == catego:
                    total += g[2]
            print(f"{catego}: C${total:.2f}")
    
    def promedioPorCategoria(self):
        for catego in self.categorias:
            total = 0
            cantidad = 0
            for g in self.gastos:
                if g[1] == catego:
                    total += g[2]
                    cantidad += 1
            if cantidad > 0:
                promedio = total / cantidad
                print(f"{catego}: promedio C${promedio:.2f}")
            else:
                print(f"{catego}: sin gastos")
                