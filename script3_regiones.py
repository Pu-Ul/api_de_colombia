import requests

URL = "https://api-colombia.com/api/v1/Region"


def obtener_regiones():
    response = requests.get(URL)
    if response.status_code == 200:
        regiones = response.json()
        for region in regiones:
            print(f"\nRegión: {region.get('name')}")
            print(f"Descripción: {region.get('description')}")
    else:
        print("Error al consultar la API")


if __name__ == "__main__":
    obtener_regiones()