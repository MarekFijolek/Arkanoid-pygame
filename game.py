#----------------------------------------------
# importing libraries and initializing pygame:
#----------------------------------------------

import pygame, sys
pygame.init()

#----------------------------------------------
# defining functions (descriptions are within each one):
#----------------------------------------------
def level_1(tile):
	'''This is level 1, just single line of bricks
	The function returns amount of tiles, which will be useful later in function which actually
	chooses which level should be played'''
	global tile_rect
	tiles_amount = 13
	for n in range(tiles_amount):
		tile_rect.append(tile.get_rect())
		tile_rect[n].midtop = (75 + n * 100, 200)
	return tiles_amount

def level_2(tile):
	'''This is level 2, two lines of bricks'''
	global tile_rect
	tiles_amount = 26
	for n in range(tiles_amount/2):
		tile_rect.append(tile.get_rect())
		tile_rect[n].midtop = (75 + n * 100, 200)
	x=0
	for n in range(tiles_amount/2,tiles_amount):
		tile_rect.append(tile.get_rect())
		tile_rect[n].midtop = (75 + x * 100, 250)
		x+=1
	return tiles_amount

def level_3(tile):
	'''This is level 3, hand-made writing "CS" '''
	global tile_rect
	tiles_amount = 20
	tile_rect.append(tile.get_rect())
	tile_rect[0].midtop = (400, 150)
	tile_rect.append(tile.get_rect())
	tile_rect[1].midtop = (300, 150)
	tile_rect.append(tile.get_rect())
	tile_rect[2].midtop = (250, 200)
	tile_rect.append(tile.get_rect())
	tile_rect[3].midtop = (250, 250)
	tile_rect.append(tile.get_rect())
	tile_rect[4].midtop = (250, 300)
	tile_rect.append(tile.get_rect())
	tile_rect[5].midtop = (250, 350)
	tile_rect.append(tile.get_rect())
	tile_rect[6].midtop = (250, 400)
	tile_rect.append(tile.get_rect())
	tile_rect[7].midtop = (300, 450)
	tile_rect.append(tile.get_rect())
	tile_rect[8].midtop = (400, 450)
	tile_rect.append(tile.get_rect())
	tile_rect[9].midtop = (1100, 150)
	tile_rect.append(tile.get_rect())
	tile_rect[10].midtop = (1000, 150)
	tile_rect.append(tile.get_rect())
	tile_rect[11].midtop = (900, 150)
	tile_rect.append(tile.get_rect())
	tile_rect[12].midtop = (900, 200)
	tile_rect.append(tile.get_rect())
	tile_rect[13].midtop = (900, 250)
	tile_rect.append(tile.get_rect())
	tile_rect[14].midtop = (1000, 300)
	tile_rect.append(tile.get_rect())
	tile_rect[15].midtop = (1100, 350)
	tile_rect.append(tile.get_rect())
	tile_rect[16].midtop = (1100, 400)
	tile_rect.append(tile.get_rect())
	tile_rect[17].midtop = (1100, 450)
	tile_rect.append(tile.get_rect())
	tile_rect[18].midtop = (1000, 450)
	tile_rect.append(tile.get_rect())
	tile_rect[19].midtop = (900, 450)
	tile_rect.append(tile.get_rect())
	return tiles_amount

def level_4(tile):
	'''This is level 3, hand-made writing "IFE" '''
	global tile_rect
	tiles_amount = 20
	tile_rect.append(tile.get_rect())
	tile_rect[0].midtop = (300, 150)
	tile_rect.append(tile.get_rect())
	tile_rect[1].midtop = (300, 200)
	tile_rect.append(tile.get_rect())
	tile_rect[2].midtop = (300, 250)
	tile_rect.append(tile.get_rect())
	tile_rect[3].midtop = (300, 300)
	tile_rect.append(tile.get_rect())
	tile_rect[4].midtop = (300, 350)
	tile_rect.append(tile.get_rect())
	tile_rect[5].midtop = (600, 150)
	tile_rect.append(tile.get_rect())
	tile_rect[6].midtop = (600, 200)
	tile_rect.append(tile.get_rect())
	tile_rect[7].midtop = (600, 250)
	tile_rect.append(tile.get_rect())
	tile_rect[8].midtop = (600, 300)
	tile_rect.append(tile.get_rect())
	tile_rect[9].midtop = (600, 350)
	tile_rect.append(tile.get_rect())
	tile_rect[10].midtop = (700, 150)
	tile_rect.append(tile.get_rect())
	tile_rect[11].midtop = (700, 250)
	tile_rect.append(tile.get_rect())
	tile_rect[12].midtop = (1000, 150)
	tile_rect.append(tile.get_rect())
	tile_rect[13].midtop = (1000, 200)
	tile_rect.append(tile.get_rect())
	tile_rect[14].midtop = (1000, 250)
	tile_rect.append(tile.get_rect())
	tile_rect[15].midtop = (1000, 300)
	tile_rect.append(tile.get_rect())
	tile_rect[16].midtop = (1000, 350)
	tile_rect.append(tile.get_rect())
	tile_rect[17].midtop = (1100, 150)
	tile_rect.append(tile.get_rect())
	tile_rect[18].midtop = (1100, 250)
	tile_rect.append(tile.get_rect())
	tile_rect[19].midtop = (1100, 350)
	tile_rect.append(tile.get_rect())
	return tiles_amount

