# This directory will be checked with pytest. It will examine
# all files that start with test_*.py and run all functions with
# names that start with test_

import filecmp
import os

infile = 'data/input.bed'
outfile = 'data/testsort.txt'
exp_outfile = 'data/input-sorted.bed'

def test_sort_bed() -> None:
    os.system(f"python3 src/sort_bed.py {infile} {outfile}")
    assert filecmp.cmp(outfile,exp_outfile)

