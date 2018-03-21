from PIL import Image


def get_vertical_cropping(columnwidth, img):
    imglist = []
    left_upper_x = 0
    left_upper_y = 0
    right_lower_x = columnwidth
    right_lower_y = img.height
    remaining = img.width - columnwidth
    imglist.append(img.crop((left_upper_x, left_upper_y, right_lower_x, right_lower_y)))

    while remaining > 0:
        left_upper_x += columnwidth
        right_lower_x += columnwidth
        remaining -= columnwidth
        if remaining < 0:
            # print("less than 0 - using remaining")
            # print("({0}, {1}, {2}, {3})".format(left_upper_x, left_upper_y, img.width, right_lower_y))
            # imglist.append(img.crop((left_upper_x, left_upper_y, img.width, right_lower_y)))
            break
        # print("({0}, {1}, {2}, {3})".format(left_upper_x, left_upper_y, right_lower_x, right_lower_y))
        imglist.append(img.crop((left_upper_x, left_upper_y, right_lower_x, right_lower_y)))

    return imglist


def get_horizontal_cropping(rowheight, img):
    imglist = []
    left_upper_x = 0
    left_upper_y = 0
    right_lower_x = img.width
    right_lower_y = rowheight
    remaining = img.height - rowheight
    # print("({0}, {1}, {2}, {3})".format(left_upper_x, left_upper_y, right_lower_x, right_lower_y))
    imglist.append(img.crop((left_upper_x, left_upper_y, right_lower_x, right_lower_y)))

    while remaining > 0:
        left_upper_y += rowheight
        right_lower_y += rowheight
        remaining -= rowheight
        if remaining < 0:
            # print("less than 0 - using remaining")
            # print("({0}, {1}, {2}, {3})".format(left_upper_x, left_upper_y, right_lower_x, img.height))
            # imglist.append(img.crop((left_upper_x, left_upper_y, right_lower_x, img.height)))
            break
        # print("({0}, {1}, {2}, {3})".format(left_upper_x, left_upper_y, right_lower_x, right_lower_y))
        imglist.append(img.crop((left_upper_x, left_upper_y, right_lower_x, right_lower_y)))

    return imglist


def stitch_horizontal(imglist):
    if imglist.__len__() <= 0:
        exit(1)

    # for horizontal images
    stitch_width = imglist[0].width * 2

    stitch_height = 0
    for pic in imglist:
        stitch_height += pic.height
    stitch_height = stitch_height / 2

    # make new image with twice the width and half the height as the original
    stitch = Image.new('RGB', (stitch_width.__int__(), stitch_height.__int__()), 0)
    # stitch.show()

    left = 0
    right = 0

    for i in range(0, imglist.__len__()):
        if i % 2 == 0:
            stitch.paste(imglist[i], (0, (imglist[i].height * left)))
            left += 1
            # stitch.show()
        else:

            stitch.paste(imglist[i], ((stitch_width / 2).__int__(), (imglist[i].height * right)))
            right += 1

    return stitch


def stitch_vertical(imglist):
    if imglist.__len__() <= 0:
        exit(1)

    # vertical cropped
    stitch_height = (imglist[0].height * 2).__int__()

    stitch_width = 0
    for pic in imglist:
        stitch_width += pic.width
    stitch_width = (stitch_width / 2).__int__()

    # make a new image to store the cropped pieces
    stitch = Image.new('RGB', (stitch_width, stitch_height), 0)

    top = 0
    bottom = 0
    for i in range(0, imglist.__len__()):
        if i % 2 == 0:
            stitch.paste(imglist[i], ((imglist[i].width * top), 0))
            top += 1
        else:
            stitch.paste(imglist[i], ((imglist[i].width * bottom), (stitch_height / 2).__int__()))
            bottom += 1

    return stitch


def convert_to_pixelated(cropsize, img):
    imglist = get_horizontal_cropping(cropsize, img)
    stitch = stitch_horizontal(imglist)
    imglist = get_vertical_cropping(cropsize, stitch)
    stitch = stitch_vertical(imglist)
    return stitch


def main():
    img = Image.open("mercy.png")
    stitched = convert_to_pixelated(1, img)
    stitched.show()


if __name__ == "__main__":
    # call main function
    main()
    exit(0)