def level_5(tile):
	'''This is level 5, the hardest, hand-made writing "PYTH !". It's not full PYTHON because lack of space'''
	global tile_rect
	tiles_amount = 36
	tile_rect.append(tile.get_rect())
	tile_rect[0].midtop = (50, 150)
	tile_rect.append(tile.get_rect())
	tile_rect[1].midtop = (50, 200)
	tile_rect.append(tile.get_rect())
	tile_rect[2].midtop = (50, 250)
	tile_rect.append(tile.get_rect())
	tile_rect[3].midtop = (50, 300)
	tile_rect.append(tile.get_rect())
	tile_rect[4].midtop = (50, 350)
	tile_rect.append(tile.get_rect())
	tile_rect[5].midtop = (150, 150)
	tile_rect.append(tile.get_rect())
	tile_rect[6].midtop = (200, 200)
	tile_rect.append(tile.get_rect())
	tile_rect[7].midtop = (150, 250)
	tile_rect.append(tile.get_rect())
	tile_rect[8].midtop = (325, 150)
	tile_rect.append(tile.get_rect())
	tile_rect[9].midtop = (450, 150)
	tile_rect.append(tile.get_rect())
	tile_rect[10].midtop = (340, 200)
	tile_rect.append(tile.get_rect())
	tile_rect[11].midtop = (435, 200)
	tile_rect.append(tile.get_rect())
	tile_rect[12].midtop = (385, 250)
	tile_rect.append(tile.get_rect())
	tile_rect[13].midtop = (385, 300)
	tile_rect.append(tile.get_rect())
	tile_rect[14].midtop = (385, 350)
	tile_rect.append(tile.get_rect())
	tile_rect[15].midtop = (575, 150)
	tile_rect.append(tile.get_rect())
	tile_rect[16].midtop = (675, 150)
	tile_rect.append(tile.get_rect())
	tile_rect[17].midtop = (625, 200)
	tile_rect.append(tile.get_rect())
	tile_rect[18].midtop = (625, 250)
	tile_rect.append(tile.get_rect())
	tile_rect[19].midtop = (625, 300)
	tile_rect.append(tile.get_rect())
	tile_rect[20].midtop = (625, 350)
	tile_rect.append(tile.get_rect())
	tile_rect[21].midtop = (800, 150)
	tile_rect.append(tile.get_rect())
	tile_rect[22].midtop = (800, 200)
	tile_rect.append(tile.get_rect())
	tile_rect[23].midtop = (800, 250)
	tile_rect.append(tile.get_rect())
	tile_rect[24].midtop = (800, 300)
	tile_rect.append(tile.get_rect())
	tile_rect[25].midtop = (800, 350)
	tile_rect.append(tile.get_rect())
	tile_rect[26].midtop = (900, 250)
	tile_rect.append(tile.get_rect())
	tile_rect[27].midtop = (1000, 150)
	tile_rect.append(tile.get_rect())
	tile_rect[28].midtop = (1000, 200)
	tile_rect.append(tile.get_rect())
	tile_rect[29].midtop = (1000, 250)
	tile_rect.append(tile.get_rect())
	tile_rect[30].midtop = (1000, 300)
	tile_rect.append(tile.get_rect())
	tile_rect[31].midtop = (1000, 350)
	tile_rect.append(tile.get_rect())
	tile_rect[32].midtop = (1300, 150)
	tile_rect.append(tile.get_rect())
	tile_rect[33].midtop = (1300, 200)
	tile_rect.append(tile.get_rect())
	tile_rect[34].midtop = (1300, 250)
	tile_rect.append(tile.get_rect())
	tile_rect[35].midtop = (1300, 350)
	tile_rect.append(tile.get_rect())
	return tiles_amount

