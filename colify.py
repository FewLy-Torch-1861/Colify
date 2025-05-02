#!/usr/bin/env python3

import argparse


def rgb_to_hex(r, g, b):
    try:
        if not all(0 <= color <= 255 for color in [r, g, b]):
            return None
        return "#{:02x}{:02x}{:02x}".format(r, g, b)

    except Exception as e:
        print(f"\nRGB to HEX error: {e}")


def hex_to_rgb(hex_color):
    try:
        hex_color = hex_color.lstrip("#")
        if not all(c in "0123456789abcdefABCDEF" for c in hex_color):
            return None
        if len(hex_color) != 6:
            return None
        return tuple(int(hex_color[i : i + 2], 16) for i in (0, 2, 4))

    except Exception as e:
        print(f"HEX to RGB error: {e}")


def main():
    parser = argparse.ArgumentParser(
        description="Colify - a simple color format converter"
    )
    parser.add_argument("--rgb2hex", action="store_true", help="convert rgb to hex")
    parser.add_argument("--hex2rgb", action="store_true", help="convert hex to rgb")
    parser.add_argument("-r", "--red", type=int, help="red")
    parser.add_argument("-g", "--green", type=int, help="green")
    parser.add_argument("-b", "--blue", type=int, help="blue")
    parser.add_argument("-H", "--hex", type=str, help="hex code")

    args = parser.parse_args()

    try:
        if args.rgb2hex:
            result = rgb_to_hex(args.red, args.green, args.blue)
            print(result)
            return

        if args.hex2rgb:
            result = hex_to_rgb(args.hex)
            print(result)
            return

        parser.print_help()

    except Exception as e:
        print(f"\nRGB to HEX error: {e}")


if __name__ == "__main__":
    main()
