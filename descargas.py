import os
import humanize
ruta = '/Users/sarag/'

def recorre (ruta):
        print("\nComprobando carpeta: ", ruta)
        # Obtener ficheros de la ruta
        lista = os.listdir(ruta)

        # Recorrer resultados lista e imprimir sólo los ficheros
        for carpeta in lista:
                rutaC = os.path.join(ruta, carpeta)
                
                #Obtener tamaño de los ficheros en formato humano
                size = os.path.getsize(rutaC)
                human = humanize.naturalsize(size)
                
                if os.path.isfile(rutaC):
                        print("Es archivo: ", carpeta, "Tamaño: ", human)
     
                elif os.path.isdir(rutaC):
                        print("Es carpeta: ", carpeta, "Tamaño: ", human)
                        recorre(rutaC)
recorre(ruta)        
   