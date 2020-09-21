import pyautogui as pag
from pyscreeze import screenshot
from time import sleep, perf_counter, time_ns
# import pyscreenshot

COLORS = ("blue", "yellow", "white", "red")

### SETUP START ###
def get_cursor_info():
	cursor_xy = pag.position()
	pixel_color = screenshot().getpixel(cursor_xy)
	pixel_color = [pixel_color[i] for i in range(3)]
	print(cursor_xy, pixel_color)
### SETUP END ###

def get_pixel_color(x, y):
	pixel_color = screenshot().getpixel((x, y))
	return tuple(pixel_color[i] for i in range(3))


def click_pattern(btns, pattern):
	for color in pattern:
		pag.click(x=btns[color][0][0], y=btns[color][0][1])
		sleep(0.523)
	pag.moveTo(900, 735)


def create_pattern(btns, stage):
	count = 0
	pattern = []
	while count < stage:
		for color in COLORS:
			btn_color = get_pixel_color(btns[color][0][0], btns[color][0][1])
			if btns[color][1] != btn_color:
				pattern.append(color)
				count += 1
				sleep(0.09)
	# print(pattern[-1])
	return pattern


def main(limit=57):
	btns = {}  # btns[color] = ((x, y), (R, G, B))
	btns["blue"] = ((731, 754), (27, 49, 99))
	btns["yellow"] = ((854, 633), (179, 199, 133))
	btns["white"] = ((972, 739), (203, 130, 128))
	btns["red"] = ((842, 866), (199, 51, 69))

	for stage in range(1, limit+1):
		pattern = create_pattern(btns, stage)
		sleep(1.97)
		click_pattern(btns, pattern)
	print("done")


if __name__ == '__main__':
	# get_cursor_info()
	main()
