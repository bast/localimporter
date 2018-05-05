[![License](https://img.shields.io/badge/license-%20MPL--v2.0-blue.svg)](LICENSE)


# localimporter: locates sources which might require an include reorder

Script that goes through your C/C++ project and finds sources which include
standard headers before including local headers.

You may then consider reordering these.

Why? Because importing standard headers first may mask missing imports in your
own local headers and sources and they otherwise may stop compiling if the
order changes or if somebody uses them in another code.

The script does not modify any files.


## Example

```shell
$ python localimporter.py --root /home/user/exciting-project

the following sources include standard headers
before including local headers:

/home/user/exciting-project/src/this.hpp
/home/user/exciting-project/src/that.h
/home/user/exciting-project/src/another.cpp
/home/user/exciting-project/src/somelib.c
/home/user/exciting-project/src/main.cpp

$ python localimporter.py --root /home/user/exciting-project --suffixes "['hpp']"

the following sources include standard headers
before including local headers:

/home/user/exciting-project/src/this.hpp
```


## Command line options

```
$ python localimporter.py --help
Usage: localimporter.py [OPTIONS]

Options:
  --root TEXT      Directory root under which the script will search files.
  --suffixes TEXT  List of suffixes to search, default: ['h', 'hpp', 'c',
                   'cpp'].
  --help           Show this message and exit.
```
