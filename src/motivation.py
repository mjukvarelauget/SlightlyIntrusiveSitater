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
        "lemonbar" : "%s%s",
        "windows"  : "%s%s",
        "i3bar"    : "%s%s"
    }

thresholds = [25,20,30]
bars = ["polybar","xmobar","windows","lemonbar","i3bar"]

def notify(quote, image_path = None):
    cmdlist = ["notify-send", quote, "-i", image_path]
    if(image_path == None):
        cmdlist = ["notify-send", quote]

    process = subprocess.Popen(cmdlist, stdout=subprocess.PIPE)
    _, _ = process.communicate()


def motivate(format_string, image_path = None, list_path = None):
    if(image_path == None):
        image_path = os.path.join(dir_path, "..","assets","harvåd.png")

    if(list_path == None):
        list_path = os.path.join(dir_path, "..","data","quotes.txt")

    with open(list_path) as f:
        f = f.readlines()
        quote = random.choice(f).strip()
        colors = [hex(random.randint(thresholds[i],2**8)).strip("0x").zfill(2) for i in range(3)]
        colorstring = "#" + colors[0] + colors[1] + colors[2]

        notify(quote, image_path)

        print(format(format_string
            %(colorstring, quote)))


if __name__ == "__main__":
    parser =  argparse.ArgumentParser(description='what is this')
    parser.add_argument('--mode', help='/'.join(bars), type=str, choices=bars)
    parser.add_argument('-i', '--image-path', help='notification icon path', type=str)
    parser.add_argument('-l', '--list', help='quote list file path', type=str)
    args = parser.parse_args()

    if(args.mode == None):
        parent = psutil.Process(psutil.Process().ppid())
        if parent.name() in bars:
            args.mode = parent.name()
        else:
            print("Could not determine which bar you're using and no bar was specified using --mode\nAborting")
            exit(1)


    motivate(format_strings[args.mode])
