import argparse
from pathlib import Path

infiles = Path('test').glob('*.in')

for infile in infiles:
    print(infile)
    outfile = infile.parent / (infile.stem + '.out')

    with infile.open('r') as f:
        s = ''.join(f.read().split())

    all_len = len(s)
    lst = sorted([s[i:] for i in range(len(s))])
        
    ans = []
    for i in range(1, 5):
        target = lst[all_len//5*i-1]
        ans.append(str(all_len - len(target) + 1))

    with outfile.open('w') as f:
        f.write(' '.join(ans)+'\n')