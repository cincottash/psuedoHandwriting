from setup import *
from globals import *
import random
import subprocess

def main():

	canvas, alphabetDict = setup()

	sentence = "this is a test"

	# while(True):
	paper = pygame.image.load("assets/paper.png")
	canvas.blit(paper, (0,0))

	
	displaySentence(canvas, sentence, alphabetDict)
	
	#pygame.display.update()

	pygame.image.save(canvas, "screenshot.jpeg")
	
	#Open the 8.5x11 with firefox
	bashCommand = "firefox screenshot.jpeg"
	
	process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
	output, error = process.communicate()
	exit(0)




def displaySentence(canvas, sentence, alphabetDict):
	collectiveSpacing = 0
	for char in list(sentence):
		if(char in alphabetDict):
			#Align to bottom of line and keep even spacing
			canvas.blit(alphabetDict[char], (canvasWidth/6 + collectiveSpacing, canvasHeight/6 - alphabetDict[char].get_rect().size[1]))
			collectiveSpacing += spacing + alphabetDict[char].get_rect().size[0]
		#It's a space
		else:
			collectiveSpacing += spacing * 3

if __name__ == '__main__':
	main()