def grayscale(im):
    '''Convert the PIL image to grayscale'''
    if im.mode != "L":
        im = im.convert("L")
    return im

def topcrop320(img):
	box = (0,0,320,250)
	img = img.crop(box)
	return img