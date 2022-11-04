# This directory will be checked with pytest. It will examine
# all files that start with test_*.py and run all functions with
# names that start with test_

import filecmp
import os

infile1 = 'data/input-sorted.bed'
infile2 = 'data/input-sorted.bed'
outfile = 'data/testmerge.bed'
exp_outfile = 'data/input-merged.bed'

def test_merge_bed() -> None:
    os.system(f"python3 src/merge_bed.py {infile1} {infile2} -o {outfile}")
    assert filecmp.cmp(outfile,exp_outfile)
