alien = Actor('alien')
alien.pos = 100, 56

WIDTH = 500
HEIGHT = alien.height + 20
alien.topright = 0, 10

def draw():
	screen.clear()
	alien.draw()

def update():
	alien.left += 2
	alien.angle += 1
	if alien.left > WIDTH:
		alien.right = 0

def on_mouse_down(pos):
	if alien.collidepoint(pos):
		set_alien_hurt()

def set_alien_hurt():
	alien.image = 'alien_hurt'
	sounds.eep.play()
	clock.schedule_unique(set_alien_normal, 1.0)
	print("Voltando pro mito do normal em um segundo! :)")

def set_alien_normal():
	alien.image = 'alien'
