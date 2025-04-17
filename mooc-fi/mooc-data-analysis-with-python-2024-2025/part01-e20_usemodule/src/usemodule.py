#!/usr/bin/env python3

# Don't modify the below hack
try:
    from src import triangle
except ModuleNotFoundError:
    import triangle

def main():
    a = 2
    b = 5
    print("hypotenuse", triangle.hypotenuse(a, b))
    print("area", triangle.area(a, b))

if __name__ == "__main__":
    main()
