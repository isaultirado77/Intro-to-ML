#!/usr/bin/env python3

import re

def red_green_blue(filename="src/rgb.txt"):
    with open(filename, 'r') as file:
        lines = file.readlines()[1:]  # Skip the first line
    
    result = []
    for line in lines:
        # Use regex to split on whitespace, but preserve spaces in color names
        match = re.match(r'^\s*(\d+)\s+(\d+)\s+(\d+)\s+(.+?)\s*$', line)
        if match:
            red, green, blue, colorname = match.groups()
            # Combine into a single string with tab-separated fields
            formatted_line = f"{red}\t{green}\t{blue}\t{colorname}"
            result.append(formatted_line)
    
    return result


def main():
    pass

if __name__ == "__main__":
    main()
