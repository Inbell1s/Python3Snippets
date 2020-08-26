#!/bin/python3
#
#Coloured text function snippet
#


import os
import sys

#Color Definitions.
#(Style;Color;Background)

def printRedB(text):
    print("\x1b[1;31;40m", text, "\x1b[0m", end="", sep="")

def printGreenB(text):
    print("\x1b[1;32;40m", text, "\x1b[0m", end="", sep="")

def printYellowB(text):
    print("\x1b[1;33;40m", text, "\x1b[0m", end="", sep="")

#Usage.
printRedB("test\n")

#Can print variables too.
tekst = "tester\n"
printGreenB(tekst)

#Print on one line
print("Hello, Can i have some ", end="")
printYellowB("Color")
print(" please?")
