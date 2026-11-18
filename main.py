"""
Módulo principal que gestiona la Interfaz de Consola.
Contiene todas las interacciones interactivas con el usuario.
"""
import os
import sys

# Asegura que Python siempre encuentre la carpeta raíz del proyecto
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from ub_monitoreo.sensor import SensorTermico


def main() -> None:
    print("--- Configuración Inicial del Sensor ---")
    id_sensor = input("Ingrese el ID del sensor (ej. SENS-01): ")
    ubicacion = input("Ingrese la ubicación (ej. Rack A-4): ")

    sensor = SensorTermico(id_sensor, ubicacion)
    print(f"\n¡Sensor '{sensor.id_sensor}' creado exitosamente en '{sensor.ubicacion}'!")

    while True:
        print("\n" + "=" * 30)
        print(" Menú del Sensor Térmico")
        print("=" * 30)
        print("1. Agregar lectura de temperatura")
        print("2. Ver todas las temperaturas registradas")
        print("3. Obtener promedio histórico")
        print("4. Obtener temperatura máxima")
        print("5. Verificar alerta de sobrecalentamiento")
        print("6. Salir")

        opcion = input("Seleccione una opción (1-6): ")

        if opcion == '1':
            try:
                temp = float(input("Ingrese la temperatura en °C: "))
                if sensor.agregar_lectura(temp):
                    print("Lectura agregada correctamente.")
                else:
                    print("Error: Temperatura descartada. Debe estar entre 0 °C y 85 °C.")
            except ValueError:
                print("Error: Por favor, ingrese un número válido.")

        elif opcion == '2':
            temps = sensor.temperaturas
            if temps:
                print(f"Temperaturas registradas: {temps}")
            else:
                print("No hay temperaturas registradas aún.")

        elif opcion == '3':
            promedio = sensor.obtener_promedio()
            print(f"Promedio histórico: {promedio:.2f} °C")

        elif opcion == '4':
            maxima = sensor.obtener_maxima()
            if maxima == 0.0 and not sensor.temperaturas:
                print("No hay lecturas para calcular la máxima.")
            else:
                print(f"Temperatura máxima registrada: {maxima:.2f} °C")

        elif opcion == '5':
            try:
                umbral = float(input("Ingrese el umbral de alerta en °C: "))
                if not sensor.temperaturas:
                    print("No hay lecturas registradas para evaluar.")
                elif sensor.alerta_sobrecalentamiento(umbral):
                    print(f"¡ALERTA! La última lectura superó el umbral de {umbral} °C.")
                else:
                    print("Estado normal. La última lectura está por debajo o igual al umbral.")
            except ValueError:
                print("Error: Por favor, ingrese un número válido.")

        elif opcion == '6':
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida. Intente de nuevo.")


if __name__ == '__main__':
    main()