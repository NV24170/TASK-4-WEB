# TASK-4-WEB

This repository contains a set of small Python scripts designed to
parse and analyze a simple log file format. The exercises are divided
into five tasks that gradually build functionality from parsing a
single line up to exporting structured JSON output.

Each task is implemented in the `WEB-4/` directory and can be run
independently. The sample log data is provided in
`WEB-4/sample_logs.txt` and the final JSON export is written to
`WEB-4/parsed_logs.json`.

---

## 📂 Project Structure

```
README.md
WEB-4/
    sample_logs.txt
    task1_parse_single.py
    task2_parse_list.py
    task3_parse_file.py
    task4_report_invalids.py
    task5_export_parsed_json.py
    parsed_logs.json     # generated after running task5
```

## 🛠 Tasks Overview

1. **Parse a single line** (`task1_parse_single.py`)
   - Implements `parse_log_line(line)` which splits a log line on
     pipes (`|`) and returns a tuple `(timestamp, level, service,
     message)` or `None` for invalid formats.
   - Contains built‑in test cases; run with `python3 WEB-4/task1_parse_single.py`.

2. **Parse a list of lines** (`task2_parse_list.py`)
   - Uses `parse_log_line` to process a hard‑coded list of sample
     strings, skipping invalid entries.

3. **Parse a log file** (`task3_parse_file.py`)
   - Reads `sample_logs.txt` line‑by‑line and prints the first five
     valid parsed tuples.

4. **Count invalid format lines** (`task4_report_invalids.py`)
   - Reports total, valid, and invalid lines in the sample log.
   - Outputs:
     ```text
     Total lines: X
     Valid lines: Y
     Invalid format lines: Z
     ```

5. **Export parsed results to JSON** (`task5_export_parsed_json.py`)
   - Parses all valid lines and writes them into
     `parsed_logs.json` with objects containing
     `timestamp`, `level`, `service`, and `message` fields.

## 🚀 Usage

Run any script from the repository root, for example:

```bash
python3 WEB-4/task3_parse_file.py
```

The scripts locate `sample_logs.txt` relative to their own directory,
so they work regardless of the current working directory.

## 📄 Sample Output

After running `task5_export_parsed_json.py`, the `parsed_logs.json`
file will contain an array of log entries similar to:

```json
[
  {"timestamp":"2026-02-05 08:11:20","level":"ERROR",
   "service":"db","message":"DB timeout while fetching user
   profile"},
  ...
]
```

## ✅ Requirements

- Python 3.x (no third‑party packages needed)

## 📝 Notes

This project was created as part of a tutorial exercise in parsing
and basic file I/O. Feel free to extend or reuse the parsing logic for
other log formats.

---

*Generated and maintained by the development environment.*
