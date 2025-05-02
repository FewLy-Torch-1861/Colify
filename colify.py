#!/usr/bin/env python3

import argparse
import re


def is_valid_rgb(r, g, b):
    """Checks if the given RGB values are valid (0-255)."""
    return all(0 <= color <= 255 for color in [r, g, b])


def rgb_to_hex(r, g, b):
    """Converts RGB color values to a hexadecimal color code."""
    if not is_valid_rgb(r, g, b):
        return None
    return f"#{r:02x}{g:02x}{b:02x}"


def is_valid_hex(hex_color):
    """Checks if the given string is a valid hexadecimal color code."""
    hex_color = hex_color.lstrip("#")
    return bool(re.fullmatch(r"[0-9a-fA-F]{6}", hex_color))


def hex_to_rgb(hex_color):
    """Converts a hexadecimal color code to RGB tuple."""
    hex_color = hex_color.lstrip("#")
    if not is_valid_hex(hex_color):
        return None
    return tuple(int(hex_color[i : i + 2], 16) for i in (0, 2, 4))


def main():
    parser = argparse.ArgumentParser(
        description="Colify - a simple color format converter"
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--rgb2hex", action="store_true", help="Convert RGB to HEX")
    group.add_argument("--hex2rgb", action="store_true", help="Convert HEX to RGB")

    parser.add_argument("-r", "--red", type=int, help="Red color value (0-255)")
    parser.add_argument("-g", "--green", type=int, help="Green color value (0-255)")
    parser.add_argument("-b", "--blue", type=int, help="Blue color value (0-255)")
    parser.add_argument(
        "-H", "--hex", type=str, help="Hexadecimal color code (e.g., #FF0000 or FF0000)"
    )

    args = parser.parse_args()

    if args.rgb2hex:
        if all(arg is not None for arg in [args.red, args.green, args.blue]):
            result = rgb_to_hex(args.red, args.green, args.blue)
            print(result)
        else:
            parser.error("For --rgb2hex, you must provide -r, -g, and -b values.")
    elif args.hex2rgb:
        if args.hex:
            result = hex_to_rgb(args.hex)
            print(result)
        else:
            parser.error("For --hex2rgb, you must provide a -H value.")


if __name__ == "__main__":
    main()
