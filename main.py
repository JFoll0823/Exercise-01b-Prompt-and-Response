#!/usr/bin/env python3
import sys
assert sys.version_info >= (3,9), "This script requires at least Python 3.9"

passage_name = "West of House"
passage_text = "This is an open field west of a white house, with a boarded front door."

print("You are at the "+passage_name+"\n"+passage_text+"\nWhat would you like to do? ")
response = input()
if(response == "go north"):
    print("Good job!")

#if the user types "Go north" or "Go North" the message "Good job!" is not displayed because capitalization matters.