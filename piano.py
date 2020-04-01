import os

try:
	import requests
	import pyautogui
	import webbrowser
	import time
	from bs4 import BeautifulSoup
except ModuleNotFoundError:
	print("Some dependencies were not found. We're installing them for you. Please wait")
	os.system('python3 -m pip install webbrowser, pyautogui, bs4')

piano_url = "https://virtualpiano.net/"

def main():
	url = str(input("Enter the piano sheet link for the song (From VirtualPiano.net) : "))
	response = requests.get(url).text
	soup = BeautifulSoup(response, 'html.parser')
	content = soup.find('p')
	for elem in content:
		sheet = elem
		break
	return sheet

def play(sheet):
	for i in range(len(sheet)):
		if sheet[i] == '.':
			time.sleep(1)
		elif sheet[i].isalnum():
			pyautogui.press(sheet[i])
		elif sheet[i] == '[':
			string = ""
			multi = []
			start = i
			for j in range(start + 1, len(sheet)):
				if sheet[j] == ']':
					end = j
					break
				else:
					multi.append(sheet[j])
			for elem in multi:
				pyautogui.press(elem)
				break
			multi.clear()
		elif sheet[i] == ' ':
			time.sleep(0.2)
		else:
			pass	

if __name__ == "__main__":
	print("""                                                                                                         
                                                                                                            
                                                                                                            
  ano CLIPia   CLIPi        ian       ano C   iano C    ano CL                CLIP     CLIPi      IPiano    
   no CLIPian  CLIPi       Piano      ano C   iano C   iano CLI            no CLIPian  CLIPi      IPiano    
   no C    ano CLIP        Piano       no CL   ano    Pian  CLIP          ano   IPian   LIP        Pian     
   no CLIPiano  LIP       IPiano       no CLI  ano    Pia    LIP         ian     Pian   LI          ian     
   no CLIPian  CLI        IPi no       no CLIP ano   IPia    LIPi        ian            LI         Pia      
   no CLIPia    LIP      LIPiano C     no CLIP ano   IPia    LIPi        ia             LI          ian     
   no           LI       LIPiano C     no  LIPiano    Pia    LIP         ia             LIP         ia      
   no           LI      CLIP   o CL    no  LIPiano    Pia    LIP         ia       ia   CLIP     C   ia      
   no          CLIP     CLI      CL    no   IPiano    Pian  CLIP         ian     Pia    LIP     C  Pian     
  ano CL       CLIPi  o CLIP   o CLIP ano C  Piano     iano CLI           ano CLIPia   CLIPiano C IPiano    
  ano CL       CLIPia o CLIP   o CLIP ano C   iano      ano CL             no CLIP     CLIPiano C IPiano    
                                                                                              
											      By Sharma Deepesh""")
	sheet = main()
	webbrowser.open_new(piano_url)
	time.sleep(10)
	play(sheet)										     
