import pyautogui as pag

pag.PAUSE = 1.0

fileManager = (375, 1040)
gimp = (745, 1040)
layer = (240, 45)
transparency = (332, 316)
addAlpha = (560, 320)
select = (100, 45)
byColor = (175, 175)
whiteSpot = (500, 300)
image = (190, 45)
autoCrop = (260, 333)
scale = (225, 270)
scaleNums = (925, 466)
scaleButton = (1000, 700)
file = (22, 42)
exportAs = (106, 384)
export = (1270, 890)
export2 = (1000, 700)
xButton = (69, 69)
discardChanges = (980, 656)
openn = (55, 111)

#open file manager
pag.moveTo(fileManager)
pag.click()

#open documents
for o in range(5):
	pag.press('down')
pag.press('enter')

#open coding projects
for n in range(2):
	pag.press('down')
pag.press('enter')

pag.PAUSE = 0.2
#Open project folder
for m in range(14):
	pag.press('down')
pag.press('enter')


#Open assets
for l in range(3):
	pag.press('down')
pag.press('enter')

#Open our folder we wanna work on 
letter = "Z"
for h in range(62):
	pag.press('down')
pag.press('enter')

#open last image
for k in range(56):
	pag.press('down')
pag.PAUSE = 0.5
pag.press('enter')

#START MAIN LOOP
for i in range(56):
	#Start with image open in gimp and delete the old one
	#pag.moveTo(682, 260)

	pag.moveTo(fileManager)
	pag.click()

	pag.press('delete')
	pag.PAUSE = 0.4
	
	#Open up gimp again
	pag.moveTo(gimp)
	pag.click()

	#add transparency layer
	pag.moveTo(layer)
	pag.click()
	pag.moveTo(transparency)
	pag.moveTo(addAlpha)
	pag.click()

	#Select by color
	pag.moveTo(select)
	pag.click()
	pag.moveTo(byColor)
	pag.click()

	#Remove background
	pag.moveTo(whiteSpot)
	pag.click()
	pag.press('delete')

	#Auto crop
	pag.moveTo(image)
	pag.click()
	pag.moveTo(autoCrop)
	pag.click()

	#Scale
	pag.click()
	pag.moveTo(image)
	pag.click()
	pag.moveTo(scale)
	pag.click()
	pag.moveTo(scaleNums)
	pag.click()
	pag.press('backspace')
	pag.press('enter')
	pag.moveTo(scaleButton)
	pag.click()

	#Export
	pag.moveTo(file)
	pag.click()
	pag.moveTo(exportAs)
	pag.click()

	fileName = letter + str(i)
	pag.typewrite(fileName)

 	#GOOD UP TO HERE
	pag.moveTo(export)
	pag.click()

	pag.moveTo(export2)
	pag.click()

	pag.moveTo(xButton)
	pag.click()

	pag.moveTo(discardChanges)
	pag.click()

	pag.moveTo(file)
	pag.click()
	pag.moveTo(openn)
	pag.click()


	
	#Click the last image
	pag.PAUSE = 0.1
	for j in range(56):
		pag.press('down')
	pag.PAUSE = 1.0
	pag.press('enter')
	# #pag.moveTo(680, 755)
	# # pag.click()
	# pag.press('enter')







