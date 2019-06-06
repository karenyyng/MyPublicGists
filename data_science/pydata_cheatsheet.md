# Table of content

<!-- toc -->

- [Numpy](#numpy)
  * [making grids / regular grid points](#making-grids--regular-grid-points)

<!-- tocstop -->

# Numpy

## making grids / regular grid points 
```
np.arange(0, 1, 0.1)  # 3rd argument is the spacing
np.linspace(0, 1, 10)  # 3rd argument is the number of grid points

# return coordinates of grid points with 3 x-spaces and 4 y-spaces
np.indices((3, 4))  
np.meshgrid(range(3), range(4))
```
