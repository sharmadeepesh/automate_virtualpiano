import os

try:
	import requests
	from selenium import webdriver
	import pyautogui
	from bs4 import BeautifulSoup
except ModuleNotFoundError:
	print("Some dependencies were not found. We're installing them for you. Please wait")
	os.system('python3 -m pip install requests, time, webbrowser, pyautogui, bs4')

piano_url = "https://virtualpiano.net/"

def main():
	newsheet = ""
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
	sheet = main()
	webbrowser.open_new(piano_url)
	time.sleep(10)
	play(sheet)
