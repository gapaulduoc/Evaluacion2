import requests
import urllib.parse

route_url = "https://graphhopper.com/api/1/route?"
profile = {"auto": "car", "bicicleta": "bike", "a pie": "foot"}
key = "5ef5fbf7-5fb3-41e2-a3a9-5eb3da2ea1c7"

def geocoding(location, key):
    while location == "":
        location = input("Ingrese la ubicación nuevamente: ").strip().lower()
        if location in ("q", "quit", "s", "salir"):
            raise SystemExit
    geocode_url = "https://graphhopper.com/api/1/geocode?"
    url = geocode_url + urllib.parse.urlencode({"q": location, "limit": "1", "key": key, "locale": "es"})
    replydata = requests.get(url)
    json_data = replydata.json()
    json_status = replydata.status_code
    if json_status == 200 and len(json_data["hits"]) != 0:
        lat = json_data["hits"][0]["point"]["lat"]
        lng = json_data["hits"][0]["point"]["lng"]
        name = json_data["hits"][0]["name"]
        value = json_data["hits"][0]["osm_value"]
        if "country" in json_data["hits"][0]:
            country = json_data["hits"][0]["country"]
        else:
            country = ""
        if "state" in json_data["hits"][0]:
            state = json_data["hits"][0]["state"]
        else:
            state = ""
        if len(state) != 0 and len(country) != 0:
            new_loc = name + ", " + state + ", " + country
        elif len(state) != 0:
            new_loc = name + ", " + country
        else:
            new_loc = name
        print("URL de Geocodificación para " + new_loc + " (Tipo de ubicación: " + value + ")\n" + url)
    else:
        lat = "null"
        lng = "null"
        new_loc = location
        if json_status != 200:
            print("Estado API Geocodificación: " + str(json_status) + "\nMensaje de error: " + json_data["message"])
        else:
            print("Estado API Geocodificación: " + str(json_status) + "\nError: lista de resultados vacía")
    return json_status, lat, lng, new_loc

def t(x):
    s = x
    repl = {
        "turn right": "gira a la derecha",
        "turn left": "gira a la izquierda",
        "turn sharp right": "gira pronunciado a la derecha",
        "turn sharp left": "gira pronunciado a la izquierda",
        "turn slight right": "gira levemente a la derecha",
        "turn slight left": "gira levemente a la izquierda",
        "continue onto": "continúa por",
        "continue on": "continúa por",
        "continue": "continúa",
        "keep right": "mantente a la derecha",
        "keep left": "mantente a la izquierda",
        "head": "dirígete",
        "merge": "incorpórate",
        "take the ramp": "toma la salida",
        "enter roundabout": "entra a la rotonda",
        "exit roundabout": "sal de la rotonda",
        "at roundabout": "en la rotonda",
        "drive toward": "conduce hacia",
        "arrive at destination": "¡fin del recorrido!",
        "arrive at": "llega a",
        "onto": "por",
        "toward": "hacia"
    }
    low = s.lower()
    for k, v in repl.items():
        if k in low:
            idx = low.find(k)
            s = s[:idx] + v + s[idx+len(k):]
            low = s.lower()
    s = s[:1].upper() + s[1:]
    return s

while True:
    print("\n+++++++++++++++++++++++++++++++++++++++++++++")
    print("Perfiles de vehículo disponibles en Graphhopper:")
    print("+++++++++++++++++++++++++++++++++++++++++++++")
    for p in profile.keys():
        print(p)
    print("+++++++++++++++++++++++++++++++++++++++++++++")
    vehicle_input = input("Ingrese un tipo de vehículo de la lista: ").strip().lower()
    if vehicle_input in ("q", "quit", "s", "salir"):
        raise SystemExit
    if vehicle_input in profile:
        vehicle = profile[vehicle_input]
    else:
        vehicle = "car"
        print("No se ingresó un tipo válido. Se usará 'auto'.")
    loc1 = input("Ubicación de inicio: ").strip()
    if loc1.lower() in ("q", "quit", "s", "salir"):
        raise SystemExit
    orig = geocoding(loc1, key)
    loc2 = input("Destino: ").strip()
    if loc2.lower() in ("q", "quit", "s", "salir"):
        raise SystemExit
    dest = geocoding(loc2, key)
    print("=================================================")
    if orig[0] == 200 and dest[0] == 200:
        op = "&point=" + str(orig[1]) + "%2C" + str(orig[2])
        dp = "&point=" + str(dest[1]) + "%2C" + str(dest[2])
        paths_url = route_url + urllib.parse.urlencode({"key": key, "vehicle": vehicle, "locale": "es"}) + op + dp
        paths_data = requests.get(paths_url).json()
        paths_status = requests.get(paths_url).status_code
        print("Estado API de Rutas: " + str(paths_status))
        print("URL de Rutas:\n" + paths_url)
        print("=================================================")
        print("Indicaciones desde " + orig[3] + " hasta " + dest[3] + " en " + vehicle_input)
        print("=================================================")
        if paths_status == 200:
            distancia_m = float(paths_data["paths"][0]["distance"])
            km = distancia_m / 1000.0
            millas = km / 1.61
            tiempo_ms = float(paths_data["paths"][0]["time"])
            horas = tiempo_ms / 1000.0 / 3600.0
            print("Distancia recorrida: {0:.2f} km / {1:.2f} millas".format(km, millas))
            print("Duración del viaje: {0:.2f} horas".format(horas))
            print("=================================================")
            for each in range(len(paths_data["paths"][0]["instructions"])):
                path = paths_data["paths"][0]["instructions"][each]["text"]
                distance = float(paths_data["paths"][0]["instructions"][each]["distance"])
                print("{0} ( {1:.2f} km / {2:.2f} millas )".format(t(path), distance/1000.0, (distance/1000.0)/1.61))
            print("=================================================")
        else:
            print("Mensaje de error: " + paths_data["message"])
            print("*************************************************")
    else:
        print("*************************************************")