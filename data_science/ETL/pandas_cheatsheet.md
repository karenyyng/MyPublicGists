# References 
* [Python for data analysis Ch. 9]

# Groupby, manipulate, transforming a df 
## How to use groupby and apply functions
```Python
gpBy = df.groupby(["col1", "col2"])
```
By default, the Pandas groupby will use `col1` and `col2` as your new index.
If you wish to use the `groupBy` object as a dataframe entry, it is better to instead do:
```Python
gpBy = df.groupby(["col1", "col2"]", as_index=False)
```



Then you can convert the gpBy object using
```Python
grouped_df = gpBy.reset_index()  # somehow this stopped working.
```

## Finding out what groups there are after the groupby:
```Python
gp_key = gpBy.groups.keys()
```
## Examine each group
[SO post](http://stackoverflow.com/questions/22407798/pandas-group-by-how-to-reset-indexes-for-all-groups-in-one-step)
```
grouped.get_group(gp_key[0])
```


```Python
gpBy.apply(lambda df_row, args: func(df_row, args), axis=1)
```
When using apply, imagine the first argument supplied to the function 
to be the `df_row` from the groupby object.
If you want to apply the function to each column instead, use `axis=0`.

Or if you want to specify the df col to be supplied to the function, do
```Python
gpBy.apply(lambda df_row, args: func(df_row.col1, df_row.col2, args), axis=1)
```

If you want to perform functions for each group then use:
```Python
gpBy.agg(function)
```
instead.


## Iterating over groups
```Python
for (k1, k2), group in df.groupby(['k1, k2']):
    print (k1, k2)
    print group
```


## return groups of objects as dictionary of df, do
```Python
gps = dict(list(grouped))
```
And the groupby index values can be found by:
```Python
gps.keys()
```

## Scatter matrix plot
[ref from documentation](http://pandas.pydata.org/pandas-docs/version/0.15.0/visualization.html#visualization-scatter-matrix)
```Python
# from pandas.tools.plotting import scatter_matrix
from pandas.plotting import scatter_matrix
df = DataFrame(randn(1000, 4), columns=['a', 'b', 'c', 'd'])
_ = scatter_matrix(df, alpha=0.2, figsize=(12, 12), diagonal='kde')
```

How to tweak axes labels or so for scatter matrix plots:
```
axArray = scatter_matrix(df[offsets], diagonal='kde', alpha=0.3,
                        figsize=(15, 15))


# for illustration purposes only, 
# the axis arange varies from mosaic to mosaic 
# which makes it hard for comparison
for axTemp in axArray:
    for ax in axTemp: 
        for item in ([ax.title, ax.xaxis.label, ax.yaxis.label]): 
            item.set_fontsize(12)
            item.set_rotation(90)
        for item in (ax.get_xticklabels() + ax.get_yticklabels()):
            item.set_fontsize(8)
            item.set_rotation(90)
```

## Dropping columns from pandas dataframe
[SO post](http://stackoverflow.com/questions/13411544/delete-column-from-pandas-dataframe)    


## displaying dataframe in Jupyter notebook 
```
from IPython.display import display, HTML
display(HTML(df2.to_html()))
```

### rounding to 2 d.p. for floats
```
display(df2.round(2))
```

### highlighting cells:
[ref](https://stackoverflow.com/questions/41555678/highlighting-multiple-cells-in-different-colors-with-pandas)
