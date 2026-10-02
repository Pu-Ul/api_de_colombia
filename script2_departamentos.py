import requests

URL = "https://api-colombia.com/api/v1/Department"


def obtener_departamentos():
    response = requests.get(URL)
    if response.status_code == 200:
        departamentos = response.json()
        for dep in departamentos:
            print(f"\n--- {dep.get('name')} ---")
            print(f"Descripción: {dep.get('description')}")

            # La capital viene dentro del objeto 'city' o 'capitals'
            capital = dep.get("city") or dep.get("capital")
            if capital and isinstance(capital, dict):
                print(f"Capital: {capital.get('name')}")
                print(f"Descripción Capital: {capital.get('description')}")
            else:
                print("Capital: No especificada")
    else:
        print("Error al consultar la API")


if __name__ == "__main__":
    obtener_departamentos()