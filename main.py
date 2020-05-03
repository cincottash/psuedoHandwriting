from setup import *
from globals import *
import random
import subprocess

def main():

	canvas, alphabetDict0, alphabetDict1 = setup()

	documentFile = open("document.txt", "r")

	document = documentFile.read()
	
	#Our college ruled 8.5x11
	paper = pygame.image.load("assets/paper.png")
	
	#x,y coords are top left of image
	canvas.blit(paper, (0,0))
	
	displayDocument(canvas, document, alphabetDict0, alphabetDict1)
	
	pygame.display.update()

	pygame.image.save(canvas, "output.jpeg")
	
	#Open the 8.5x11 with firefox
	bashCommand = "firefox output.jpeg"
	
	process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
	output, error = process.communicate()
	exit(0)

def displayDocument(canvas, document, alphabetDict0, alphabetDict1):
	#The total space from the start of our current horizontal line
	collectiveSpacing = 0

	#Current horizontal line
	currentLine = 0

	for char in list(document):
			
		#Pick a random dict to use for this specific char
		dictNum = random.randint(0, 1)
		if(dictNum == 0):
			alphabetDict = alphabetDict0
		elif(dictNum == 1):
			alphabetDict = alphabetDict1

		if(char in alphabetDict):
			#Adds random spacing between each letter
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
		
		#If char not in our dict, put unknown char symbol
		else:
			unknownChar = pygame.image.load("assets/unknownChar.png")
			
			canvas.blit(unknownChar, (xStart + collectiveSpacing, yStart + currentLine * lineGap - unknownChar.get_rect().size[1]))
			
			#Add a gap to compensate for the image length
			collectiveSpacing += unknownChar.get_rect().size[0]


if __name__ == '__main__':
	main()