import requests


# 1. Información General de Colombia
def info_colombia():
    res = requests.get("https://api-colombia.com/api/v1/Country/Colombia")
    if res.status_code == 200:
        d = res.json()
        print(f"\n--- INFORMACIÓN GENERAL ---")
        print(f"Nombre: {d.get('name')}")
        print(f"Descripción: {d.get('description')}")
        print(f"Moneda: {d.get('currencyCode')}")


# 2. Lista de Departamentos
def info_departamentos():
    res = requests.get("https://api-colombia.com/api/v1/Department")
    if res.status_code == 200:
        for dep in res.json():
            cap = dep.get("city") or dep.get("capital") or {}
            print(f"\n--- {dep.get('name')} ---")
            print(f"Descripción: {dep.get('description')}")
            print(f"Capital: {cap.get('name', 'N/A')}")
            print(f"Descripción Capital: {cap.get('description', 'N/A')}")


# 3. Regiones del país
def info_regiones():
    res = requests.get("https://api-colombia.com/api/v1/Region")
    if res.status_code == 200:
        for reg in res.json():
            print(f"\n--- {reg.get('name')} ---")
            print(f"Descripción: {reg.get('description')}")


# 4. Atracciones turísticas
def info_atracciones():
    res = requests.get("https://api-colombia.com/api/v1/TouristicAttraction")
    if res.status_code == 200:
        for atr in res.json():
            ciu = atr.get("city") or {}
            print(f"\n--- {atr.get('name')} ---")
            print(f"Descripción: {atr.get('description')}")
            print(f"Ciudad: {ciu.get('name', 'N/A')}")


# Extra: Menú interactivo
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