"""Tool for cleaning up a BED file."""

import argparse  # we use this module for option parsing. See main for details.

import sys
from typing import TextIO
from bed import (
    parse_line, print_line, BedLine
)


def read_bed_file(f: TextIO) -> list[BedLine]:
    """Read an entire sorted bed file."""
    # Handle first line...
    line = f.readline()
    if not line:
        return []

    res = [parse_line(line)]                          # list with only the first bedline
    for line in f:
        feature = parse_line(line)
        prev_feature = res[-1]                        # the last bedline in the list
        assert prev_feature.chrom < feature.chrom or \
            (prev_feature.chrom == feature.chrom and
             prev_feature.chrom_start <= feature.chrom_start), \
            "Input files must be sorted"
        res.append(feature)

    return res


def merge(f1: list[BedLine], f2: list[BedLine], outfile: TextIO) -> None:  
    """Merge features and write them to outfile."""
    # FIXME: I have work to do here!
    i, j = 0, 0
    z = []  # a new list to copy elements into

    # merge by chromosome name except if they are equal, then merge by chrom_start

    while i < len(f1) and j < len(f2):
        feature_f1 = f1[i]                             # bedline accessed by the names chrom and chrom_start
        feature_f2 = f2[j]

        if feature_f1.chrom == feature_f2.chrom:                   # merge by 'chrom_start'
            if feature_f1.chrom_start < feature_f2.chrom_start:
                z.append(feature_f1)
                i += 1
            else:
                z.append(feature_f2)
                j += 1

        elif feature_f1.chrom < feature_f2.chrom:                  # merge by 'chrom'
            z.append(feature_f1)
            i += 1
        else:
            z.append(feature_f2)
            j += 1
        
        if i == len(f1):
            z.extend(f2[j:])

        if j == len(f2):
            z.extend(f1[i:])


    for features in z:
        print_line(features, outfile)


def main() -> None:
    """Run the program."""
    # Setting up the option parsing using the argparse module
    argparser = argparse.ArgumentParser(description="Merge two BED files")
    argparser.add_argument('f1', type=argparse.FileType('r'))
    argparser.add_argument('f2', type=argparse.FileType('r'))
    argparser.add_argument('-o', '--outfile',  # use an option to specify this
                           metavar='output',   # name used in help text
                           type=argparse.FileType('w'),  # file for writing
                           default=sys.stdout)

    # Parse options and put them in the table args
    args = argparser.parse_args()

    # With all the options handled, we just need to do the real work
    features1 = read_bed_file(args.f1)
    features2 = read_bed_file(args.f2)
    merge(features1, features2, args.outfile)


if __name__ == '__main__':
    main()
