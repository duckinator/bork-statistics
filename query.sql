#standardSQL

-- BigQuery, pulling from the PyPi package downloads data.
-- https://packaging.python.org/guides/analyzing-pypi-package-downloads/

DECLARE start TIMESTAMP;
DECLARE start_date DATE;
SET start = '2020-12-01';
SET start_date = DATE(start);

SELECT file.version, COUNT(*) AS count FROM `the-psf.pypi.file_downloads`
WHERE file.project = 'bork'
  -- Limit to the month we're looking for.
  AND DATE(timestamp)
    BETWEEN start_date
    AND DATE_SUB(DATE_ADD(start_date, INTERVAL 1 MONTH), INTERVAL 1 DAY)
GROUP BY
  file.version
