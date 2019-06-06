# Table of content

<!-- toc -->

  * [C++ profiling](#c-profiling)
    + [timing profile](#timing-profile)
      - [using Valgrind / callgrind](#using-valgrind--callgrind)
- [Vtune](#vtune)

<!-- tocstop -->

on the relevant computer, execute
```bash
cat /proc/cpuinfo
cat /proc/meminfo
```
to find the relevant hardware specification
Then use http://ark.intel.com/search?q= to check the hardware specs.

Also you can use 
```
uname
```

## C++ profiling

### timing profile
#### using Valgrind / callgrind
```bash
$ valgrind --dsymutil=yes --tool=callgrind ./test_kernels.x 
$ callgrind_annotate ./callgrind.out.26984 test_kernels.cpp > profile_test_kernels.txt
```

# Vtune
A job needs to be submitted before Vtune can profile the code properly on the compute node.
```
amplxe-gui $PATH_TO/r001hs.amplxe
```
