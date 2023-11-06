import requests

def hae_chuck_norris_vitsi():
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        vitsi = data["value"]
        return vitsi
    else:
        return None

def main():
    vitsi = hae_chuck_norris_vitsi()
    if vitsi:
        print(vitsi)
    else:
        print("Vitsin hakeminen epäonnistui. Yritä myöhemmin uudelleen.")

if __name__ == "__main__":
    main()