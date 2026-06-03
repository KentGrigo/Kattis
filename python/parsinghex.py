import sys
import re

hexPattern = re.compile(r'0[xX][0-9a-fA-F]{1,8}')

for line in sys.stdin:
    matches = hexPattern.findall(line)
    for match in matches:
        print(match, int(match, 16))
