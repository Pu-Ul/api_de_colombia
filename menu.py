import requests


def info_colombia():
    res = requests.get("https://api-colombia.com/api/v1/Country/Colombia")
    if res.status_code == 200:
        d = res.json()
        print(
            f"\n--- INFORMACIÓN GENERAL ---\nNombre: {d.get('name')}\nDescripción: {d.get('description')}\nMoneda: {d.get('currencyCode')}"
        )


def info_departamentos():
    res = requests.get("https://api-colombia.com/api/v1/Department")
    if res.status_code == 200:
        for dep in res.json():
            cap = dep.get("city") or dep.get("capital") or {}
            print(
                f"\n--- {dep.get('name')} ---\nDescripción: {dep.get('description')}\nCapital: {cap.get('name', 'N/A')}\nDesc. Capital: {cap.get('description', 'N/A')}"
            )


def info_regiones():
    res = requests.get("https://api-colombia.com/api/v1/Region")
    if res.status_code == 200:
        for reg in res.json():
            print(
                f"\n--- {reg.get('name')} ---\nDescripción: {reg.get('description')}"
            )


def info_atracciones():
    res = requests.get("https://api-colombia.com/api/v1/TouristicAttraction")
    if res.status_code == 200:
        for atr in res.json():
            ciu = atr.get("city") or {}
            print(
                f"\n--- {atr.get('name')} ---\nDescripción: {atr.get('description')}\nCiudad: {ciu.get('name', 'N/A')}"
            )


def menu():
    while True:
        print("\n=== MENÚ DE CONSULTA API COLOMBIA ===")
        print("1. Información general de Colombia")
        print("2. Lista de departamentos")
        print("3. Regiones del país")
        print("4. Atracciones turísticas")
        print("5. Salir")

        opcion = input("\nSeleccione una opción (1-5): ")

        if opcion == "1":
            info_colombia()
        elif opcion == "2":
            info_departamentos()
        elif opcion == "3":
            info_regiones()
        elif opcion == "4":
            info_atracciones()
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    menu()