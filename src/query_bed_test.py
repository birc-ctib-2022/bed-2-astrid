# This directory will be checked with pytest. It will examine
# all files that start with test_*.py and run all functions with
# names that start with test_

import filecmp
import os

infile = 'data/large-sorted.bed'
query = 'data/query-1.txt'
outfile = 'data/testquery.txt'
exp_outfile = 'data/expected-1.txt'

def test_sort_bed() -> None:
    os.system(f"python3 src/query_bed.py {infile} {query} -o {outfile}")
    assert filecmp.cmp(outfile,exp_outfile)
