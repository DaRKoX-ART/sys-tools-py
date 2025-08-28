import sys, re
def logstats(path):
    counts = {}
    with open(path, encoding="utf-8", errors="ignore") as f:
        for line in f:
            level = (re.search(r"\b(INFO|WARN|ERROR|DEBUG)\b", line) or ["OTHER"])[0]
            counts[level] = counts.get(level, 0) + 1
    return counts

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python tools/logstats.py <file.log>")
        sys.exit(1)
    print(logstats(sys.argv[1]))
