# what the funny symbols mean
```
~ current directory
[^...] negate class 

```

## automatic variables 
p.16 of GNU make book by Merklenburg R book
```
$@ The filename representing the target 
$% The filename element of an archive member specification
$< the filename of the first prerequisite 
$? The name of all prerequisites that are newer than the target, separated by spaces
$^ The filenames of all the prerequisties, separated by spaces . This List has duplicate filenames removed since for most uses, such as compiling , copying etc.
$+ the names of all prerequisites separated by spaces 
$* the stem of the target filename 
```

```
%.EXTENSION ## % is the wildcard file prefix
```

