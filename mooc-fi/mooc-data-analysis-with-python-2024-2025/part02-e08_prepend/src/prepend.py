#!/usr/bin/env python3

class Prepend(object):
    def __init__(self, s: str):
        self.string = s

    def write(self, s: str):
        print(f"{self.string}{s}") 

def main():
    p = Prepend("+++ ")
    p.write("Hello")

if __name__ == "__main__":
    main()
