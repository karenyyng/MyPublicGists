# Table of content

<!-- toc -->

- [Cheatsheet for using Jupyter notebook](#cheatsheet-for-using-jupyter-notebook)
  * [display more lines without having a scroll bar for the output](#display-more-lines-without-having-a-scroll-bar-for-the-output)
  * [cell magic vs line magic](#cell-magic-vs-line-magic)
  * [display matplotlib plots](#display-matplotlib-plots)

<!-- tocstop -->

# Cheatsheet for using Jupyter notebook

## display more lines without having a scroll bar for the output
tweak the javascript
```
%%javascript
IPython.OutputArea.auto_scroll_threshold = 9999;
```

## cell magic vs line magic
cell magic starts with two `%%`
```python
%%time
CODE_SHOULD_START_ON_THE_NEXT_LINE
```
line magic starts with only one `%`

```python
%time ONE_LINE_OF_CODE
```

## display matplotlib plots 
```python
%matplotlib inline
```
or if you want more interactions with matplotlib plots within the notebook, use
```
%matplotlib notebook
```
but if you use the `notebook` option, you need to create a `matplotlib` figure separately each time or else the latest plot will overwrite the previous plot as they share the same `figure` object. E.g. before plotting each figure, enter the following to create a new figure object.

```python
fig = plt.figure()
ax = ax.add_subplot(111)
ax.plot(x, y)
plt.show()
```
