from setup import *
from globals import *
import random
import subprocess

def main():

	canvas, alphabetDict0, alphabetDict1 = setup()

	sentence = "the quick brown fox jumps over the lazy dog the quick brown fox jumps over the lazy dog the quick brown fox jumps over the lazy dog the quick brown fox jumps over the lazy dog the quick brown fox jumps over the lazy dog the quick brown fox jumps over the lazy dog "

	# while(True):
	paper = pygame.image.load("assets/paper.png")
	canvas.blit(paper, (0,0))

	
	displaySentence(canvas, sentence, alphabetDict0, alphabetDict1)
	
	pygame.display.update()

	pygame.image.save(canvas, "screenshot.jpeg")
	
	#Open the 8.5x11 with firefox
	bashCommand = "firefox screenshot.jpeg"
	
	process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
	output, error = process.communicate()
	exit(0)

def displaySentence(canvas, sentence, alphabetDict0, alphabetDict1):
	collectiveSpacing = 0
	currentLine = 0

	for char in list(sentence):
			
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
				#Move to next line
				currentLine += 1

				#Reset spacing
				collectiveSpacing = 0

				#add random margin on new line
				collectiveSpacing += random.uniform(0, 20)

			#Align to bottom of line and keep even spacing and varying height, also check if our char can go below line
			offCenterChar = 0
			if(char in offCenterCharList):
				offCenterChar = 1
			

			collectiveSpacing += letterGap
			canvas.blit(alphabetDict[char], (xStart + collectiveSpacing, yStart + offCenterChar*alphabetDict[char].get_rect().size[1]/2 + currentLine * lineGap - alphabetDict[char].get_rect().size[1]  + random.uniform(-7, 7)))
			collectiveSpacing += alphabetDict[char].get_rect().size[0]
		#It's a space
		elif(char == " "):
			collectiveSpacing += space * random.uniform(0.8, 1.5)
		#TODO: ELSE: PUT "?" CHAR THERE OR SOMETHING
		else:
			unknownChar = pygame.image.load("assets/unknownChar.png")
			canvas.blit(unknownChar, (xStart + collectiveSpacing, yStart + currentLine * lineGap - unknownChar.get_rect().size[1]))
			collectiveSpacing += unknownChar.get_rect().size[0]


if __name__ == '__main__':
	main()