"""
Módulo que contiene la definición de la clase SensorTermico.
Bajo acoplamiento: no incluye interacciones de consola (ni print ni input).
"""

class SensorTermico:
    """
    Clase que representa un sensor térmico encargado de monitorear 
    las temperaturas de servidores.
    """

    def __init__(self, id_sensor: str, ubicacion: str) -> None:
        self.id_sensor: str = id_sensor
        self.ubicacion: str = ubicacion
        self.__temperaturas: list[float] = []

    @property
    def temperaturas(self) -> list[float]:
        return self.__temperaturas[:]

    def agregar_lectura(self, temp: float) -> bool:
        if 0.0 <= temp <= 85.0:
            self.__temperaturas.append(temp)
            return True
        return False

    def obtener_promedio(self) -> float:
        if not self.__temperaturas:
            return 0.0
        return sum(self.__temperaturas) / len(self.__temperaturas)

    def obtener_maxima(self) -> float:
        try:
            return max(self.__temperaturas)
        except ValueError:
            return 0.0

    def alerta_sobrecalentamiento(self, umbral: float) -> bool:
        if not self.__temperaturas:
            return False
        return self.__temperaturas[-1] > umbral
