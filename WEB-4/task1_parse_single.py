# Task 1 — Parse a single line (Lesson 1)
# Implement parse_log_line(line) and run the test cases.

def parse_log_line(line: str):
    """Return (timestamp, level, service, message) OR None if invalid format."""
    # remove leading/trailing whitespace and newlines
    if line is None:
        return None
    text = line.strip()
    # empty lines are invalid
    if not text:
        return None
    # split on pipe character
    parts = text.split("|")
    # if we don't have exactly 4 pieces, it's malformed
    if len(parts) != 4:
        return None
    # strip whitespace from each part
    parts = [p.strip() for p in parts]
    return tuple(parts)


def run_tests():
    cases = [
        ("2026-02-05 08:11:20 | ERROR | db | DB timeout",
         ("2026-02-05 08:11:20", "ERROR", "db", "DB timeout")),
        ("  2026-02-05 08:11:20|ERROR|db|DB timeout  \n",
         ("2026-02-05 08:11:20", "ERROR", "db", "DB timeout")),
        ("BAD LINE WITHOUT SEPARATORS", None),
        ("2026-02-05 | INFO | auth | ok | EXTRA", None),
    ]

    for i, (line, expected) in enumerate(cases, start=1):
        got = parse_log_line(line)
        print(f"Case {i}: expected={expected} got={got}")


if __name__ == "__main__":
    run_tests()
