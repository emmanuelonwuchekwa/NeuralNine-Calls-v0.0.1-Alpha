import tkinter as tk
from vidstream import *
import socket

local_ip_address = socket.gethostbyname(socket.gethostname())
print(local_ip_address)

server = StreamingServer(local_ip_address, 7777)
receiver = AudioReceiver(local_ip_address, 6666)


def start_listening():
    t1 = threading.Thread(target=server.start_server)
    t2 = threading.Thread(target=receiver.start_server)
    t1.start()
    t2.start()


def start_camera_stream():
    camera_client = CameraClient(text_target_ip.get(1.0, 'end-1c'), 9999)
    t3 = threading.Thread(target=camera_client.start_stream)
    t3.start()


def start_screen_sharing():
    screen_client = ScreenShareClient(text_target_ip.get(1.0, 'end-1c'), 9999)
    t4 = threading.Thread(target=screen_client.start_stream)
    t4.start()


def start_audio_stream():
    audio_sender = AudioSender(text_target_ip.get(1.0, 'end-1c'), 8888)
    t5 = threading.Thread(target=audio_sender.start_stream)
    t5.start()


# GUI
window = tk.Tk()
window.title("NeuralNine Calls v0.0.1 Alpha")
window.geometry('300x250')

label_target_ip = tk.Label(window, text="Enter Target IP:")
label_target_ip.pack()

text_target_ip = tk.Text(window, height=1, width=30)
text_target_ip.pack()

btn_listen = tk.Button(window, text="Initiate Server", width=30, command=start_listening)
btn_listen.pack(pady=5)

btn_camera = tk.Button(window, text="Begin Camera Streaming", width=30, command=start_camera_stream)
btn_camera.pack(pady=5)

btn_screen = tk.Button(window, text="Start Screen Sharing", width=30, command=start_screen_sharing)
btn_screen.pack(pady=5)

btn_audio = tk.Button(window, text="Start Audio Stream", width=30, command=start_audio_stream)
btn_audio.pack(pady=5)

window.mainloop()
