# How many Sundays fell on the first of the month during the twentieth century
from datetime import datetime as dtm

one_line_monstrosity = sum(sum(dtm(y, m, 1).weekday() == 6 for m in range(1, 12 + 1)) for y in range(1901, 2000 + 1))

print(one_line_monstrosity)