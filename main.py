from PIL import Image


def get_horizontal_cropping(rowheight, img):
    imglist = []
    left_upper_x = 0
    left_upper_y = 0
    right_lower_x = img.width
    right_lower_y = rowheight
    remaining = img.height - rowheight
    print("({0}, {1}, {2}, {3})".format(left_upper_x, left_upper_y, right_lower_x, right_lower_y))
    imglist.append(img.crop((left_upper_x, left_upper_y, right_lower_x, right_lower_y)))

    while remaining > 0:
        left_upper_y += rowheight
        right_lower_y += rowheight
        remaining -= rowheight
        if remaining < 0:
            print("less than 0 - using remaining")
            print("({0}, {1}, {2}, {3})".format(left_upper_x, left_upper_y, right_lower_x, img.height))
            imglist.append(img.crop((left_upper_x, left_upper_y, right_lower_x, img.height)))
            break
        print("({0}, {1}, {2}, {3})".format(left_upper_x, left_upper_y, right_lower_x, right_lower_y))
        imglist.append(img.crop((left_upper_x, left_upper_y, right_lower_x, right_lower_y)))

    return imglist


def main():
    img = Image.open("mercy.png")
    imglist = get_horizontal_cropping(200, img)

    for pic in imglist:
        pic.show()

if __name__ == "__main__":
    # call main fuction
    main()
    exit(0)