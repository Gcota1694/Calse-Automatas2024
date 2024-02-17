import json

def imprimir_cacaracteres(ejemplo_json):
    with open(ejemplo_json, 'r') as file:
        contenido_json = json.load(file)
        
        for clave, valor in contenido_json.items():
            print("{")
            for caracter in clave:
                print(caracter)
            
            print("\"")
            for caracter in valor:
                print(caracter)
            print("\"")
            print("}")

imprimir_cacaracteres('ejemplo.json')
