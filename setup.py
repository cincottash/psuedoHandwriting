import pygame

from globals import canvasWidth, canvasHeight

def setup():

	pygame.init()

	canvas = pygame.display.set_mode((canvasWidth, canvasHeight))

	alphabetDict = {
	
	"a": pygame.image.load("assets/a.png"),
	"b": pygame.image.load("assets/b.png"),
	"c": pygame.image.load("assets/c.png"),
	"d": pygame.image.load("assets/d.png"),
	"e": pygame.image.load("assets/e.png"),
	"f": pygame.image.load("assets/f.png"),
	"g": pygame.image.load("assets/g.png"),
	"h": pygame.image.load("assets/h.png"),
	"i": pygame.image.load("assets/i.png"),
	"j": pygame.image.load("assets/j.png"),
	"k": pygame.image.load("assets/k.png"),
	"l": pygame.image.load("assets/l.png"),
	"m": pygame.image.load("assets/m.png"),
	"n": pygame.image.load("assets/n.png"),
	"o": pygame.image.load("assets/o.png"),
	"p": pygame.image.load("assets/p.png"),
	"q": pygame.image.load("assets/q.png"),
	"r": pygame.image.load("assets/r.png"),
	"s": pygame.image.load("assets/s.png"),
	"t": pygame.image.load("assets/t.png"),
	"u": pygame.image.load("assets/u.png"),
	"v": pygame.image.load("assets/v.png"),
	"w": pygame.image.load("assets/w.png"),
	"x": pygame.image.load("assets/x.png"),
	"y": pygame.image.load("assets/y.png"),
	"z": pygame.image.load("assets/z.png")

	}

	return canvas, alphabetDict