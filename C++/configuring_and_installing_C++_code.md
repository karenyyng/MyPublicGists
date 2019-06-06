# Table of content

<!-- toc -->

- [concepts](#concepts)
  * [autoconf](#autoconf)
  * [configure](#configure)
  * [make](#make)
  * [cmake](#cmake)
  * [libraries](#libraries)
- [paths to find stuff](#paths-to-find-stuff)
  * [`LD_LIBRARY_PATH`](#ld_library_path)
  * [`INCLUDE` path](#include-path)
  * [`RPATH`](#rpath)

<!-- tocstop -->

# concepts 

## autoconf

## configure 
```
./configure --help
```
should list how to specify the library / include paths 

## make 
[tutorial](https://linuxacademy.com/blog/linux/troubleshooting-configure-make-and-make-install-tutorial/)

## cmake

## libraries 
* statically linked 
* dynamically linked 


# paths to find stuff 
## `LD_LIBRARY_PATH`
where `/lib` are located 

## `INCLUDE` path
where header files are located.
This is less commonly used than `LD_LIBRARY_PATH`
```
C_INCLUDE_PATH (for C header files) or 
CPLUS_INCLUDE_PATH
```

## `RPATH`
[wiki](https://en.wikipedia.org/wiki/Rpath)
Runtime search paths for shared libraries 
Not sure what this is used for.
