import subprocess 
import winshell
import pyttsx3 
import tkinter 
import json 
import random 
import operator 
import speech_recognition as sr 
import datetime 
import wikipedia 
import webbrowser 
import os 
import pyjokes 
import feedparser 
import smtplib 
import ctypes 
import time 
import requests 
import shutil 
from clint.textui import progress 
from ecapture import ecapture as ec 
from bs4 import BeautifulSoup 
import win32com.client as wincl 
from urllib.request import urlopen 
engine = pyttsx3.init('sapi5') 
voices = engine.getProperty('voices') 


def speak(audio): 
	engine.say(audio) 
	engine.runAndWait() 
def takeCommand(): 
	
	r = sr.Recognizer() 
	
	with sr.Microphone() as source: 
		
		print("Listening...") 
		r.pause_threshold = 1
		audio = r.listen(source) 

	try: 
		print("Recognizing...")	 
		query = r.recognize_google(audio, language ='en-in') 
		print(f"User said: {query}\n") 

	except Exception as e: 
		print(e)	 
		print("Unable to Recognizing your voice.") 
		return "None"
	
	return query 

def sendEmail(to, content): 
	server = smtplib.SMTP('smtp.gmail.com', 587) 
	server.ehlo() 
	server.starttls() 
	
	# Enable low security in gmail 
	server.login('****************', '*********') 
	server.sendmail('*****************', to, content) 
	server.close()
if __name__ == '__main__': 
	clear = lambda: os.system('cls') 
	
	# This Function will clean any 
	# command before execution of this python file 
	clear() 
	while True: 
		
		query = takeCommand().lower() 
		
		# All the commands said by user will be 
		# stored here in 'query' and will be 
		# converted to lower case for easily 
		# recognition of command 

		if 'open youtube' in query: 
			speak("Here you go to Youtube\n") 
			webbrowser.open("youtube.com") 

		elif 'open google' in query: 
			speak("Here you go to Google\n") 
			webbrowser.open("google.com") 

		elif 'open stackoverflow' in query: 
			speak("Here you go to Stack Over flow.Happy coding") 
			webbrowser.open("stackoverflow.com") 

		elif 'play music' in query or "play song" in query: 
			speak("Here you go with music") 
			# music_dir = "G:\\Song" 
			music_dir = "C:\\Users\\DELL\\Music"
			songs = os.listdir(music_dir) 
			print(songs)	 
			random = os.startfile(os.path.join(music_dir, songs[1])) 

		elif 'the time' in query: 
			strTime = datetime.datetime.now().strftime("%H:%M:%S")	 
			speak(f"Mam, the time is {strTime}") 
    
		elif 'send a mail' in query: 
			try: 
				speak("What should I say?") 
				content = takeCommand() 
				speak("whome should i send") 
				to = input()	 
				sendEmail(to, content) 
				speak("Email has been sent !") 
			except Exception as e: 
				print(e) 
				speak("I am not able to send this email") 


		elif 'exit' in query: 
			speak("Thanks for giving me your time") 
			exit() 
		elif 'joke' in query: 
			speak(pyjokes.get_joke()) 
			
		elif "calculate" in query: 
			
			os.startfile("calc")

		elif 'search' in query or 'play' in query: 
			
			query = query.replace("search", "") 
			query = query.replace("play", "")		 
			webbrowser.open(query) 

		
		elif 'lock window' in query: 
				speak("locking the device") 
				ctypes.windll.user32.LockWorkStation() 

		elif 'shutdown system' in query: 
				speak("Hold On a Sec ! Your system is on its way to shut down") 
				subprocess.call('shutdown / p /f') 
				
		elif 'empty recycle bin' in query: 
			winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True) 
			speak("Recycle Bin Recycled") 

		elif "don't listen" in query or "stop listening" in query: 
			speak("for how much time you want to stop from listening commands") 
			a = int(takeCommand()) 
			time.sleep(a) 
			print(a) 

		elif "where is" in query: 
			query = query.replace("where is", "") 
			location = query 
			speak("User asked to Locate") 
			speak(location) 
			webbrowser.open("https://www.google.nl / maps / place/" + location + "") 

		elif "camera" in query or "take a photo" in query: 
			ec.capture(0, "My Camera ", "img.jpg") 

		elif "restart" in query: 
			subprocess.call(["shutdown", "/r"]) 
			
		elif "hibernate" in query or "sleep" in query: 
			speak("Hibernating") 
			subprocess.call("shutdown / h") 

		elif "log off" in query or "sign out" in query: 
			speak("Make sure all the application are closed before sign-out") 
			time.sleep(5) 
			subprocess.call(["shutdown", "/l"]) 

		elif "write a note" in query: 
			speak("What should i write, Mam") 
			note = takeCommand() 
			file = open('f3.txt', 'w') 
			speak("Mam, Should i include date and time") 
			snfm = takeCommand() 
			if 'yes' in snfm or 'sure' in snfm: 
				strTime = datetime.datetime.now().strftime("% H:% M:% S") 
				file.write(strTime) 
				file.write(" :- ") 
				file.write(note) 
			else: 
				file.write(note) 
		
		elif "show note" in query: 
			speak("Showing Notes") 
			file = open("f3.txt", "r") 
			print(file.read()) 
			speak(file.read(6)) 

		elif "wikipedia" in query: 
			webbrowser.open("wikipedia.com") 

		