def which_level_and_tiles_amount(level,tile):
	''' Purpose of this function is to determine which level should be played based on user's advance through the
	game stored in a file
	Function returns amount of tiles along with creating tiles (by using level_x functions)'''
	if level == 1: return level_1(tile)
	elif level == 2: return level_2(tile)
	elif level == 3: return level_3(tile)
	elif level == 4: return level_4(tile)
	else: return level_5(tile)

def paddle_borders_check_singleplayer(p_left,w_left,p_right,w_right):
	''' This function cheks if the paddle is within the frame/game window'''
	if p_right > w_right:
		paddle.right = win.right
	if p_left < w_left:
		paddle.left = win.left

def ball_movement_borders(b_right,b_top,b_left,w_top,w_left,w_right,vec):
	''' This function is responsible for keeping ball within frame/game window'''
	if b_right > w_right or b_left < w_left:
		vec[0] = -vec[0]
	if b_top < w_top:
		vec[1] = -vec[1]

def ball_hit_paddle_singleplayer(b_bottom,p_top,b_cent,p_cent,b_w,p_w,vec):
	''' This function describes what happens when the ball hits the paddle
	Depenging on a place on a paddle the ball can be launched on different angles'''
	global point
	if b_bottom > p_top and abs(b_cent-p_cent) < (b_w+p_w)/2:
		if abs(b_cent-p_cent) < b_w/10:
			vec[0] = 0
			vec[1] = -3
		elif abs(b_cent-p_cent) < b_w/5:
			if b_cent-p_cent > 0:
				vec[0] = 1
			else:
				vec[0] = -1
			vec[1] = -vec[1]
		elif abs(b_cent-p_cent) < b_w/3:
			if b_cent-p_cent > 0:
				vec[0] = 2
			else:
				vec[0] = -2
			vec[1] = -vec[1]
		elif abs(b_cent-p_cent) < b_w/1.5:
			if b_cent-p_cent > 0:
				vec[0] = 3
			else:
				vec[0] = -3
			vec[1] = -vec[1]
		else:
			if b_cent-p_cent > 0:
				vec[0] = 4
			else:
				vec[0] = -4
			vec[1] = -vec[1]

def lose_game(b_bottom,w_bottom):
	''' This function defines what happens after player don't manage to hit the ball with the paddle'''
	if b_bottom <= w_bottom:
		return "endscreen"
	else: return "game"

def ball_hit_tile(tile, n):
	''' This function is repsonsible for detecting collision of ball with tile and if it hits from top/bottom
	or sides'''
	global tiles_destroyed
	if ball.colliderect(tile):
		col_tl = (ball.topleft[0]+4,ball.topleft[1]) # col_tl is a topleft point of ball plus four because sometimes
		# it seems that the function don't detect the collision immediately
		col_tr = (ball.topright[0] - 4, ball.topright[1])
		col_bl = (ball.bottomleft[0] + 4, ball.bottomleft[1])
		col_br = (ball.bottomright[0] - 4, ball.bottomright[1])
		if  tile.collidepoint(col_tl)==True or tile.collidepoint(col_tr)==True or \
						tile.collidepoint(col_bl)==True or tile.collidepoint(col_br)==True:
			# this means that the colliding point is inside the tile so this is hit from top or bottom
			vec[1] = -vec[1]
		else:
			vec[0] = -vec[0]
		tile_hit[n] = True # saving that the tile has been hit
		tiles_destroyed+=1 # adding 1 to the counter of how many tiles have been destroyed

#----------------------------------------------
# defining colors
#----------------------------------------------

black = (0, 0, 0); white = (255, 255, 255); background = (10,10,10)

#----------------------------------------------
# defining variables:
#----------------------------------------------

winsize=(1366,768) # size of the window
game_status = "menu" # this determines if you're in menus or game
scr = pygame.display.set_mode(winsize,pygame.FULLSCREEN) # defining game window
win = scr.get_rect() # creating the game window
fps = pygame.time.Clock() # frames per second amount
pygame.key.set_repeat(10,10) # repetition of keys during long press
ball_start_at_paddle = True # if True then the ball is at paddle and the game haven't started
ball_moves = False # if False than the ball doesn't move yet (it's on the paddle)
tiles_amount = tiles_destroyed = 0 # counters of tiles and tiles destroyed
tile_rect=[] # empty array which will be later filled with rectangles of tiles

