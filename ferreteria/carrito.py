class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
           carrito = self.session["carrito"] = {}
        self.carrito = carrito
    
    def agregar(self, producto):
        id = str(producto.id)
        if id not in self.carrito.keys():
            self.carrito[id] = {
                'producto_id': producto.id,
                'nombre_producto': producto.nombre,
                'acumulado': producto.precio,
                'cantidad': 1,   
            }
        else:
            self.carrito[id]["cantidad"] +=1
            self.carrito[id]["acumulado"] += producto.precio
        self.save

    def save(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True 

    def remove(self, producto):
        id = str(producto.id)
        if id in self.carrito:
            del self.carrito[id]
            self.save()
    
    def decrement(self, producto):
        id = str(producto.id)
        if id in self.carrito.keys():
                self.carrito[id]["cantidad"] -= 1
                self.carrito[id]["acumulado"] -= producto.precio
                if self.carrito[id]["cantidad"] <= 0: self.remove(producto)
                self.save()

    def clear(self):
        self.session["carrito"] = {}
        self.session.modified = True



