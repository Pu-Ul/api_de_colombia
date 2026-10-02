import requests

URL = "https://api-colombia.com/api/v1/Country/Colombia"


def obtener_info_colombia():
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        print(f"Nombre: {data.get('name')}")
        print(f"Descripción: {data.get('description')}")
        print(f"Código de moneda: {data.get('currencyCode')}")
    else:
        print("Error al consultar la API")


if __name__ == "__main__":
    obtener_info_colombia()