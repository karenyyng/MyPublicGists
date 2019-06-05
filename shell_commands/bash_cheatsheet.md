# printing time stamp  
```bash
$ date "+%Y-%m-%d_%H-%M-%S"
2019-06-05_14-49-16
```

# Reference:
[ref](http://www.oliverelliott.org/article/computing/ref_unix/)

# find full path to a file 
```
$ readlink -f filename  # on Linux
$ greadlink -f filename  # on Mac
```
[SO post](http://stackoverflow.com/questions/5265702/how-to-get-full-path-of-a-file)

# Other useful command:
```
pdsh   # issue commands to groups of hosts in parallel
ls *.txt | xargs <OTHER BASH COMMAND>
```

# system monitoring
```
$ top
$ 1  # shows CPU usage breakdown by each CPU in a multiple core system
```
Better still, use
```
htop
```
for more detailed diagnostics

# free memory 
[ref](http://unix.stackexchange.com/questions/87908/how-do-you-empty-the-buffers-and-cache-on-a-linux-system)


# list-of-open-files (lsof)
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

# watching job 
```
watch -n 120 job_command 
# e.g.
watch -n 120 squeue karenyng
```
change the output every 120 seconds

# find position in job queue
```
squeue -p knl | grep -B 10000000 karenyng | wc -l
```

# transfer files between machines 
```
scp -3 -r $REMOTE_MACHINE_1:$REMOTE_DIR_LOC $REMOTE_MACHINE_2:$REMOTE_DESTINATION
```
# count no. of columns in a csv file
```
!head -1 cs_pos_data.csv | awk -F',' ' { print NF }'  ## only count the first line
awk -F',' ' { print NF }' FILE.csv | sort | uniq -c   ## count how many lines and delimiters there are
```

# umask
```
umask 002
```
002 means 777 - 002 = 775 deafult directory permisions    
and 666 - 002 = 664 for default file permissions

# find files 
If i want to find files with names `odbc.ini`
```
sudo find /dir/to/search -name odbc*.ini 

## if cannot print directly as log message in some special terminal types, use `2>/dev/null`
find /dir/to/search -name odbc*.ini 2>/dev/null
```

# grep 
grep recursively from a specific file extension type
```
grep -r -i --include \*.py $A_PATH
```
[link](https://stackoverflow.com/questions/12516937/grep-but-only-certain-file-extensions)

# check architecture 
if we are using on linux 
```
$ lscpu
```
If not, use the following command for checking the operating system name
```
$ uname
```

# run command without fear of network disconnection 
```
$ nohup COMMAND
```
