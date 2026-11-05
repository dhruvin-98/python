import requests

# response = requests.get("https://api.github.com")
# print(response.status_code)
# # print(response.json())


base_url = "https://pokeapi.co/api/v2/"

def get_pockmon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Failed to retrive data : {response.status_code}")


pockmon_name = input("Enter name of your favourite POKEMON : ")

pockmon_info = get_pockmon_info(pockmon_name)


if pockmon_info:
    print(f"Name : {pockmon_info["name"]}")
    print(f"Height : {pockmon_info["height"]}")
    print(f"Weight : {pockmon_info["weight"]}")


