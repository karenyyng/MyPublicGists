# traversing the directory keys of a `hdf5` file 
```Python
from __future__ import print_function
import h5py
h5file = h5py.File("PATH_TO_FILE")
h5file.visit(print) 
```
the `visit` method takes a function as its argument and supply the key of the file to the function.

# navigating different keys of a file
```Python
file["key1/subkey2/subsubkey3/"] 
```
You can chain the keys as a string.

## guide to hdf5
# to traverse the hdf5 directory structure and apply a function to the arguments:
```
import h5py
h5File = h5py.File("PATH_TO_h5_FILE")
h5File.visit(function)
h5File["group"].visit
```
but we may not want to visit ALL the elements, in that case we can use
`.iteritems()` instead.
