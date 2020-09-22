import pyautogui as pag
from pyscreeze import screenshot, pixelMatchesColor
from time import sleep, perf_counter, time_ns
# from pyscreenshot import grab

COLORS = ("blue", "yellow", "white", "red")

### SETUP START ###
def get_cursor_info():
	cursor_xy = pag.position()
	pixel_color = screenshot().getpixel(cursor_xy)
	pixel_color = [pixel_color[i] for i in range(3)]
	print(cursor_xy, pixel_color)
### SETUP END ###

def get_pixel_color(x, y):
	pixel_color = screenshot(region=(730, 632, 243, 235)).getpixel((x, y))  # (left, top, width, height)
	# pixel_color = grab(bbox=(730, 632, 973, 867)).getpixel((x, y))  # (x1, y1, x2, y2)
	return tuple(pixel_color[i] for i in range(3))


def click_pattern(real_btns, pattern):
	for color in pattern:
		pag.click(x=real_btns[color][0], y=real_btns[color][1])
		sleep(0.223)
	pag.moveTo(900, 735)


def create_pattern(box_btns, real_btns, stage):
	count = 0
	pattern = []
	while count < stage:
		for color in COLORS:
			btn_color = get_pixel_color(box_btns[color][0][0], box_btns[color][0][1])
			if box_btns[color][1] != btn_color:
				pattern.append(color)
				count += 1
				while not pixelMatchesColor(real_btns[color][0], real_btns[color][1], box_btns[color][1]):
					pass
				break
	return pattern


def main(limit=57):
	real_btns = {}  # real_btns[color] = (x, y)
	real_btns["blue"] = (731, 754)
	real_btns["yellow"] = (854, 633)
	real_btns["white"] = (972, 739)
	real_btns["red"] = (842, 866)
	# xy positions according to new screenshot box: (730, 632, 973, 867)
	box_btns = {}  # box_btns[color] = ((rel_x, rel_y), red)
	box_btns["blue"] = ((1, 122), (27, 49, 99))
	box_btns["yellow"] = ((124, 1), (179, 199, 133))
	box_btns["white"] = ((242, 107), (203, 130, 128))
	box_btns["red"] = ((112, 234), (199, 51, 69))

	for stage in range(1, limit+1):
		pattern = create_pattern(box_btns, real_btns, stage)
		sleep(1.97)
		click_pattern(real_btns, pattern)
	print("done")


if __name__ == '__main__':
	# get_cursor_info()
	main()
