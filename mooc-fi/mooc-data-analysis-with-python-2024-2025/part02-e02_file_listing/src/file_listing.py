#!/usr/bin/env python3

import re


def file_listing(filename="src/listing.txt"):
    with open(filename, "r") as file:
        lines = file.readlines()
    
    pattern = r"""
        ^                           # Start of line
        (?:                         # Non-capturing group for initial fields
            \S+                     # Access rights (non-whitespace)
            \s+                     # One or more spaces
            \d+                     # Number of references
            \s+                     # One or more spaces
            \S+                     # Owner's name
            \s+                     # One or more spaces
            \S+                     # Owning group
            \s+                     # One or more spaces
        )
        (\d+)                       # File size (captured)
        \s+                         # One or more spaces
        (\w{3})                     # Month (3 letters, captured)
        \s+                         # One or more spaces
        (\d{1,2})                   # Day (1 or 2 digits, captured)
        \s+                         # One or more spaces
        (\d{2}):(\d{2})             # Hour:minute (captured separately)
        \s+                         # One or more spaces
        (.+)$                       # Filename (rest of the line, captured)
    """
    
    result = []
    for line in lines:
        match = re.search(pattern, line, re.VERBOSE)
        if match:
            size = int(match.group(1))
            month = match.group(2)
            day = int(match.group(3))
            hour = int(match.group(4))
            minute = int(match.group(5))
            filename = match.group(6).strip()  # Remove trailing whitespace
            result.append((size, month, day, hour, minute, filename))
    
    return result

def main():
    pass

if __name__ == "__main__":
    main()
