# bork statistics

This repository contains historical data for Bork downloads over time,
and the tools to generate that data.

## PyPi

Download data for PyPi is stored on Google BigQuery as a public dataset.
They [provide a guide](https://packaging.python.org/guides/analyzing-pypi-package-downloads/)
for using the data.

### Historical Data (July 2019&ndash;December 2020)

When importing the initial historical data (July 2019 through December 2020),
I manually ran and downloaded the JSON results for the following query,
changing `YYYY-MM` to the year and month in question.

Given that I only needed to do 18 months, it felt unnecessary to fully automate it.

<details>
<summary>Historical data query</summary>

```sql
#standardSQL

DECLARE start TIMESTAMP;
DECLARE start_date DATE;
SET start = 'YYYY-MM-01';
SET start_date = DATE(start);

SELECT file.version, COUNT(*) AS count FROM `the-psf.pypi.file_downloads`
WHERE file.project = 'bork'
  -- Limit to the month we're looking for.
  AND DATE(timestamp)
    BETWEEN start_date
    AND DATE_SUB(DATE_ADD(start_date, INTERVAL 1 MONTH), INTERVAL 1 DAY)
GROUP BY
  file.version
```

</details>

## GitHub Releases

TODO
