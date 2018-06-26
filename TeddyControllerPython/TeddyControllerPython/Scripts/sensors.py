import Constellation
import serial
import random
import json
import time
import serial.tools.list_ports

def OnExit():
    pass

def OnStart():
    #declaration du StateObject
    Constellation.DescribeStateObjectType("Sensors", "StateObject qui récupère données des capteurs ", [
    { 'Name':'CO2', 'Type':'int', 'Description': 'Temperature en °C' },        
    { 'Name':'Soundlevel', 'Type':'int', 'Description': ' intensite sonore en dB' },
    {'Name':'Temperature', 'Type' : 'float', 'Description' : 'niveau de co2(en ppm)'},
    {'Name':'Ledstate', 'Type' : 'bool', 'Description' : 'niveau de co2(en ppm)'}])
    #ouverture de port serie
    
    Constellation.WriteInfo("Hi I'm '%s' and I currently running on %s and %s to Constellation" % (Constellation.PackageName, Constellation.SentinelName if not Constellation.IsStandAlone else 'local sandbox', "connected" if Constellation.IsConnected else "disconnected"))
    connected = []
    ser = 0
    while len(connected) <= 0 and ser == 0: 

	    ports_series = serial.tools.list_ports.comports()

	    for element in ports_series:
	        connected.append(element.device)
	
	    if len(connected) > 0:						# on test si plusieurs ports ont été trouvée, si oui on utilise le 1er
		    ser = serial.Serial(connected[0], 9600)
    ser.flushInput() 

    while 1: 
        #on lit le json sorti du port serie
        data = ser.readline()
        #on lui explique que c'est un json
        pushMe = json.loads(data)
        #Et on l'envoi a constellation
        Constellation.PushStateObject("Sensors",pushMe)
        time.sleep(1)





Constellation.Start(OnStart);