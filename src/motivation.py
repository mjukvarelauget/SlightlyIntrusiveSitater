#!/usr/bin/python3

import random
import subprocess
import argparse
import psutil
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

def notify(quote, image_path = None):
    cmdlist = ["notify-send", quote, "-i", image_path]
    if(image_path == None):
        cmdlist = ["notify-send", quote]

    process = subprocess.Popen(cmdlist, stdout=subprocess.PIPE)
    _, _ = process.communicate()


def motivate(format_string, image_path):
    thresholds = [25,20,30]
    with open(os.path.join(dir_path, "..","data","quotes.txt")) as f:
        f = f.readlines()
        quote = random.choice(f).strip()
        colors = [hex(random.randint(0,2**8)).strip("0x").zfill(2) for i in range(3)]
        colorstring = "#" + colors[0] + colors[1] + colors[2]

        notify(quote, image_path)

        print(format(format_string
            %(colorstring, quote)))

def polybar(args):
    motivate("%%{F%s}%s", os.path.join(dir_path, "..","assets","harvåd.png"))

def xmobar(args):
    motivate("<fc=%s>%s</fc>", os.path.join(dir_path, "..","assets","harvåd.png"))

def windows(args):
    print("fuck you, not implemented yet")


if __name__ == "__main__":

    bars = ["polybar","xmobar","windows","lemonbar","i3bar"]
    parser =  argparse.ArgumentParser(description='what is this')
    parser.add_argument('--mode', help='polybar/xmobar/windows/lemonbar/i3bar', type=str, choices=bars)
    parser.add_argument('-i', '--image-path', help='notification icon path', type=str)
    parser.add_argument('-l', '--list', help='quote list file path', type=str)
    args = parser.parse_args()

    if(args.mode == None):
        parent = psutil.Process(psutil.Process().ppid())
        if parent.name() in bars:
            args.mode = parent.name()

    if args.mode == "polybar":
        polybar(args)
    elif args.mode == "xmobar":
        xmobar(args)
    elif args.mode == "windows":
        windows(args)
    else:
        print("Could not determine which bar you're using and no bar was specified using --mode\nAborting")

