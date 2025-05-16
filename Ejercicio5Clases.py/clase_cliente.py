'''Ejercicio #5: Procesamiento de pedidos y clientes
Crear una clase Cliente con atributos básicos (por ejemplo, ID, nombre y 
contacto) y una clase Pedido que contenga información sobre el cliente, la lista 
de productos solicitados y el total de la venta. Se podrá incluir el uso de herencia 
para diferenciar entre tipos de clientes (por ejemplo, cliente regular y cliente VIP) 
y aplicar descuentos especiales, demostrando el uso de la herencia y el 
polimorfismo para adaptar el comportamiento de los objetos según el tipo de 
cliente.'''

class Cliente:
    def __init__(self, ID, nombre, contacto, tipo):
        self.ID = ID
        self.nombre = nombre
        self.contacto = contacto
        self.tipo = tipo

    def aplicarDescuento (self, total):
        if self.tipo == "vip":
            return total * 0.15
        else:
            return 0
    
    def __str__(self):
        return (f"{self.nombre} (ID: {self.ID}, Tipo: {self.tipo.upper()})\n" f"Contacto: {self.contacto}")

class Pedido(Cliente):
    def __init__(self, cliente):
        self.cliente = cliente
        self.productos = []

    def agregarProducto(self, nombre, precio):
        self.productos.append({"nombre": nombre, "precio": precio})

    def calcularTotal (self):
        subtotal = sum(p["precio"] for p in self.productos)
        descuento = self.cliente.aplicarDescuento(subtotal)
        total = subtotal - descuento
        return total, descuento
    
    def mostrarResumen(self):
        print(f"Cliente: {self.cliente}")
        print("Productos comprados:")
        
        for p in self.productos:
            print(f" - {p['nombre']}: C${p['precio']:.2f}")
        
        total, descuento = self.calcularTotal()
        print (f"Descuento aplicado: C${descuento:.2f}")
        print(f"Total final: C${total:.2f}\n")

if __name__ == "__main__":
   cliente1 = Cliente(1, "Valeria Grijalva", 89937002, "regular")
   cliente2 = Cliente(2, "Manuel Chamorro", 89421920, "vip")
   
   pedido1 = Pedido(cliente1)
   pedido1.agregarProducto("Teléfono Celular", 2000)
   pedido1.agregarProducto("Cornflake", 100)
   
   pedido2 = Pedido(cliente2)
   pedido2.agregarProducto("Pan", 200)
   pedido2.agregarProducto("Gaseosa", 150)
   
   print("\nPEDIDO 1:")
   pedido1.mostrarResumen()
   print("-------------------------\n")
   
   print("PEDIDO 2:")
   pedido2.mostrarResumen()