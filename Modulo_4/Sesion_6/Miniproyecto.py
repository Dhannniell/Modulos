"""Walter necesita llevar una app de control, donde registrar las actividades de sus empleados. Hay 4 estados: Volando, Descansando, Disponible y No Disponible.
Tiene 3 rutas; Ruta 1 - 100.000, Ruta 2 - 150.000, y Ruta  - 200.000  """

from abc import ABC, abstractmethod

class EstadoEmpleado(ABC):
    @abstractmethod
    def obtener_estado(self):
        pass
    
class Volando(EstadoEmpleado):
    def obtener_estado(self):
        return "Volando"
    
class Descansando(EstadoEmpleado):
    def obtener_estado(self):
        return "Descansando"
    
class Disponible(EstadoEmpleado):
    def obtener_estado(self):
        return "Disponible"
    
class NoDisponible(EstadoEmpleado):
    def obtener_estado(self):
        return "NoDisponible"
    

    
class Ruta(ABC):
    @abstractmethod
    def obtener_costo(self):
        pass
    
class RutaEconomica(Ruta):
    def obtener_costo(self):
        return 100
    
class RutaPremium(Ruta):
    def obtener_costo(self):
        return 150
    
class RutaExtraPremium(Ruta):
    def obtener_costo(self):
        return 200

class Empleado:
    def __init__(self, nombre, estado: EstadoEmpleado):
        self.nombre = nombre
        self.estado = estado
        self.historial = []

    def cambiar_estado(self, nuevo_estado: EstadoEmpleado):
        self.estado = nuevo_estado
        
    def obtener_info(self):
        return f"Empleado: {self.nombre} Estado: {self.estado.obtener_estado()}"
    
    def asignar_ruta(self, ruta: Ruta):
        if isinstance(self.estado, Disponible):
            self.estado = Volando()
            self.historial.append(f"Ruta Asignada: {type(ruta).__name__}")
            print(f"{self.nombre} ha sido asignado a la ruta {type(ruta).__name__}")
    
class ControlRutas:
    def __init__(self, rutas: list[Ruta]):
        self.rutas = {type(ruta).__name__: ruta for ruta in rutas}
        
    def obtener_precio_ruta(self, nombre_ruta: str):
        ruta = self.rutas.get(nombre_ruta)
        
        if ruta:
            return ruta.obtener_costo()
        else:
            raise ValueError("Error ruta no existe")
        
class ControlEmpleados:
    def __init__(self):
        self.empleados = []
        
    def agregar_empleados(self, empleado: Empleado):
        self.empleados.append(empleado)
        
    def lista_empleados(self):
        for empleado in self.empleados:
            print(empleado.obtener_info())
            
    def cambiar_estado_empleado(self, nombre:str, nuevo_estado: EstadoEmpleado):
        for empleado in self.empleados:
            if empleado.nombre == nombre:
                empleado.cambiar_estado(nuevo_estado)
                print(f"Estado de {nombre} cambiado a {nuevo_estado.obtener_estado()}")
                return
        print(f"No se encontro empleado con ese nombre")
        
    def asignar_ruta_a_empleado(self, nombre:str, ruta: Ruta):
        for empleado in self.empleados:
            if empleado.nombre == nombre:
                empleado.asignar_ruta(ruta)
                return
        print(f"No se encontro empleado con ese nombre")

empleado1 = Empleado("Walter", Disponible())
empleado2 = Empleado("Pedro", Disponible())
control_empleados = ControlEmpleados()
control_empleados.agregar_empleados(empleado1)
control_empleados.agregar_empleados(empleado2)
ruta_economica = RutaEconomica()

control_empleados.lista_empleados()
control_rutas = ControlRutas([ruta_economica])
print(control_rutas.obtener_precio_ruta("RutaEconomica"))

control_empleados.cambiar_estado_empleado("Walter", Volando())
control_empleados.lista_empleados()

control_empleados.asignar_ruta_a_empleado("Pedro",RutaEconomica())