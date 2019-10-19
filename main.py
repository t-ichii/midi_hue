import time
from phue import Bridge
import rtmidi2

midi_in = rtmidi2.MidiIn()
device_name = "nanoKONTROL2"
index = midi_in.ports_matching(device_name + "*")[0]
input_port = midi_in.open_port(index)
messages = [None, None] # prev, current

b = Bridge('172.24.13.125', 'RuLy6eJ4JSzXjmBD25-dna71FDETb8TXGVf85AmN')
b.connect()
# print(b.get_group())

while True:
    time.sleep(0.01)
    messages[0] = messages[1]
    messages[1] = input_port.get_message() # 変化がない場合はNone

    if messages[1] == None and messages[0] != None:
        if messages[0][1] in range(0,8):
            b.set_group(messages[0][1], 'bri', messages[0][2] * 2, transitiontime = 1)
        elif messages[0][1] in range(16, 24):
            b.set_group(messages[0][1] - 16, 'hue',  int(65535 * messages[0][2]/127), transitiontime = 1)
        print(messages[0])

# 0-7: フェーダ
# 16-23: つまみ
