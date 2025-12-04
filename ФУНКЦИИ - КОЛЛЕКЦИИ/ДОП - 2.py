import re
import sys

s = list(map(str, sys.stdin))
lst = [list(map(int, re.findall(r'\d+', i))) for i in s]
print(min(map(sum, filter(lambda x: len(x) == len(max(lst, key=len)), lst)))
      if re.search(r'\d+', str(s)) else -1)
