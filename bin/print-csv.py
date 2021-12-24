#!/usr/bin/env python3

import csv
import json
from pathlib import Path
import sys


table = {}
versions = set()

for file in Path('data/pypi').glob('*'):
    row = {}
    with file.open() as f:
        data = json.load(f)
    for col in data:
        row[col['version']] = col['count']
        versions.add(col['version'])
    table[file.stem] = row

versions = sorted(versions)

if len(sys.argv) > 1:
    csvfile = open(sys.argv[1], 'w', newline='')
else:
    csvfile = sys.stdout

writer = csv.writer(csvfile, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
writer.writerow(['Start Date'] + versions)
for row_name in table:
    row = table[row_name]
    writer.writerow([row_name] + [row.get(version, 0) for version in versions])

csvfile.close()
