#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""\
Generate SHA-256 Hash of a Given String

usage:
    python generate_hash.py <input_string>
    python generate_hash.py <input_string> <compare_hash>
    python generate_hash.py --algorithm <algorithm> <input_string>
"""

import os
import argparse
import hashlib


def calculate_hash(value, algorithm='sha256'):
    """Calculate hash of the given value using the specified algorithm."""
    encoded_value = value.encode()
    match algorithm:
        case 'md5':
            return hashlib.md5(encoded_value).hexdigest()
        case 'sha1':
            return hashlib.sha1(encoded_value).hexdigest()
        case 'sha256':
            return hashlib.sha256(encoded_value).hexdigest()
        case 'sha512':
            return hashlib.sha512(encoded_value).hexdigest()
        case _:
            raise ValueError("Unsupported hash algorithm")


def example_run():
    example_string = "example"
    print(f"Example run with input '{example_string}':")
    print(f"`python generate_hash.py {example_string}`")
    calculated_hash = calculate_hash(example_string)
    print(f"Calculated SHA-256 hash: {calculated_hash}")


if __name__ == "__main__":
    # Check if script is called without arguments then run example
    if len(os.sys.argv) == 1:
        example_run()
        os.sys.exit(0)

    # Argument parser setup
    parser = argparse.ArgumentParser(
        description='Generate SHA-256 Hash of a Given String',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    # Change hash algorithm if needed (default is sha256)
    parser.add_argument(
        '--algorithm', '-a',
        default='sha256',
        choices=['md5', 'sha1', 'sha256', 'sha512'],
        help='Hash algorithm to use'
    )

    # Print output in uppercase (optional)
    parser.add_argument(
        '--uppercase', '-u',
        action='store_true',
        help='Print the hash in uppercase'
    )

    # Receive the desired input string to generate hash for
    parser.add_argument(
        'input_string',
        help='The input string to hash'
    )

    # Compare with a given hash (optional)
    parser.add_argument(
        'compare_hash',
        nargs='?',
        help='The hash to compare with'
    )

    args = parser.parse_args()

    # Generate the hash
    generated_hash = calculate_hash(
        args.input_string,
        algorithm=args.algorithm
    )

    if args.uppercase:
        generated_hash = generated_hash.upper()

    # Show result
    print(generated_hash)

    # If compare hash is provided, compare and show result
    if args.compare_hash:
        if generated_hash == args.compare_hash:
            print("Hashes match!")
        else:
            print("Hashes do not match.")
