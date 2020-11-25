# Table of content

<!-- toc -->

- [Return sorted index of a list](#return-sorted-index-of-a-list)
- [Transposing list of lists](#transposing-list-of-lists)
- [Adding types hints to function definitions](#adding-types-hints-to-function-definitions)
- [Objects don't know their own names](#objects-dont-know-their-own-names)
- [List comprehension with `if`, `else`](#list-comprehension-with-if-else)
- [Regular expression](#regular-expression)
  * [find pattern that repeats n times](#find-pattern-that-repeats-n-times)
  * [Optional match](#optional-match)
  * [Differences between `()` and `[]`](#differences-between--and-)
  * [Differences between `re.match` and `re.search`](#differences-between-rematch-and-research)
- [Namespaces for python variables](#namespaces-for-python-variables)
- [Concatenating dictionaries and list:](#concatenating-dictionaries-and-list)
- [Logging](#logging)
  * [Debug: when NO log file is written](#debug-when-no-log-file-is-written)
- [Using the argument parser](#using-the-argument-parser)
- [Using `subprocess` to retrive shell outputs](#using-subprocess-to-retrive-shell-outputs)
  * [simpliest approach](#simpliest-approach)
  * [approach with more fine-grained control](#approach-with-more-fine-grained-control)
  * [Finding array types](#finding-array-types)
- [Handling date types](#handling-date-types)

<!-- tocstop -->

# Return sorted index of a list 
[ref](http://stackoverflow.com/questions/7851077/how-to-return-index-of-a-sorted-list)

# Transposing list of lists
[ref](http://stackoverflow.com/questions/6473679/python-list-of-lists-transpose-without-zipm-thing)

# Adding types hints to function definitions 
[ref1](https://docs.python.org/3/library/typing.html)
[ref2](https://www.python.org/dev/peps/pep-3107/#syntax)
[SO answers](https://stackoverflow.com/questions/38727520/adding-default-parameter-value-with-type-hint-in-python)


```
def this_function(a: str, b: str = "hello", c: dict = {}):
	return
```

# Objects don't know their own names 
[SO post](http://stackoverflow.com/questions/2553354/how-to-get-a-variable-name-as-a-string-in-python)
Names of objects live in namespaces....


# List comprehension with `if`, `else`
* Possible but the order of the syntax is different
```Python
[1e-6 if i % 2 == 0 else 1e-9 for i in range(12)]
```

# Regular expression 
```
import re
```
[ref](https://docs.python.org/3/library/re.html)
finding a match after a pattern
```
> match = re.findall("(?<=MemID =) ([0-9]+)", 'MemID = 000124, MemID = 0001234')
['000124', '0001234']
```

## find pattern that repeats n times 
use 'PATTERN{n}' with n being the times that the pattern repeats
e.g. 
```
> re.search('12345678', '[0-9]{8}')
```

numbers repeating between 8 to 10 times
```
> re.search('12345678', '[0-9]{8, 10}')
```

[ref](https://stackoverflow.com/questions/4760215/running-shell-command-from-python-and-capturing-the-output)

## Optional match
```Python
>>> match = re.search("home(brew)?", "home")
>>> match.group(1)
home
```

## Differences between `()` and `[]`
* `[]` denotes a character class, what to match, e.g. `[a-z0-9]` matches one character of the class range `a-z` or `0-9`
* `()` denotes a `capture`. `(a-z0-9)` captures the extract string `a-z0-9`. It is a grouping construct that has a precedence order.


## Differences between `re.match` and `re.search`
`match()` function only checks if the RE matches at the beginning of the string while `search()` will scan forward through the string for a match
[reference](https://docs.python.org/2/howto/regex.html#match-versus-search)


# Namespaces for python variables
```Python
>>> dir()  # inspect local namespace
```

# Concatenating dictionaries and list:
[SO post](http://stackoverflow.com/questions/1781571/how-to-concatenate-two-dictionaries-to-create-a-new-one-in-python) 

```
from itertools import chain
dict(chain.from_iterable(d.items() for d in (d1, d2, d3)))

flattened_list = chain.from_iterable(nested_list)
```


# Logging
logging module is part of standard Python. 
[tutorials from python doc](https://docs.python.org/2/library/logging.config.html)
[other tutorial](http://docs.python-guide.org/en/latest/writing/logging/) for parsing config settings from an ini file
You can read in a config file for parsing config settings for the logger.
```python
import logging
import datetime as dt
import pytz
logging.basicConfig(
    filename="debug.log",  # output log filename
    level=logging.INFO,   # set the verbosity using level 
    format="%(asctime)s %(levelname)s: %(message)s",   
    datefmt="%Y-%m-%d %H:%M:%S"
)
# set the timezone of the displayed time in the log									
logging.Formatter.converter = lambda *args: dt.datetime.now(
    tz=pytz.timezone('America/Los_Angeles')).timetuple()
logging.debug("Debug message")
logging.info("if level is set to logging.INFO")
logging.warning("This will be printed")
logger = logging.getLogger()
logger.level = logging.DEBUG
```

`Debug` has a lower level number than `info` so debug messages are not shown in the
above example. `Warning` has a higher level than `info` so warning messages are
captured by the logger.

## Debug: when NO log file is written
* check no `logging.DEBUG` or other `logging.*` lines are put before the `logging.basicConfig` line.
* check that the string formattings are correct in the logging lines.
Use `logging.warning` to make sure all formatting is ok.

# Using the argument parser 
See [examples](https://docs.python.org/3/library/argparse.html#example)
```
import argparse

parser = argparse.ArgumentParser(
          description="Visualize DM subhalos in 3D for specific cluster.")
parser.add_argument("clstNo", type=int, default=10,
                    help="Zeroth based numbering of cluster number")
parser.add_argument("--debug", action='store_true', 
										help='Supply flag to turn on debugging mode')
args = parser.parse_args()
# the parsed argument can be accessed 
# as the first string of the `add argument` method
print(args.clstNo)
```

# Using `subprocess` to retrive shell outputs
```python
import subprocess
```
## simpliest approach
```
subprocess.check_output(["ls", "../data"]) # alternatively
subprocess.check_output("grep 'heatdap2*' ./*json", shell=True)
```
If the returned status is 2, it means that your shell command is problematic.
`shell=False` disables all shell based features, but does not suffer from security vulnerability; see the Note in the `Popen` constructor documentation for helpful hints in getting `shell=False` to work.

When using `shell=True`, `pipes.quote()` can be used to properly escape whitespace
and shell metacharacters in strings that are going to be used to construct
shell commands.
[ref](https://docs.python.org/2/library/subprocess.html#frequently-used-arguments)

## approach with more fine-grained control
For Python 3.5+
```
p = subprocess.run("ls *.csv", shell=True,
                     stdin=subprocess.PIPE,
                     stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE)

output_from_shell = p.decode('utf-8')

```
where `output_from_shell` is a tuple of the stuff read from either `stdin`, `stdout` or `stderr`.

## Finding array types 
```python
np.issubdtype(arr, np.number)
```

# Handling date types 
Use `datetime` and `dateutils` libraries 
```
import datetime as dt 
from dateutils.relativedelta import relativedelta

# get date 3 months from today
dt.datetime.today() + relativedelta(months=3)
```
