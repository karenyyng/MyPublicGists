# Table of content

<!-- toc -->

- [All things about contour plot](#all-things-about-contour-plot)
  * [Contour plot with log axes](#contour-plot-with-log-axes)
  * [Making contour plot or so with log colors](#making-contour-plot-or-so-with-log-colors)
  * [similarly specifying color range for contour plot](#similarly-specifying-color-range-for-contour-plot)
  * [putting color bar on a different axis](#putting-color-bar-on-a-different-axis)
- [Plot aspects](#plot-aspects)
  * [making plots with multiple panels (subplots)](#making-plots-with-multiple-panels-subplots)
    + [perhaps the best approach](#perhaps-the-best-approach)
    + [More complicated approach](#more-complicated-approach)
    + [slightly less complicated approach](#slightly-less-complicated-approach)
    + [Colormap](#colormap)
      - [Revert colormap](#revert-colormap)
  * [Rotate axis labels](#rotate-axis-labels)
  * [Adjust subplots spacing](#adjust-subplots-spacing)
  * [colorbar label size](#colorbar-label-size)
- [plot frame](#plot-frame)
    + [[remove upper / right axis ticks]](#remove-upper--right-axis-ticks)
    + [[change the direction of the ticks]](#change-the-direction-of-the-ticks)
  * [color blind friendly map](#color-blind-friendly-map)
- [pandas scattermatrix plotting](#pandas-scattermatrix-plotting)
- [pandas KDE](#pandas-kde)
- [legend](#legend)
- [legend outside plot](#legend-outside-plot)

<!-- tocstop -->

# All things about contour plot
## Contour plot with log axes 
[Post](http://matplotlib.1069221.n5.nabble.com/contour-plots-with-logarithmic-axes-td8732.html)
# approach 1 
```Python
z = np.arange(100).reshape((10,10)) 
x = np.logspace(0, 4, 10) 
y = np.logspace(0, 4, 10) 

ax1 = subplot(121) 
ax1.contour(np.log10(x), np.log10(y), z) 
```

# approach 2 
```Python
ax2 = subplot(122) 
ax2.set_xscale("log") 
ax2.set_yscale("log") 
ax2.contour(x, y, z) 
```

## Making contour plot or so with log colors
[ref](http://matplotlib.org/examples/pylab_examples/pcolor_log.html)

```Python
from matplotlib.colors import LogNorm
plt.pcolor(X, Y, Z1, norm=LogNorm(vmin=Z1.min(), vmax=Z1.max()), cmap='PuBu_r')
```

## similarly specifying color range for contour plot 
Use `vmin` and `vmax` keyword.

## putting color bar on a different axis
[SO post](http://stackoverflow.com/questions/13784201/matplotlib-2-subplots-1-colorbar)
```python
ig, axes = plt.subplots(nrows=2, ncols=2)
for ax in axes.flat:
    im = ax.imshow(np.random.random((10,10)), vmin=0, vmax=1)

fig.subplots_adjust(right=0.8)
cbar_ax = fig.add_axes([0.85, 0.15, 0.05, 0.7])
fig.colorbar(im, cax=cbar_ax)
```

# Plot aspects
```Python
plt.axes().set_aspect('equal')   # ratio of long to short dimensions
```
when you want the X and Y axes have the same size dimensions for each unit.


## making plots with multiple panels (subplots)
### perhaps the best approach 
using gridspec
```Python
import matplotlib.gridspec as gridspec
# specify the overall figure size 
plt.figure(figsize=(6, 6))
# specify a 2 x 2 grid 
gs = gridspec.GridSpec(2, 2, width_ratios=[1, 1], 
                       height_ratios=[1, 1])
gs.update(hspace=0.2, wspace=0.5)
# add a lower triangle and have each axis named accordingly 
ax00 = plt.subplot(gs[0, 0])
ax10 = plt.subplot(gs[1, 0])
ax11 = plt.subplot(gs[1, 1])
# use each axis to make whatever plots!
```


### More complicated approach 
* with more fine grained control

```Python
fig = plt.figure()
ax1 = fig.add_subplot(<row_no>, <col_no>, <plot_no_1>)
ax1.plot()

ax2 = fig.add_subplot(<row_no>, <col_no>, <plot_no_2>)
ax2.plot()
...
# saving all the subplots

fig.savefig("plot_name.png", bbox_inches='tight')
```

### slightly less complicated approach
[ref](http://matplotlib.org/examples/pylab_examples/subplots_demo.html)


### Colormap
[ref](https://jakevdp.github.io/blog/2014/10/16/how-bad-is-your-colormap/)

#### Revert colormap 
append `_r` to the name of the colormap, e.g. use `cubehelix_r` instead of `cubehelix`


## Rotate axis labels
```
plt.xticks(rotation=45)
```

[SO post](http://stackoverflow.com/questions/14852821/aligning-rotated-xticklabels-with-their-respective-xticks)

Or
[ref](https://stackoverflow.com/questions/10998621/rotate-axis-text-in-python-matplotlib/10998872#10998872)
```Python
locs, labels = plt.xticks()

plt.setp(labels, rotation=90)
plt.plot(x, delay)
```

## Adjust subplots spacing
[SO post](http://stackoverflow.com/questions/6541123/improve-subplot-size-spacing-with-many-subplots-in-matplotlib)

## colorbar label size
```Python
cbar = fig.colorbar(surf, shrink=0.5, aspect=20, fraction=.12,pad=.02)
cbar.set_label('Activation',size=18)
# access to cbar tick labels:
cbar.ax.tick_params(labelsize=5) 
```
[ref](http://stackoverflow.com/questions/6567724/matplotlib-so-log-axis-only-has-minor-tick-mark-labels-at-specified-points-also/6568248)

# plot frame 
[remove upper / right axis line](http://stackoverflow.com/questions/925024/how-can-i-remove-the-top-and-right-axis-in-matplotlib)

### [remove upper / right axis ticks]
```Python
ax.tick_params(labeltop='off', labelright='off')
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')
```

### [change the direction of the ticks]
```Python
mpl.rcParams['xtick.direction']= out
mpl.rcParmas['ytick.direction'] = out
```

## color blind friendly map
[ref](http://bconnelly.net/2013/10/creating-colorblind-friendly-figures/)   


Fix in `~/matplotlib/matplotlib.rc` 
```Python
# colorblind friendly color cycler 
axes.prop_cycle    : cycler('color', 'E69F00, 56B4E9, 009E73, 0072B2, D55E00, CC79A7, F0E442, 000000')
```
Alternative colormap [tableau colors](http://tableaufriction.blogspot.ro/2012/11/finally-you-can-use-tableau-data-colors.html)

# pandas scattermatrix plotting

control axis limits for Pandas kde plots 
```python
from pandas.plotting import scatter_matrix
axes = scatter_matrix(pointOfSalesDf[:], alpha=0.1, 
                      figsize=(10, 10), diagonal='kde')
_ = axes[0][0].set_xlim(*sales_xlim)
_ = axes[0][0].set_ylim(*inv_xlim)

_ = axes[1][0].set_xlim(*sales_xlim)
_ = axes[1][0].set_ylim(*inv_xlim)

_ = axes[0][1].set_xlim(*inv_xlim)
_ = axes[0][1].set_ylim(*sales_xlim)

_ = axes[1][1].set_xlim(*inv_xlim)
_ = axes[1][1].set_ylim(*sales_xlim)
```

# pandas KDE 
```
ax = pointOfSalesDf.OHInvUnts_WTD.plot.kde()
_ = ax.set_xlim(-1e4, 5e3)
```

# legend
```python
plt.plot(x, y, title='STUFF')
plt.legend()
```

# legend outside plot
[ref](https://stackoverflow.com/questions/7125009/how-to-change-legend-size-with-matplotlib-pyplot)
use `bbox_to_anchor` keyword
```
plt.legend(loc="upper left", bbox_to_anchor=(1,1))
```