#----------------------------------------------
# loading images, creating rectangles from them and describing positions of those rectangles
#----------------------------------------------

ball_image = pygame.image.load("Res/ball.png").convert_alpha()
paddle_image = pygame.image.load("Res/paddle.png").convert_alpha()
tile = pygame.image.load("Res/tile.png").convert_alpha()
button = pygame.image.load("Res/button.png").convert_alpha()
exitmenu_button = pygame.image.load("Res/exitmenu_button.png").convert_alpha()
menu = pygame.image.load("Res/menu.png").convert_alpha()
end = pygame.image.load("Res/end.png").convert_alpha()
won = pygame.image.load("Res/won.png").convert_alpha()
restart_button = pygame.image.load("Res/restartbutton.png").convert_alpha()
menu_button = pygame.image.load("Res/menubutton.png").convert_alpha()
exit_button = pygame.image.load("Res/escbutton.png").convert_alpha()

start_small = pygame.image.load("Res/start_small.png").convert_alpha()
start_big = pygame.image.load("Res/start_big.png").convert_alpha()
exitmenu_small = pygame.image.load("Res/exitmenu_small.png").convert_alpha()
exitmenu_big = pygame.image.load("Res/exitmenu_big.png").convert_alpha()
restart_small = pygame.image.load("Res/restart_small.png").convert_alpha()
restart_big = pygame.image.load("Res/restart_big.png").convert_alpha()
menu_small = pygame.image.load("Res/menu_small.png").convert_alpha()
menu_big = pygame.image.load("Res/menu_big.png").convert_alpha()
exit_small = pygame.image.load("Res/exit_small.png").convert_alpha()
exit_big = pygame.image.load("Res/exit_big.png").convert_alpha()
continue_small = pygame.image.load("Res/continue_small.png").convert_alpha()
continue_big = pygame.image.load("Res/continue_big.png").convert_alpha()



ball = ball_image.get_rect()
paddle = paddle_image.get_rect()
menu_rect = menu.get_rect()
button_rect = button.get_rect()
exitmenu_button_rect = exitmenu_button.get_rect()
end_rect = end.get_rect()
won_rect = won.get_rect()
restart_button_rect = restart_button.get_rect()
menu_button_rect = menu_button.get_rect()
exit_button_rect = exit_button.get_rect()

start_small_rect = start_small.get_rect()
start_big_rect = start_big.get_rect()
exitmenu_small_rect = exitmenu_small.get_rect()
exitmenu_big_rect = exitmenu_big.get_rect()
restart_small_rect = restart_small.get_rect()
restart_big_rect = restart_big.get_rect()
menu_small_rect = menu_small.get_rect()
menu_big_rect = menu_big.get_rect()
exit_small_rect = exit_small.get_rect()
exit_big_rect = exit_big.get_rect()
continue_small_rect = continue_small.get_rect()
continue_big_rect = continue_big.get_rect()

paddle.midbottom = win.midbottom
ball.midbottom = paddle.midtop
menu_rect.center = win.center
button_rect.center = win.center
exitmenu_button_rect.center = (1183,86)
end_rect.center = win.center
won_rect.center = win.center
restart_button_rect.center = (691,496)
menu_button_rect.center = (252,513)
exit_button_rect.center = (1220,590)

start_small_rect.center = start_big_rect.center = win.center
exitmenu_small_rect.center = exitmenu_big_rect.center = win.center
restart_big_rect.center = restart_small_rect.center = (740,395)
menu_big_rect.center = menu_small_rect.center = (338,276)
exit_big_rect.center = exit_small_rect.center = (1050,390)
continue_big_rect.center = continue_small_rect.center = (690,385)

#----------------------------------------------
# MAIN LOOP
#----------------------------------------------
file = open("Res/levels.txt",'r+') # opening file with the level the player is on currently
level = int(file.read()) # reading the level from file
file.close() # closing file
tiles_amount = which_level_and_tiles_amount(level,tile)
tile_hit=[] # creating empty array which will be filled with booleans determining if the tile was destroyed
for n in range (tiles_amount): # filling this array with Falses because all tiles haven't been destroyed yet
	tile_hit.append(False)

