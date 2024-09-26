from socket import *  
import threading  
from datetime import datetime  

# Dirección y puerto donde el servidor escuchará conexiones
direccionServidor = 'localhost'
puertoServidor = 9099

# Crear el socket del servidor
socketServidor = socket(AF_INET, SOCK_STREAM)
socketServidor.bind((direccionServidor, puertoServidor))  # Asocia el socket a una dirección IP y puerto
socketServidor.listen()  # Configura el socket para escuchar conexiones entrantes

clientes = {}  # Diccionario que guarda las conexiones de los clientes
nombres = {}  # Diccionario que asocia nombres de clientes con sus conexiones

# Función que maneja la comunicación con cada cliente de forma individual
def manejar_cliente(socketConexion, addr):
    nombre_cliente = socketConexion.recv(4096).decode()  # Recibe el nombre del cliente
    bienvenida = f"{nombre_cliente} se ha unido al chat."  
    print(bienvenida)  
    broadcast(bienvenida, socketConexion)  
    
    # Añade al cliente al diccionario de clientes y guarda su nombre
    clientes[socketConexion] = addr
    nombres[socketConexion] = nombre_cliente
    
    while True:
        try:
            # Recibe mensajes del cliente
            mensajeRecibido = socketConexion.recv(4096).decode()
            hora_actual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Obtiene la hora actual

            if mensajeRecibido.lower() == "/finalizar chat":
                break  # Si el cliente decide finalizar, sale del loop

            # Condicionales para mensajes especiales
            elif mensajeRecibido.lower() == "/saludar":
                mensaje = f"{nombres[socketConexion]}: Hola ¿Cómo estás?"
                enviar_a_cliente(socketConexion, mensaje)  # Envía el mensaje al cliente que lo escribió
                broadcast(mensaje, socketConexion)  # Envía el mensaje a todos los demás
                print(f"[{hora_actual}] {mensaje}")

            elif mensajeRecibido.lower() == "/despedirse":
                mensaje = f"{nombres[socketConexion]}: Hasta luego. Que tengas un lindo día"
                enviar_a_cliente(socketConexion, mensaje)
                broadcast(mensaje, socketConexion)
                print(f"[{hora_actual}] {mensaje}")

            elif mensajeRecibido.lower() == "/emoji":
                mensaje = f"{nombres[socketConexion]}: 😊"
                enviar_a_cliente(socketConexion, mensaje)
                broadcast(mensaje, socketConexion)
                print(f"[{hora_actual}] {mensaje}")
                
            else:
                # Cualquier otro mensaje normal
                mensaje_completo = f"{nombres[socketConexion]}: {mensajeRecibido}"
                enviar_a_cliente(socketConexion, mensaje_completo)
                broadcast(mensaje_completo, socketConexion)
                print(f"[{hora_actual}] {mensaje_completo}")  # Muestra el mensaje en consola del servidor
                
        except Exception as e:
            # Si hay un error en la recepción del mensaje
            print(f"Error al recibir mensaje de {addr}: {e}")
            break

    despedida = f"{nombres[socketConexion]} ha dejado el chat."
    print(despedida)
    broadcast(despedida, socketConexion)  # Notifica a los otros clientes que este cliente dejó el chat
    socketConexion.close()  # Cierra la conexión con el cliente
    del clientes[socketConexion]  # Elimina al cliente del diccionario de conexiones
    del nombres[socketConexion]  # Elimina el nombre del cliente

# Función para enviar un mensaje al cliente que lo envía
def enviar_a_cliente(cliente, mensaje):
    try:
        cliente.send(mensaje.encode())  # Envía el mensaje codificado al cliente
    except:
        cliente.close()  # Si falla, cierra la conexión

# Función para enviar mensajes a todos los clientes excepto al que lo envía
def broadcast(mensaje, conexion_actual):
    for cliente in clientes:
        if cliente != conexion_actual:  # Evita que el remitente reciba su propio mensaje
            try:
                cliente.send(mensaje.encode())  # Envía el mensaje codificado
            except:
                cliente.close()  # Cierra la conexión si falla
                del clientes[cliente]  # Elimina el cliente que falló

# Mensaje que indica que el servidor ha comenzado a escuchar
print("Servidor iniciado...")
while True:
    # Acepta nuevas conexiones de clientes
    socketConexion, addr = socketServidor.accept()
    print(f"Conectado con un cliente {addr}")
    # Inicia un hilo para manejar la conexión del cliente
    hilo_cliente = threading.Thread(target=manejar_cliente, args=(socketConexion, addr))
    hilo_cliente.start()
