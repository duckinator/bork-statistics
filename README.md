# bork statistics

This repository contains historical data for Bork downloads over time,
and the tools to generate that data.

## PyPi

Download data for PyPi is stored on Google BigQuery as a public dataset.
They [provide a guide](https://packaging.python.org/guides/analyzing-pypi-package-downloads/)
for using the data.

### New Data (January 2021&ndash;Present)

At the end of each month, I've been manually running `./bin/last-month.py`
and committing + pushing the resulting JSON file.

### Historical Data (July 2019&ndash;December 2020)

When importing the initial historical data (July 2019 through December 2020),
I used `./bin/specific-month.py YYYY-MM`, changing `YYYY-MM` to the year
and month in question.

## GitHub Releases

TODO