while True:

	while game_status == "menu": # player is in menu

		for event in pygame.event.get():
			if pygame.mouse.get_pressed() == (1,0,0): # if player clicks LMB
				if button_rect.collidepoint(pygame.mouse.get_pos()) == True:
					vec = [0, -3]  # first the ball moves only upwards
					step = 12  # paddle moves with step 12
					game_status = "game"  # switching status of program to GAME
				if exitmenu_button_rect.collidepoint(pygame.mouse.get_pos()) == True:
					sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE: # closing the game with ESC key
					sys.exit()
			if event.type == pygame.QUIT: # close with regular system button
				sys.exit()

		# printing menu background
		scr.blit(menu,menu_rect)

		if button_rect.collidepoint(pygame.mouse.get_pos()) == True: # if mouse cursor is on button than the font
			# is big, otherwise it's small. It's to know what option is being choosed at the moment
			scr.blit(start_big, start_big_rect)
		else:
			scr.blit(start_small, start_small_rect)

		if exitmenu_button_rect.collidepoint(pygame.mouse.get_pos()) == True:
			scr.blit(exitmenu_big, exitmenu_big_rect)
		else:
			scr.blit(exitmenu_small, exitmenu_small_rect)

		# refreshing screen
		pygame.display.flip()

		fps.tick(360)

	while game_status == "game": # player is in game
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if pygame.key.get_pressed()[pygame.K_LEFT]: # moving the paddle
					paddle = paddle.move(-step,0)
					if ball_start_at_paddle == True:
						ball = ball.move(-step,0)
				if pygame.key.get_pressed()[pygame.K_RIGHT]: # moving the paddle
					paddle = paddle.move(step,0)
					if ball_start_at_paddle == True:
						ball = ball.move(step, 0)
				if pygame.key.get_pressed()[pygame.K_ESCAPE]: # close the game with ESC key
					sys.exit()
				if pygame.key.get_pressed()[pygame.K_SPACE] and ball_start_at_paddle == True: # releasing the ball with
					# SPACE key
					ball_moves = True
					ball_start_at_paddle = False

		if ball_moves == True: # making the ball move if the ball is no longer on starting position (on paddle)
			ball = ball.move(vec)

		# using all the functions I introduced before:

		paddle_borders_check_singleplayer(paddle.left,win.left,paddle.right,win.right)

		ball_movement_borders(ball.right,ball.top,ball.left,win.top,win.left,win.right,vec)

		if ball.bottom > paddle.top - 5: # since iterating through conditions where the ball hit the paddle is
			# time consuming, it is checked only in neighbourhood of paddle
			ball_hit_paddle_singleplayer(ball.bottom,paddle.top,ball.centerx,paddle.centerx,ball.w,paddle.w,vec)
			game_status = lose_game(win.bottom,ball.bottom) # this is also here because you can't lose in other way
			# than by touching bottom of the screen

		#scr.blit(background,background_rect)
		scr.fill(background)

		# printing ball and paddles
		scr.blit(ball_image,ball)
		scr.blit(paddle_image,paddle)

		for n in range (tiles_amount): # printing the tiles
			if (tile_hit[n] == False):
				scr.blit(tile,tile_rect[n])

		if (ball.top < tile_rect[tiles_amount-1].bottom + 5): # same situation as with paddle but with tiles this time
			for n in range (tiles_amount):
				if (tile_hit[n] == False):
					ball_hit_tile(tile_rect[n],n)

		if tiles_destroyed == tiles_amount: # if all tiles are destroyed
			if level<5:
				level+=1
			file = open("Res/levels.txt", 'r+') # opening file, deleting what is there and replacing it with new value
			file.seek(0)
			file.truncate()
			file.write(str(level))
			file.close()
			game_status = "won" # going to winning screen

		# refreshing screen
		pygame.display.flip()

		# fps are set to 120 to assure smooth gameplay
		fps.tick(120)

	while game_status == "endscreen":
		for event in pygame.event.get():
			if pygame.mouse.get_pressed() == (1, 0, 0):
				if exit_button_rect.collidepoint(pygame.mouse.get_pos()) == True:  # closing the game
					sys.exit()
				if menu_button_rect.collidepoint(pygame.mouse.get_pos()) == True:  # option to return to menu
					# all those variables are in fact to reset everything to zero state
					ball.bottom = paddle.top
					ball.midbottom = (winsize[0] * 0.5, winsize[1] - paddle.height)
					ball_start_at_paddle = True
					ball_moves = False
					vec = [0, -3]
					paddle.midbottom = win.midbottom  # paddle appears in
					tiles_destroyed = 0
					point = 0
					time = 0
					tick = 0
					tile_hit = []
					for n in range(tiles_amount):
						tile_hit.append(False)
					game_status = "menu"
				if restart_button_rect.collidepoint(pygame.mouse.get_pos()) == True:  # quick restart
					ball.bottom = paddle.top
					ball.midbottom = (winsize[0] * 0.5, winsize[1] - paddle.height)
					ball_start_at_paddle = True
					ball_moves = False
					paddle.midbottom = win.midbottom
					vec = [0, -3]
					tile_hit = []
					for n in range(tiles_amount):
						tile_hit.append(False)
					tiles_destroyed = 0
					point = 0
					time = 0
					tick = 0
					game_status = "game"
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE: # closing the game
					sys.exit()
			if event.type == pygame.QUIT:
				sys.exit()

		scr.fill(black)

		# printing options and score
		scr.blit(end, end_rect)

		if restart_button_rect.collidepoint(pygame.mouse.get_pos()) == True: # if cursor is on button
			scr.blit(restart_big, restart_big_rect)
		else:
			scr.blit(restart_small, restart_small_rect)

		if menu_button_rect.collidepoint(pygame.mouse.get_pos()) == True:
			scr.blit(menu_big, menu_big_rect)
		else:
			scr.blit(menu_small, menu_small_rect)

		if exit_button_rect.collidepoint(pygame.mouse.get_pos()) == True:
			scr.blit(exit_big, exit_big_rect)
		else:
			scr.blit(exit_small, exit_small_rect)

		pygame.display.flip()
		fps.tick(120)

	while game_status == "won":  # player is in winning screen
		for event in pygame.event.get():
			if pygame.mouse.get_pressed() == (1, 0, 0):
				if restart_button_rect.collidepoint(pygame.mouse.get_pos()) == True:
					file = open("Res/levels.txt", 'r+') # determining which level to play based on progress stored in file
					level = int(file.read())
					file.close()
					tiles_amount = which_level_and_tiles_amount(level, tile)

					ball.bottom = paddle.top
					ball.midbottom = (winsize[0] * 0.5, winsize[1] - paddle.height)
					ball_start_at_paddle = True
					ball_moves = False
					paddle.midbottom = win.midbottom
					vec = [0, -3]
					tile_hit = []
					for n in range(tiles_amount):
						tile_hit.append(False)
					tiles_destroyed = 0
					point = 0
					time = 0
					tick = 0
					game_status = "game"  # switching status of program to GAME
				if exit_button_rect.collidepoint(pygame.mouse.get_pos()) == True:  # closing the game
					sys.exit()
				if menu_button_rect.collidepoint(pygame.mouse.get_pos()) == True:  # option to return to menu
					file = open("Res/levels.txt", 'r+')
					level = int(file.read())
					file.close()
					tiles_amount = which_level_and_tiles_amount(level, tile)

					ball.bottom = paddle.top
					ball.midbottom = (winsize[0] * 0.5, winsize[1] - paddle.height)
					ball_start_at_paddle = True
					ball_moves = False
					vec = [0, -3]
					paddle.midbottom = win.midbottom  # paddle appears in the centre
					tiles_destroyed = 0
					point = 0
					time = 0
					tick = 0
					tile_hit = []
					for n in range(tiles_amount):
						tile_hit.append(False)
					game_status = "menu"
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:  # closing the game with ESC key
					sys.exit()
			if event.type == pygame.QUIT:  # close with regular system button
				sys.exit()
		# printing texts on screen
		scr.blit(won, won_rect)

		if restart_button_rect.collidepoint(pygame.mouse.get_pos()) == True:
			scr.blit(continue_big, continue_big_rect)
		else:
			scr.blit(continue_small, continue_small_rect)

		if menu_button_rect.collidepoint(pygame.mouse.get_pos()) == True:
			scr.blit(menu_big, menu_big_rect)
		else:
			scr.blit(menu_small, menu_small_rect)

		if exit_button_rect.collidepoint(pygame.mouse.get_pos()) == True:
			scr.blit(exit_big, exit_big_rect)
		else:
			scr.blit(exit_small, exit_small_rect)

		# refreshing screen
		pygame.display.flip()

		fps.tick(360)