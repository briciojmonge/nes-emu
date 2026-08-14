from pathlib import Path
import re
import sys

base = Path('.')
a = (base/'mynes.log').read_text(encoding='utf-8', errors='ignore').splitlines()
b = (base/'nestest.log').read_text(encoding='utf-8', errors='ignore').splitlines()

def strip(line):
    s = line.strip()
    if not s:
        return None
    s = re.sub(r'\s+PPU:.*$', '', s)
    s = re.sub(r'\s+CYC:\d+.*$', '', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s

na = [strip(x) for x in a if strip(x) is not None]
nb = [strip(x) for x in b if strip(x) is not None]

idx_a = next((i for i, l in enumerate(na) if 'C68B' in l), None)
idx_b = next((i for i, l in enumerate(nb) if 'C68B' in l), None)
print('index mynes before C68B:', idx_a)
print('index nestest before C68B:', idx_b)
if idx_a is None or idx_b is None:
    print('could not find C68B in one of the logs')
    sys.exit(0)

pre_a = na[:idx_a]
pre_b = nb[:idx_b]
print('prefix lines mynes:', len(pre_a))
print('prefix lines nestest:', len(pre_b))
print('same prefix length:', len(pre_a) == len(pre_b))

for i, (x, y) in enumerate(zip(pre_a, pre_b), 1):
    if x != y:
        print('first mismatch at prefix line', i)
        print('mynes :', x)
        print('nestest:', y)
        break
else:
    print('all prefix lines match up to the line before C68B')
