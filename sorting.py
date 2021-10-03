#! python3
import os
import re
import shutil

datePattern = re.compile(r"""^(.*?) #all text before date
    ((20)\d\d)                   #year
    ((0|1)?\d)                   #month
    ((0|1|2|3)?\d)               #day
    (.*?)$                       #all text by date
    """, re.VERBOSE)

for filename in os.listdir('.'):
    mo = datePattern.search(filename)

    if mo is None:
        continue
    beforePart = mo.group(1)
    yearPart = mo.group(2)
    monthPart = mo.group(4)
    dayPart = mo.group(6)
    afterPart = mo.group(8)

    absWorkingDir = os.path.abspath('.')
    path = os.path.join(absWorkingDir, yearPart)
    path2 = os.path.join(path, monthPart)

    isdir = os.path.isdir(path)
    isdir2 = os.path.isdir(path2)

    if not isdir:
        os.mkdir(path)

    if not isdir2:
        os.mkdir(path2)

    shutil.move(filename, path2)

