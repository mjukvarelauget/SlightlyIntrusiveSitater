#!/usr/bin/python3

import random
import subprocess
import argparse

def polybar(args):
    thresholds = [25,20,30]
    with open ("/home/joakim/Documents/Python/Motivation/data/quotes.txt","r") as f:
        f = f.readlines()
        quote = random.choice(f).strip()
        colors = [hex(random.randint(0,2**8)).strip("0x").zfill(2) for i in range(3)]
        colorstring = "#" + colors[0]+ colors[1]+ colors[2]

        cmdlist = ["notify-send", quote, "-i", "/home/joakim/Documents/Python/Motivation/assets/harvåd.png"]
        process = subprocess.Popen(cmdlist, stdout=subprocess.PIPE)

        _, _ = process.communicate()
        print(format("%%{F%s}%s"
            %(colorstring, quote)))

def xmobar(args):
    thresholds = [25,20,30]
    with open ("/home/joakim/Documents/Python/Motivation/data/quotes.txt","r") as f:
        f = f.readlines()
        quote = random.choice(f).strip()
        colors = [hex(random.randint(thresholds[i],2**8)).strip("0x").zfill(2) for i in range(3)]
        colorstring = "#" + colors[0]+ colors[1]+ colors[2]

        cmdlist = ["notify-send", quote, "-i", "/home/joakim/Documents/Python/Motivation/assets/harvåd.png"]
        process = subprocess.Popen(cmdlist, stdout=subprocess.PIPE)

        _, _ = process.communicate()
        print(format("<fc=%s>%s</fc>"
            %(colorstring, quote)))

def windows(args):
    print("fuck you, not implemented yet")


if __name__ == "__main__":
    parser =  argparse.ArgumentParser(description='what is this')
    parser.add_argument('--mode', help='polybar/xmobar', type=str, choices=['polybar','xmobar',
        'windows'], default='xmobar')
    args = parser.parse_args()

    # print(args.mode)
    if args.mode == "polybar":
        polybar(args)
    elif args.mode == "xmobar":
        xmobar(args)
    elif args.mode == "windows":
        windows(args)
    else:
        print("please specify which bar to use")

