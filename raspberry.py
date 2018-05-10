#!/usr/bin/pythonAdafruit_DHT
from bs4 import BeautifulSoup
import urllib2
import datetime
import serial
import requests
import json
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(22, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(23, GPIO.OUT, initial = GPIO.LOW)
def publish(Tem, humidity, ppm, lat, lon):
        url = "https://ajitjadhav.pythonanywhere.com/pollution-data/getdata?t=" +str(Tem)+"&h="+str(humidity)+"&pol=" +str(ppm)+"&lat="+str(lat)+"&lon="+str(lon)
        print(url)
        result = urllib2.urlopen(url).read()
t=0
lat=13.5492047
lon=79.9910752
while (True):
        while(len(L) != 3):
                try:
                        ser = serial.Serial('/dev/ttyACM0',9600) 
                        read_serial=ser.readline()
                        L = read_serial.split()
                        #print read_serial
                except: 
                        pass
        try:
                r  = requests.get('https://maps.app.goo.gl/jF39aYpPXu51BUlm2')
                data = r.text
                soup = BeautifulSoup(data, 'html.parser')
                soup=str(soup)
                n= soup.find(',13.5')
                lon, lat =soup[n-17:n+11].split(',')
                print(lat, lon)
        print L[0],L[1],L[2], lat, lon
        #print("hello")
        #print str(datetime.datetime.now())
	
        publish(L[0],L[1],L[2], lat, lon)
        print "YES"
        L = []
