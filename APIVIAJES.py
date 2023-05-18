#importa las librerias pip requests y json
import requests, json

#define la funcion entre los viajes y los parametros origen y destino y dentro de este se encuentran:
def distancia_viajes(orig, dest):
    api_key = "gbJ0WKZXvFyauAS4XjzINUtZIpi9J8Zd" #la clave que nos entrega MapQuest Developer
    url = f'http://www.mapquestapi.com/directions/v2/route?key={api_key}&from={orig},Chile&to={dest}' #aqui la url donde se capturan los datos
    json_data = requests.get(url) #json data son las solicitudes GET que se hacen hacia la URL
    data = json_data.json() #data es la casilla anterior convertida a json
    distance = data['route']['distance'] * 1.60934  #se obtiene la distancia y se convierte en kilometros, los parametros en '' y [] los obtiene de la URL
    duration = data['route']['time']  #la duracion la obtiene de nuestros datos que estan en la URL
    return distance, duration

#define la función de coneversión del tiempo y los parametros que se usaran dentro de esta
def conversiontiempo(seg):              
    hrs = int(seg / 3600) #todo se trabaja en segundos y se realizan operaciones como division, el resto (%=)
    seg %= 3600
    min = int(seg / 60)
    seg %= 60
    return hrs, min, seg        #lo que nos devuelve las horas,minutos y segundos

#se define la funcion "principal" ya que en este se nos pide ingresar los destinos que serán validados con los datos que capturamos de MapQuest
def main():
    while True:                                                                                     #se crea un bucle de sentencia true
        orig = input("Ingrese ciudad de origen(para salir persione S o escriba salir ): ")             #pide ingresar la ciudad de origen
        #if orig.lower() == 's':
        if orig.upper() == 'S' or orig.lower() == 'salir':                         #si se presionan las letras "S" o se escribe Salida se termina el bucle y se termina el script y nos muestra la ultima linea que dice "Salida"
            break                                                                               #se solicita la ciudad de destino 
        dest = input("Ingrese la ciudad de destino: ")
        distance, duration = distancia_viajes(orig, dest)                           #despues de ingresar nos muestra la distancia y duracion de donde obtiene los datos que en este caso los obtiene de la primera función y la funcion inferior
        datos1(orig, dest, distance, duration)
    print("Se ha cerrado el programa")

#define los datos uno en donde se muestra al usuario la distancia en kilometros y la duracion del viaje y de donde hacia donde se realizará el viaje
def datos1(orig, dest, distance, duration):                                                 
    hrs, min, seg = conversiontiempo(duration) #la hora minutos y segundos son la duracion que se mostrará en el print
    print(f"Iniciando viaje desde {orig} hacia {dest}") 
    print(f"La distancia es de {distance:.1f} km.")
    print(f"La duración del viaje es de {hrs} horas, {min} minutos y {seg} segundos.")
    print()

if __name__ == '__main__':                                          #se utiliza para verificar que el script este siendo ejecutado correctamente, ya que sin este no se puede ejecutar correctamente el codigo
   main()
