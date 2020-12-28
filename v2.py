import pyautogui as pag
from pyscreeze import screenshot
from time import sleep, perf_counter

BOTTLE_POSITION = {"color_position": (1750, 490), (122, 116, 99): "left_bottle", (99, 44, 14): "mid_bottle", (90, 39, 13): "right_bottle"}

### SETUP START ###
def get_cursor_info():
	cursor_xy = pag.position()
	pixel_color = screenshot().getpixel(cursor_xy)
	pixel_color = [pixel_color[i] for i in range(3)]
	print(cursor_xy, pixel_color)
### SETUP END ###

def get_pixel_color(xy):
	''' xy is tuple '''
	return screenshot().getpixel(xy)


def get_bottle(pos):
	''' pos is tuple '''
	try:
		if get_pixel_color(pos) in BOTTLE_POSITION:
			return BOTTLE_POSITION[get_pixel_color(pos)]
	except:
		return None
		print("phew")
	return None


def toss_left():
	pag.mouseDown(button='left', x=945, y=890)
	pag.mouseUp(button='left', x=945, y=585)


def toss_mid_right():
	pag.mouseDown(button='left', x=945, y=890)
	pag.mouseUp(button='left', x=945, y=540)


def main():
	try:
		stuck = 0
		while stuck <= 15:
			bottle = get_bottle(BOTTLE_POSITION["color_position"])
			if bottle == "left_bottle":
				stuck = 0
				toss_left()
			elif bottle in ["mid_bottle", "right_bottle"]:
				stuck = 0
				toss_mid_right()
			else:
				print("on the move")
				stuck += 1
				sleep(0.15)
	except KeyboardInterrupt:
		print("Done")


if __name__ == '__main__':
	# get_cursor_info()
	main()
	
