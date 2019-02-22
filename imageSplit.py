import argparse
import os
from PIL import Image, ImageDraw, ImageFont
import math

font = ImageFont.truetype('Roboto-Bold.ttf', size=14)

DIMENSIONS = {
    "A4": [8.27, 11.69],
    "A3": [11.69, 16.53]
}

# TODO:
# this process needs to be improved
# steps of the algorithm:
# (1) get the size of one grid square in px
# (2) get the desired dpi i.e 100 dpi
# (3) scale the picture by dpi / size
# (4) now each cell of the picture will be exactly one inch wide
# (5) now create multiple pages from the image an A4 page is 8.27 x 11.69 inches


def flood_fill(data, size, start, expected=(0, 0, 0), fill=(255, 255,255)):
    # start should be x, y
    x, y = start
    imx, imy = size
    neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    for n in neighbors:
        x, y = n
        if 0 < x < imx and 0 < y < imy:
            pos_color = data[x, y]
            if pos_color == expected:
                data[x, y] = fill
                neighbors += [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        # add neighbors


def calc_size_in_px(dpi, format):
    return dpi * format[0], dpi * format[1]


def calc_scaling_factor(dpi, size):
    # the scaling factor is the size increase or decrease
    # relative to the images desired dpi, with this scale factor each cell of the image should be 1 inch wide
    # ex: size = 50 dpi = 300, scale = 300/50 = 6
    return dpi / size


def scale_tuple2(t, scale, to_int=False):
    # multiplies 2 elements of t with scale
    res = t[0] * scale, t[1] * scale
    if to_int:
        return int(res[0]), int(res[1])
    return res


def scale_image(image, desired_dpi, size):
    scaled = scale_tuple2(image.size, calc_scaling_factor(desired_dpi, size), to_int=True)
    print("scaling original image to", scaled)
    return image.resize(scaled, Image.ANTIALIAS)


def subdivide_image(image, desired_dpi, size, format):
    # create a image array at format (i.e A4) in which each cell is 1 inch
    # image should be the upscaled original image
    # the return value is [(region xpos, ypos) ...]
    arr = []
    scale_factor = calc_scaling_factor(desired_dpi, size)
    format_in_px = scale_tuple2(format, desired_dpi)  # this is the size of an a4 page
    x_pages = image.size[0] / format_in_px[0]
    y_pages = image.size[1] / format_in_px[1]
    print("subdividing image into pages")
    print("scale factor", scale_factor)
    print("format in px", format_in_px)
    print("original image size", image.size)
    print("there will be ", math.ceil(x_pages + y_pages), "pages")
    for i in range(int(math.ceil(x_pages))):
        for j in range(int(math.ceil(y_pages))):
            box = (
                (0 + i) * format_in_px[0],
                (0 + j) * format_in_px[1],
                (1 + i) * format_in_px[0],
                (1 + j) * format_in_px[1]
            )
            print("cropping ", box)
            region = image.crop(box)
            min_pix = region.size[0] - 1, region.size[1] - 1
            flood_fill(region.load(), region.size, min_pix)
            arr += [(region, i, j)]
    return arr


def create_pdf(images, outdir, desired_dpi=300, page_numbers=True):
    if page_numbers:
        for p in images:
            image, i, j = p
            draw = ImageDraw.Draw(image)
            text = "p:" + str(i + j) + "x:" + str(j) + "y:" + str(i)
            size = font.getsize(text)
            bgx, bgy = size
            bgx += 5
            bgy += 5
            draw.rectangle(((35, 35), (40 + bgx, 40 + bgy)), fill="rgb(0, 0, 0)")
            draw.text((40, 40), text=text, fill="rgb(255, 255, 255)", font=font)
            image.save(outdir + "/page(" + str(i) + "_" + str(j) + ").png", dpi=(desired_dpi, desired_dpi))

    if len(images) > 1:
        images[0][0].save(
            outdir + "/result.pdf",
            dpi=(desired_dpi, desired_dpi),
            save_all=True,
            append_images=list(map(lambda x: x[0], images[1:]))
        )


def stitch(image, outdir, frmt, size, page_numbers=True, desired_dpi=300):
    scaled_image = scale_image(image, desired_dpi, size)
    images = subdivide_image(scaled_image, desired_dpi, size, frmt)
    create_pdf(images, outdir, desired_dpi, page_numbers)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("infile", help="the input file to read from")
    parser.add_argument("-s", "--size", help="the size of a single tile in the map given in pixels")
    parser.add_argument("-o", "--out",  help="the out directory to write to")
    parser.add_argument("-f", "--format", help="the format of the outfile, one of 'A4', 'A5'")
    parser.add_argument(
        "-n",
        "--numbers",
        action="store_false",
        help= "if this is option is present it will include page numbers",
    )
    parser.add_argument(
        "-d",
        "--dpi",
        type=int,
        nargs="?",
        default=100,
        const=100,
        help="the desired output dpi, default 100",
    )
    args = parser.parse_args()

    try:
        curdir = os.getcwd()
        outdir = args.out
        format = args.format
        infile = args.infile
        size = int(args.size)
        if format in DIMENSIONS:
            format = DIMENSIONS[format]
        else:
            print("Error: the format", format, "is not supported, supported formats are", str(DIMENSIONS.keys())[11:-2])
            return
    except KeyError as k:
        print("command is mission arguments")
        print(k)
        return

    if os.path.isfile(infile):
        pass
    elif os.path.isfile(curdir + "/" + infile):
        infile = curdir + "/" + infile
    else:
        print("Error: infile does not exist!\nAborting.")
        return

    outpath = curdir + "/" + outdir
    if os.path.exists(outpath):
        inp = input("do you want to override " + outpath + " ? [y/N]")
        if inp.lower() == "y":
            os.rmdir(outpath)
        else:
            print("writing files to ", outpath)
    else:
        os.mkdir(outpath)
        print("dir created ...")
    print("dpi = ", args.dpi)
    stitch(Image.open(infile), outpath, format, size, page_numbers=args.numbers, desired_dpi=100)







if __name__ == '__main__':
    main()
