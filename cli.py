#!/usr/bin/env python3
"""
Command-line interface for package sorting.
"""
import argparse
from src.main import sort


def main():
    """Parse arguments and call the sort function."""
    parser = argparse.ArgumentParser(description="Sort a package into a stack.")
    parser.add_argument("--width", type=float, required=True, help="Width in cm")
    parser.add_argument("--height", type=float, required=True, help="Height in cm")
    parser.add_argument("--length", type=int, required=True, help="Length in cm")
    parser.add_argument("--mass", type=float, required=True, help="Mass in kg")

    args = parser.parse_args()

    result = sort(args.width, args.height, args.length, args.mass)
    print(f"Package stack: {result}")


if __name__ == "__main__":
    main()
