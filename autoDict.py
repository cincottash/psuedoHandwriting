import pyautogui as pag

startPoint = (114, 725)

def main():
	#Click on page
	pag.click(startPoint)
	
	for dictIndex in range(10, 52):
		

		#Start with 1 WS gap below last curly brace and paste the example Dict
		pag.hotkey('ctrl', 'v')

		#Move to the dict name
		for i in range(66):
			pag.press('up')

		#Go over 8 times
		for j in range(13):
			pag.press('right')
		
		#Update the dictNum
		digits = [int(x) for x in str(dictIndex)]
		for number in digits:
			pag.press(str(number))

		for k in range(2):
			pag.press('down')

		for l in range(24):
			pag.press('right')


		# #Iterate over each letter in the dict
		digits = [int(x) for x in str(dictIndex)]
		for number in digits:
			pag.press(str(number))

		for i in range(0, 61):
			pag.press('down')
			pag.press('left')
			pag.press('left')
			for number in digits:
				pag.press(str(number))
			#pag.press(str(dictIndex))
		for u in range(4):
			pag.press('down')
		# pag.press('tab')









if __name__ == '__main__':
	main()