#!/usr/bin/python3

import random
import subprocess
import argparse
import psutil
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

format_strings = {
        "polybar"  : "%%{F%s}%s",
        "xmobar"   : "<fc=%s>%s</fc>",
        "lemonbar" : "%%{F%s}%s",
        "windows"  : "%s%s",
        "i3bar"    : "%s%s",
        "default"  : "%s%s"
    }

thresholds = [25,20,30]

bars = ["polybar","xmobar","windows","lemonbar","i3bar"]

def notify(quote, image_path = None):
    cmdlist = ["notify-send", quote, "-i", image_path]
    if(image_path == None):
        cmdlist = ["notify-send", quote]

    process = subprocess.Popen(cmdlist, stdout=subprocess.PIPE)
    _, _ = process.communicate()

def determine_colors(color):
    if(color == None):
        colors = [hex(random.randint(thresholds[i],2**8)).strip("0x").zfill(2) for i in range(3)]
        return '#' + colors[0] + colors[1] + colors[2]
    else:
        color = color.split("0x")[-1]
        color = color.split("#")[-1]
        if(len(color) != 6):
            print("Wrong color format!\nAborting")
            exit(3)
        return '#' + color


def motivate(format_string, color = None, no_color = False, image_path = None, list_path = None):
    if(image_path == None):
        image_path = os.path.join(dir_path, "..","assets","harvåd.png")
    elif(not os.path.isabs(image_path)):
        image_path = os.path.abspath(image_path)

    if(list_path == None):
        list_path = os.path.join(dir_path, "..","data","quotes.txt")

    if(no_color):
        colorstring=''
    else:
        colorstring = determine_colors(color)

    with open(list_path) as f:
        f = f.readlines()
        quote = random.choice(f).strip()
        notify(quote, image_path)

        print(format(format_string
            %(colorstring, quote)))


if __name__ == "__main__":
    parser =  argparse.ArgumentParser(description='what is this')
    parser.add_argument('--mode', help='/'.join(bars), type=str, choices=bars)
    parser.add_argument('-i', '--image-path', help='notification icon path', type=str)
    parser.add_argument('-l', '--list', help='quote list file path', type=str)

    color_group = parser.add_mutually_exclusive_group()
    color_group.add_argument('-c', '--color', help='text color', type=str)
    color_group.add_argument('-n', '--no-color', help='no text coloring', action='store_true', default=False)

    args = parser.parse_args()

    if(args.mode == None):
        parent = psutil.Process(psutil.Process().ppid())
        if parent.name() in bars:
            args.mode = parent.name()
        else:
            print("Could not determine which bar you're using and no bar was specified using --mode\nAborting")
            exit(1)

    motivate(
            format_string = format_strings["default" if args.no_color else args.mode],
            color         = args.color,
            no_color      = args.no_color,
            image_path    = args.image_path,
            list_path     = args.list)
