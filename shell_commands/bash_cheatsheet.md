# Table of content

<!-- toc -->

- [Printing time stamp](#printing-time-stamp)
- [Find full path to a file](#find-full-path-to-a-file)
- [Running command in parallel : PDSH](#running-command-in-parallel--pdsh)
- [Xargs](#xargs)
- [System monitoring](#system-monitoring)
- [Free memory from linux host](#free-memory-from-linux-host)
- [List-of-open-files (lsof)](#list-of-open-files-lsof)
- [Redirecting outputs from `stderr`](#redirecting-outputs-from-stderr)
- [Watching log files](#watching-log-files)
- [Watching job](#watching-job)
- [Find position in job queue](#find-position-in-job-queue)
- [Transfer files between machines](#transfer-files-between-machines)
- [Count no. of columns in a csv file](#count-no-of-columns-in-a-csv-file)
- [Changing permission with umask](#changing-permission-with-umask)
- [Find files](#find-files)
- [Grep](#grep)
- [Check hardware architecture](#check-hardware-architecture)
- [Run command without fear of network disconnection](#run-command-without-fear-of-network-disconnection)
- [Reference for a list of linux commands](#reference-for-a-list-of-linux-commands)

<!-- tocstop -->

# Printing time stamp  
```bash
$ date "+%Y-%m-%d_%H-%M-%S"
2019-06-05_14-49-16
```


# Find full path to a file 
```
$ readlink -f filename  # on Linux
$ greadlink -f filename  # on Mac
```
[SO post](http://stackoverflow.com/questions/5265702/how-to-get-full-path-of-a-file)

# Running command in parallel : PDSH 
```
pdsh   # issue commands to groups of hosts in parallel
```
# Xargs 
```
ls *.txt | xargs <OTHER BASH COMMAND>
```

# System monitoring
```
$ top
$ 1  # shows CPU usage breakdown by each CPU in a multiple core system
```
Better still, use
```
htop
```
for more detailed diagnostics

# Free memory from linux host
[ref](http://unix.stackexchange.com/questions/87908/how-do-you-empty-the-buffers-and-cache-on-a-linux-system)


# List-of-open-files (lsof)
```
$ lsof +D /path_to_file
```
try to find which process is using a file.
[ref](http://unix.stackexchange.com/questions/11238/how-to-get-over-device-or-resource-busy)

# Redirecting outputs from `stderr`
```
module avail 2>&1
```
`2` is from `stderr`
`1` is from `stdoutput`

# Watching log files 
```
tail -f output.log
```

# Watching job 
```
watch -n 120 job_command 
# e.g.
watch -n 120 squeue karenyng
```
change the output every 120 seconds

# Find position in job queue
```
squeue -p knl | grep -B 10000000 karenyng | wc -l
```

# Transfer files between machines 
```
scp -3 -r $REMOTE_MACHINE_1:$REMOTE_DIR_LOC $REMOTE_MACHINE_2:$REMOTE_DESTINATION
```
# Count no. of columns in a csv file
```
!head -1 cs_pos_data.csv | awk -F',' ' { print NF }'  ## only count the first line
awk -F',' ' { print NF }' FILE.csv | sort | uniq -c   ## count how many lines and delimiters there are
```

# Changing permission with umask
```
umask 002
```
002 means 777 - 002 = 775 deafult directory permisions    
and 666 - 002 = 664 for default file permissions

# Find files 
If i want to find files with names `odbc.ini`
```
find /dir/to/search -name odbc*.ini 
```
Then `find` will look for a pattern match of the file name you specified
recursively.
If you cannot print directly as log message in some special terminal types, use `2>/dev/null`
`find /dir/to/search -name odbc*.ini 2>/dev/null`
[ref](https://www.linode.com/docs/tools-reference/tools/find-files-in-linux-using-the-command-line/)

# Grep 
grep recursively from a specific file extension type
```
grep -r -i --include \*.py $A_PATH
```
[link](https://stackoverflow.com/questions/12516937/grep-but-only-certain-file-extensions)

# Check hardware architecture 
if we are using on linux 
```
$ lscpu
```
If not, use the following command for checking the operating system name
```
$ uname
```

# Run command without fear of network disconnection 
```
$ nohup COMMAND
```

# Find the number of lines in a csv or text file 
```bash
$ wc -l FILENAME
```
# Find the number of delimited columns in csv or text file
```bash 
$ head -1 FILENAME | awk -F',' '{print $NF}'
```
In the above example we were counting the number of ',' strings. [SO ref](https://stackoverflow.com/questions/18351284/how-to-get-the-count-of-fields-in-a-delimited-string)
`$NF` refers to the correct number of fields in the file, not the number of
delimiters.

# Reference for a list of linux commands
[ref link](http://www.oliverelliott.org/article/computing/ref_unix/)


