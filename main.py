from setup import *
from globals import *
import random
import subprocess

def main():

	canvas = setup()

	documentFile = open("document.txt", "r")

	document = documentFile.read()
	
	#Our college ruled 8.5x11
	paper = pygame.image.load("assets/paper.png")
	
	#x,y coords are top left of image
	canvas.blit(paper, (0,0))
	
	displayDocument(canvas, document)
	
	pygame.display.update()

	pygame.image.save(canvas, "output.jpeg")
	
	#Open the 8.5x11 with firefox
	bashCommand = "firefox output.jpeg"
	
	process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
	output, error = process.communicate()
	exit(0)

def displayDocument(canvas, document):
	#The total space from the start of our current horizontal line
	collectiveSpacing = 0

	#Current horizontal line
	currentLine = 0

	for char in list(document):
			
		#Pick a random dict to use for this specific char
		dictNum = random.randint(0, 52)
		if(dictNum == 0):
			alphabetDict = alphabetDict0
		elif(dictNum == 1):
			alphabetDict = alphabetDict1
		elif(dictNum == 2):
			alphabetDict = alphabetDict2
		elif(dictNum == 3):
			alphabetDict = alphabetDict3
		elif(dictNum == 4):
			alphabetDict = alphabetDict4
		elif(dictNum == 5):
			alphabetDict = alphabetDict5
		elif(dictNum == 6):
			alphabetDict = alphabetDict6
		elif(dictNum == 7):
			alphabetDict = alphabetDict7
		elif(dictNum == 8):
			alphabetDict = alphabetDict8
		elif(dictNum == 9):
			alphabetDict = alphabetDict9
		elif(dictNum == 10):
			alphabetDict = alphabetDict10
		elif(dictNum == 11):
			alphabetDict = alphabetDict11
		elif(dictNum == 12):
			alphabetDict = alphabetDict12
		elif(dictNum == 13):
			alphabetDict = alphabetDict13
		elif(dictNum == 14):
			alphabetDict = alphabetDict14
		elif(dictNum == 15):
			alphabetDict = alphabetDict15
		elif(dictNum == 16):
			alphabetDict = alphabetDict16
		elif(dictNum == 17):
			alphabetDict = alphabetDict17
		elif(dictNum == 18):
			alphabetDict = alphabetDict18
		elif(dictNum == 19):
			alphabetDict = alphabetDict19
		elif(dictNum == 20):
			alphabetDict = alphabetDict20
		elif(dictNum == 21):
			alphabetDict = alphabetDict21
		elif(dictNum == 22):
			alphabetDict = alphabetDict22
		elif(dictNum == 23):
			alphabetDict = alphabetDict23
		elif(dictNum == 24):
			alphabetDict = alphabetDict24
		elif(dictNum == 25):
			alphabetDict = alphabetDict25
		elif(dictNum == 26):
			alphabetDict = alphabetDict26
		elif(dictNum == 27):
			alphabetDict = alphabetDict27
		elif(dictNum == 28):
			alphabetDict = alphabetDict28
		elif(dictNum == 29):
			alphabetDict = alphabetDict29
		elif(dictNum == 30):
			alphabetDict = alphabetDict30
		elif(dictNum == 31):
			alphabetDict = alphabetDict31
		elif(dictNum == 32):
			alphabetDict = alphabetDict32
		elif(dictNum == 33):
			alphabetDict = alphabetDict33
		elif(dictNum == 34):
			alphabetDict = alphabetDict34
		elif(dictNum == 35):
			alphabetDict = alphabetDict35
		elif(dictNum == 36):
			alphabetDict = alphabetDict36
		elif(dictNum == 37):
			alphabetDict = alphabetDict37
		elif(dictNum == 38):
			alphabetDict = alphabetDict38
		elif(dictNum == 39):
			alphabetDict = alphabetDict39
		elif(dictNum == 40):
			alphabetDict = alphabetDict40
		elif(dictNum == 41):
			alphabetDict = alphabetDict41
		elif(dictNum == 42):
			alphabetDict = alphabetDict42
		elif(dictNum == 43):
			alphabetDict = alphabetDict43
		elif(dictNum == 44):
			alphabetDict = alphabetDict44
		elif(dictNum == 45):
			alphabetDict = alphabetDict45
		elif(dictNum == 46):
			alphabetDict = alphabetDict46
		elif(dictNum == 47):
			alphabetDict = alphabetDict47
		elif(dictNum == 48):
			alphabetDict = alphabetDict48
		elif(dictNum == 49):
			alphabetDict = alphabetDict49
		elif(dictNum == 50):
			alphabetDict = alphabetDict50
		elif(dictNum == 51):
			alphabetDict = alphabetDict51

		if(char in alphabetDict):
			#Adds random spacing between each letter
			#TODO add the ability to overlap
			letterGap = random.uniform(0, 10)

			#Check if we're about to go over the page
			if(xStart + collectiveSpacing + letterGap + alphabetDict[char].get_rect().size[0] > canvasWidth):
				#Move to next horizontal line
				currentLine += 1

				#Reset total spacing
				collectiveSpacing = 0

				#add random margin on new line
				collectiveSpacing += random.uniform(0, 20)

			#Align to bottom of line and keep varying spacing as well as varying height, also check if our char can go below line (e.g like "j")
			offCenterChar = 0
			if(char in offCenterCharList):
				offCenterChar = 1

			collectiveSpacing += letterGap
			
			canvas.blit(alphabetDict[char], (xStart + collectiveSpacing, yStart + offCenterChar*alphabetDict[char].get_rect().size[1]/2 + currentLine * lineGap - alphabetDict[char].get_rect().size[1]  + random.uniform(-7, 7)))
			
			#Add a gap to compensate for the image length
			collectiveSpacing += alphabetDict[char].get_rect().size[0]
		
		#It's a space
		elif(char == " "):
			#A random sized space
			collectiveSpacing += space * random.uniform(0.8, 1.5)
		elif(char == "\n"):
			currentLine +=1 
			collectiveSpacing = 0
		
		#If char not in our dict, put unknown char symbol
		else:
			unknownChar = pygame.image.load("assets/unknownChar.png")
			
			canvas.blit(unknownChar, (xStart + collectiveSpacing, yStart + currentLine * lineGap - unknownChar.get_rect().size[1]))
			
			#Add a gap to compensate for the image length
			collectiveSpacing += unknownChar.get_rect().size[0]


if __name__ == '__main__':
	main()