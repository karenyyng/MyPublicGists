# Table of content

<!-- toc -->

- [batch profiling](#batch-profiling)
  * [use `cProfile`](#use-cprofile)
    + [saving the stats](#saving-the-stats)
  * [visualizing `cProfile` call tree if needed](#visualizing-cprofile-call-tree-if-needed)
- [profiling functions within ipython](#profiling-functions-within-ipython)
  * [Or use Intel Vtune if possible](#or-use-intel-vtune-if-possible)
    + [How to set up a machine to use the HPC performance profiling mode](#how-to-set-up-a-machine-to-use-the-hpc-performance-profiling-mode)
    + [pros and cons for using Vtune for profiling Python](#pros-and-cons-for-using-vtune-for-profiling-python)
      - [profiling with vtune](#profiling-with-vtune)
- [IO profiling](#io-profiling)

<!-- tocstop -->

# batch profiling
## use `cProfile`
[tutorial](https://docs.python.org/2/library/profile.html#module-cProfile)
```
python -m cProfile -o <profile_of_code>.cprof <script>.py
ipython
import pstats
p = pstats.Stats('<profile_of_code>.cprof')
# to view what function takes up the most time
number_of_lines_to_show = 40
p.strip_dirs().sort_stats('cumtime').print_stats(number_of_lines_to_show)
```
### saving the stats 
[ref](https://docs.python.org/2/library/profile.html#pstats.Stats.dump_stats)

## visualizing `cProfile` call tree if needed
* use `gprof2dot`, install via `pip`

```
$ pip install gprof2dot
$ gprof2dot -f pstats <profile_of_code>.cprof | dot -Tpng -o <profile_of_code>.png
```

# profiling functions within ipython
Install dependencies:
```
conda install line_profiler memory_profiler
```
Open up an ipython interactive session
```
from code import run_function
%load_ext line_profiler
%lprun

%load_ext memory_profiler
%mprun
```

```
%prun -T lpstat.txt run_function()  # same as cProfile 
%prun -T lpstat.txt %run run_function.py
```
You have to wrap your code into a function.
View the results:
```
head -10 lpstat.txt
```

## Or use Intel Vtune if possible

### How to set up a machine to use the HPC performance profiling mode 
source: Jeongnim, Larry
```
sudo cp -r /opt/intel/vtune_amplifier_xe_${YEAR_VERSION}/sepdk /usr/local
cd /usr/local/sepdk/src
sudo ./build-driver
sudo ./insmod-sep
```
### pros and cons for using Vtune for profiling Python
source of knowledge: [Nathan](nathan.g.greeneltch@intel.com)
* use 2018 version Vtune 
* `memory profiler` is stable 
* only basic `hotspot` is stable for python - it is the most useful for finding slow pieces of code in Python
* `advanced hotspot` is not stable for python
* locks and waits is only an interface - not useful as Python doesn't do multithreading

* if debugging Cython code, Cython code needs proper debugging symbol and source code

#### profiling with vtune 
On internal machines
```
source /opt/intel/parallel_studio_xe_2018/vtune_amplifier_2018/amplxe-vars.sh
amplxe-cl -collect hotspot -- python SCRIPT.py
```

```
$ export ARK=knl
$ amplxe-cl -collect hpc-performance -r r@@@{at}_${ARK} -knob analyze-openmp=true -- numactl -p 1 python ./tests/slow_mtx_ops.py 
```


# IO profiling 
* use darshan that works for both POSIX read and MPI IO read<Paste>
