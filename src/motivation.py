#!/usr/bin/python3

import random
import subprocess
import argparse
import psutil

def notify(quote, image_path = None):
    cmdlist = ["notify-send", quote, "-i", image_path]
    if(image_path == None):
        cmdlist = ["notify-send", quote]

    process = subprocess.Popen(cmdlist, stdout=subprocess.PIPE)
    _, _ = process.communicate()


def motivate(format_string, image_path):
    thresholds = [25,20,30]
    with open("/home/joakim/Documents/Python/Motivation/data/quotes.txt","r") as f:
        f = f.readlines()
        quote = random.choice(f).strip()
        colors = [hex(random.randint(0,2**8)).strip("0x").zfill(2) for i in range(3)]
        colorstring = "#" + colors[0] + colors[1] + colors[2]

        notify(quote, image_path)

        print(format(format_string
            %(colorstring, quote)))

def polybar(args):
    motivate("%%{F%s}%s", "/home/joakim/Documents/Python/Motivation/assets/harvåd.png")

def xmobar(args):
    motivate("<fc=%s>%s</fc>","/home/joakim/Documents/Python/Motivation/assets/harvåd.png")

def windows(args):
    print("fuck you, not implemented yet")


if __name__ == "__main__":
    bars = ["polybar","xmobar","windows","lemonbar","i3bar"]
    parser =  argparse.ArgumentParser(description='what is this')
    parser.add_argument('--mode', help='polybar/xmobar', type=str, choices=bars)
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

