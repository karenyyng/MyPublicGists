# Table of content

<!-- toc -->

- [making simple plot](#making-simple-plot)
  * [to show plot within Jupyter notebook](#to-show-plot-within-jupyter-notebook)
  * [use ColumnDataSource](#use-columndatasource)
  * [adding legend to plot with specific location](#adding-legend-to-plot-with-specific-location)
  * [saving the plot to html](#saving-the-plot-to-html)
  * [bokeh modules / objects to import](#bokeh-modules--objects-to-import)
  * [arrange plots in a layout with widgets](#arrange-plots-in-a-layout-with-widgets)

<!-- tocstop -->

# making simple plot 

## to show plot within Jupyter notebook 

execute this following line at the top of the notebook
```python
output_notebook()
```

```python
from bokeh.io import output_notebook, output_file
from bokeh.plotting import figure, show, ColumnDataSource

x_values = [1, 2, 3, 4, 5]
y_values = [6, 7, 2, 3, 6]

p = figure(width=800, height=600, title='TITLE OF THE PLOT')
p.circle(x=x_values, y=y_values, legend='to appear on the legend')
p.legend.location = "center_right"
p.legend.background_fill_color = "darkgrey"
p.xaxis.axis_label = 'x'
p.yaxis.axis_label = 'Pr(x)'

show(p)
```


## use ColumnDataSource 
such as dataframes
```python
from bokeh.models import HoverTools
data = {'x_values': [1, 2, 3, 4, 5],
        'y_values': [6, 7, 2, 3, 6]}

source = ColumnDataSource(data=data)

# use `@` to retrieve the column values from a dataframe
# use `$x` to retrieve the x value of the plotted point
hover = HoverTool(tooltips=[
    ("(x, y)", "(@x_values, @y_values)"),
    ("x", "$x{0}")  # this `{0}` will make sure that the hover values are integers with 0 decimial points
])
p = figure(tools=[hover, 'pan', 'save', 'box_zoom'])
p.circle(x='x_values', y='y_values', source=source, )

show(p)

```
[ref for using HoverTool](https://bokeh.pydata.org/en/latest/docs/user_guide/tools.html#basic-tooltips)
[ref for other tools](https://bokeh.pydata.org/en/latest/docs/user_guide/tools.html)
specify the default tool by their names as strings

[ref](https://stackoverflow.com/questions/44958328/how-to-show-only-integers-in-bokeh-hovertool) to make sure hovertools show integers for numerical values

## adding legend to plot with specific location
[ref](https://stackoverflow.com/questions/46730609/position-the-legend-outside-the-plot-area-with-bokeh)

```python
r0 = p.line(x, y, source=source)
r1 = p.line(x1, y1, source=source)
r2 = p.line(x2, y2, source=source)
r3 = p.line(x3, y3, source=source)
legend = Legend(items=[
    ("sin(x)",   [r0, r1]),
    ("2*sin(x)", [r2]),
    ("3*sin(x)", [r3,])
], location=(0, -30))

p.add_layout(legend, 'right')

```


## saving the plot to html 
Just add the following line
```python
output_file('histogram.html', title="histogram.py example")
```


## bokeh modules / objects to import
```python
from bokeh.io import output_notebook
from bokeh.plotting import figure, show, ColumnDataSource
from bokeh.models import HoverTool, Legend
```
## arrange plots in a layout with widgets
[ref](https://bokeh.pydata.org/en/latest/docs/user_guide/layout.html)
```
from bokeh.layouts import column, row, gridplot, widgetbox
from bokeh.models.widgets import Button, RadioButtonGroup, Select, Slider

```
