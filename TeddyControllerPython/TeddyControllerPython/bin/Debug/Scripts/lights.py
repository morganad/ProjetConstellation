import Constellation
import serial
import serial.tools.list_ports
def OnExit():
    pass
@Constellation.MessageCallback()
def lightsCallback(isOn):
    # On ouvre le port serie
    connected = []
    ser = 0
    while len(connected) <= 0 and ser == 0: 

	    ports_series = serial.tools.list_ports.comports()

	    for element in ports_series:
	        connected.append(element.device)
	
	    if len(connected) > 0:						# on test si plusieurs ports ont été trouvée, si oui on utilise le 1er
		    ser = serial.Serial(connected[0], 9600)
    ser.flushInput()
    if(isOn == "True"):
        #Si ison est vrai, on allume la lumière
        Constellation.WriteInfo("lights are on")
        ser.write('a')

    else:
        Constellation.WriteInfo("lights are off")
        ser.write('e')


def OnStart():
    Constellation.OnExitCallback = OnExit
    

Constellation.Start(OnStart);