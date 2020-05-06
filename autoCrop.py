import pyautogui as pag

pag.PAUSE = 1.0

fileManager = (411, 1036)
gimp = (837, 1034)
layer = (242, 46)
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
pag.moveTo(330, 298)
pag.click()

#open coding projects
pag.moveTo(530, 263)
pag.click(clicks = 2)

#Open project folder
pag.scroll(-100)
pag.moveTo(470, 420)
pag.click(clicks = 2)

#Open assets
pag.moveTo(475, 310)
pag.click(clicks = 2)
pag.scroll(-50)

#Open our folder we wanna work on
#Open w
pag.moveTo(470, 555)
pag.click(clicks = 2)
#pag.scroll(-300)

#Double click the first image
pag.moveTo(550, 220)
pag.click(clicks = 2)


#START MAIN LOOP
for i in range(2, 54):
	pag.PAUSE = 1.0
	#Start with image open in gimp and delete the old one
	pag.moveTo(682, 260)

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

	fileName = "z" + str(i)
	pag.typewrite(fileName)

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
	pag.moveTo(650, 255)
	#pag.scroll(-500)
	#pag.moveTo(680, 755)
	pag.click()
	pag.press('enter')







