import pygame

from globals import canvasWidth, canvasHeight

def setup():

	pygame.init()

	canvas = pygame.display.set_mode((canvasWidth, canvasHeight))

	alphabetDict0 = {
	
	"a": pygame.image.load("assets/a/a0.png"),
	"b": pygame.image.load("assets/b/b0.png"),
	"c": pygame.image.load("assets/c/c0.png"),
	"d": pygame.image.load("assets/d/d0.png"),
	"e": pygame.image.load("assets/e/e0.png"),
	"f": pygame.image.load("assets/f/f0.png"),
	"g": pygame.image.load("assets/g/g0.png"),
	"h": pygame.image.load("assets/h/h0.png"),
	"i": pygame.image.load("assets/i/i0.png"),
	"j": pygame.image.load("assets/j/j0.png"),
	"k": pygame.image.load("assets/k/k0.png"),
	"l": pygame.image.load("assets/l/l0.png"),
	"m": pygame.image.load("assets/m/m0.png"),
	"n": pygame.image.load("assets/n/n0.png"),
	"o": pygame.image.load("assets/o/o0.png"),
	"p": pygame.image.load("assets/p/p0.png"),
	"q": pygame.image.load("assets/q/q0.png"),
	"r": pygame.image.load("assets/r/r0.png"),
	"s": pygame.image.load("assets/s/s0.png"),
	"t": pygame.image.load("assets/t/t0.png"),
	"u": pygame.image.load("assets/u/u0.png"),
	"v": pygame.image.load("assets/v/v0.png"),
	"w": pygame.image.load("assets/w/w0.png"),
	"x": pygame.image.load("assets/x/x0.png"),
	"y": pygame.image.load("assets/y/y0.png"),
	"z": pygame.image.load("assets/z/z0.png")

	}

	alphabetDict1 = {
	
	"a": pygame.image.load("assets/a/a1.png"),
	"b": pygame.image.load("assets/b/b1.png"),
	"c": pygame.image.load("assets/c/c1.png"),
	"d": pygame.image.load("assets/d/d1.png"),
	"e": pygame.image.load("assets/e/e1.png"),
	"f": pygame.image.load("assets/f/f1.png"),
	"g": pygame.image.load("assets/g/g1.png"),
	"h": pygame.image.load("assets/h/h1.png"),
	"i": pygame.image.load("assets/i/i1.png"),
	"j": pygame.image.load("assets/j/j1.png"),
	"k": pygame.image.load("assets/k/k1.png"),
	"l": pygame.image.load("assets/l/l1.png"),
	"m": pygame.image.load("assets/m/m1.png"),
	"n": pygame.image.load("assets/n/n1.png"),
	"o": pygame.image.load("assets/o/o1.png"),
	"p": pygame.image.load("assets/p/p1.png"),
	"q": pygame.image.load("assets/q/q1.png"),
	"r": pygame.image.load("assets/r/r1.png"),
	"s": pygame.image.load("assets/s/s1.png"),
	"t": pygame.image.load("assets/t/t1.png"),
	"u": pygame.image.load("assets/u/u1.png"),
	"v": pygame.image.load("assets/v/v1.png"),
	"w": pygame.image.load("assets/w/w1.png"),
	"x": pygame.image.load("assets/x/x1.png"),
	"y": pygame.image.load("assets/y/y1.png"),
	"z": pygame.image.load("assets/z/z1.png")

	}

	return canvas, alphabetDict0, alphabetDict1