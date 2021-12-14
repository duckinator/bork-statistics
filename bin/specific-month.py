#!/usr/bin/env python3

'''
Downloads data for last month's downloads.
'''

import json
from pathlib import Path
import sys
from google.cloud import bigquery

# pylint: disable=invalid-name

if len(sys.argv) < 2 or "-h" in sys.argv or "--help" in sys.argv:
    print("Usage: {} YYYY-MM".format(sys.argv[0]))
    sys.exit(1)

month = sys.argv[1]
assert month

root_dir = Path(__file__, '..', '..').resolve()

client = bigquery.Client.from_service_account_json(Path.home() / '.bigquery' / 'keys' / 'bork-statistics.json')

query = Path(root_dir, 'queries', 'downloads-specific-month.sql').resolve().read_text()
query = query.replace('YYYY-MM', month)

query_job = client.query(query)

results = [{'version': row['version'], 'count': row['count']} for row in query_job]
results_json = json.dumps(results, indent=2)

start_date = next(iter(query_job))['start_date'].strftime('%Y-%m-%d')
Path(root_dir, 'data', 'pypi', start_date + '.json').write_text(results_json)
