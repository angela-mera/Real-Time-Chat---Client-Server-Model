import tkinter as tk  
from socket import *  
import threading 
import sys  

# Dirección IP y puerto del servidor al cual se conectará el cliente
IPServidor = "localhost"
puertoServidor = 9099

# Función que recibe mensajes del servidor y los muestra en la interfaz de chat
def recibir_mensajes():
    while True:
        try:
            # Recibe mensajes del servidor con un tamaño máximo de 4096 bytes
            mensaje = socketCliente.recv(4096).decode()
            # Si el mensaje tiene un formato con ":", separa el nombre del mensaje
            if ":" in mensaje:
                nombre, texto = mensaje.split(":", 1)
                chat_box.insert(tk.END, nombre + ":", 'negrita')
                chat_box.insert(tk.END, texto + "\n")
            else:
                chat_box.insert(tk.END, mensaje + "\n")
        except:
            print("Conexión cerrada.")
            socketCliente.close()
            break

# Función para enviar mensajes al servidor desde la interfaz gráfica
def enviar_mensaje():
    mensaje = mensaje_entry.get() 
    if mensaje.lower() == "/finalizar chat":  
        socketCliente.send("/finalizar chat".encode())  # Envía la señal de finalizar al servidor
        root.quit()  
    else:
        socketCliente.send(mensaje.encode())  
    mensaje_entry.delete(0, tk.END)  

# Establece la conexión del cliente con el servidor
socketCliente = socket(AF_INET, SOCK_STREAM)
socketCliente.connect((IPServidor, puertoServidor))

# Solicita el nombre del usuario que usará en el chat
nombre_cliente = input("Ingrese su nombre: ")
socketCliente.send(nombre_cliente.encode())  

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title(f"Chat de {nombre_cliente}")  

# Caja de texto donde se mostrarán los mensajes del chat
chat_box = tk.Text(root, height=20, width=50)
chat_box.pack()

# Configura el estilo de los nombres en negrita
chat_box.tag_configure('negrita', font=('Arial', 10, 'bold'))

# Entrada de texto donde el cliente escribirá sus mensajes
mensaje_entry = tk.Entry(root, width=50)
mensaje_entry.pack()

# Botón que enviará el mensaje al presionarlo
enviar_btn = tk.Button(root, text="Enviar", command=enviar_mensaje)
enviar_btn.pack()

# Inicia un hilo para recibir mensajes en segundo plano
hilo_recibir = threading.Thread(target=recibir_mensajes)
hilo_recibir.daemon = True  # Permite que el hilo se cierre cuando la aplicación principal se cierre
hilo_recibir.start()


root.mainloop()
