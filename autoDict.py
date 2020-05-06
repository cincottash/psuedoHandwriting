import pyautogui as pag

startPoint = (115, 694)

def main():
	#Click on page
	pag.click(startPoint)
	
	for dictIndex in range(10, 54):
		

		#Start with 1 WS gap below last curly brace and paste the example Dict
		pag.hotkey('ctrl', 'v')

		#Press up 29 times
		for i in range(29):
			pag.press('up')

		#Go over 8 times
		for j in range(11):
			pag.press('right')
		
		#Update the dictNum
		digits = [int(x) for x in str(dictIndex)]
		for number in digits:
			pag.press(str(number))

		for k in range(2):
			pag.press('down')

		for l in range(20):
			pag.press('right')

		# for number in digits:
		# 	pag.press(str(number))

		#TODO FIX THIS
		# #Iterate over each letter in the dict
		numIndex = 0
		for number in digits:
			pag.press(str(number))

		# #Handle the 1=9 nums
		for numIndex in range(25):
			pag.press('down')
			pag.press('left')
			pag.press('left')
			for number in digits:
				pag.press(str(number))

		for u in range(5):
			pag.press('down')
		pag.press('tab')









if __name__ == '__main__':
	main()