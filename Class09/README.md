# Class 09

- [Class 09](#class-09)
- [c09ex01 - "Chuckifier"](#c09ex01---%22chuckifier%22)
- [Jupyter Notebooks](#jupyter-notebooks)
    - [Installing Jupyter Notebooks](#installing-jupyter-notebooks)
    - [Using jupyter notebooks](#using-jupyter-notebooks)
    - [Creating your first Jupyter notebook](#creating-your-first-jupyter-notebook)
    - [Navigating Jupyter](#navigating-jupyter)
  - [Modes and Cell Types](#modes-and-cell-types)
    - [Modes](#modes)
    - [Cell type](#cell-type)

# c09ex01 - "Chuckifier"

Write a command line program that accepts a first and last name and prints a message from the Chuck Norris Web API with the given First and Last name. 

http://www.icndb.com/api/


# Jupyter Notebooks

Jupyter Notebook is a client server (web application) that you can use to create and share documents that contain live Python code (it also can be configured for other languages such as R), explanatory text (written in markdown), and visualizations.

Jupyter notebooks are used for data processing, simulation, data modeling, and machine learning. It's also used in fields such as finance and economics. 

### Installing Jupyter Notebooks

One of the advantages of using the Anaconda distribution of Python is that Jupyter Notebook (and other python tools and libraries) come pre-installed. 

To check if it's installed, fun the following from your terminal

```
jupyter notebook
```

If there is an error -- please check with the professor.


### Using jupyter notebooks

You can start a Jupyter notebook from the Anaconda Navigator or (as shown above) from the command prompt. One of the advantages of running from the command prompt, is that you can control which directory you wish to have Jupyter use. 

### Creating your first Jupyter notebook

Using the command prompt, navigate to directory that you use for experimentation (in my case, Sandbox). Then type `jupyter notebook` and then select "new" to create a new Jupyter notebook.

After doing this, you should see the following:

![jupyter3.png](./Images/jupyter3.png)


You can change the name of your notebook by clicking on the "Untitled" area, and entering the name you wish to have the notebook called.

in the enter box on your newly created notebook, enter print("Hello World!) and then click the run button.

![jupyter5.png](./Images/jupyter5.png)

### Navigating Jupyter

CTRL-SHIFT-P will bring up a menu of all the commands.

![jupyter4.png](./Images/jupyter4.png)

## Modes and Cell Types

### Modes

When a cell is selected, it will be highlighted in either blue or green. Green indicates that the cell is in edit more, while blue indicates that the cell is in command mode.

Clicking to the left of the cell (the In [?] area) will put the cell in command mode. Clicking in the edit window will put the cell in edit more.

### Cell type

By default, Jupyter cells are "code" cells. You can change the cell mode by selecting the cell and the menu item cell -> cell type. The two cell types we will use in this course are the code type (which is where you'll enter python code) and the Markdown type (which will allow you to enter Markdown code that will be rendered on the page when run)

Try changing the second cell to Markdown mode, and enter a Markdown header and then run Jupyter.

![jupyter6.png](./Images/jupyter6.png)

Though Jupyter has many useful menu items, you often want to use keyboard commands.

| Key Stroke | Description
|----|----|
| CTRL-SHIFT-P | List all keyboard shortcuts |
CTRL-Enter | Run the contents of a code cell, or render the contents of a Markdown cell. |
|SHIFT-Enter| same as CTRL-Enter but inserts a new cell after the current one |
| Esc|Enter command mode, where you can navigate around using arrow keys.|
| A | Insert a new cell above the current cell|
| B | Insert a new cell below the current cell|
| M | Change the cell type to Markdown |
| Y | Change the cell type to Code |
|D + D| Press D twice to delete the current cell|
|Enter|Take you back from command mode to edit mode on a bell|
| SHIFT+TAB|Show Docstring for the python objects you have in your code. Continuing SHIFT-TAB again will cycle through all Docstrings|
| SHIFT - Mouse Click | Multi select cells |
|Shift-M|Merge multiple cells|

A great "cheatsheet" can be found here https://www.cheatography.com/weidadeyue/cheat-sheets/jupyter-notebook/pdf/


For the remaining portion of this class, we will work in the class09.ipynb file (a jupyter notebook). You'll need to download and copy this file into your personal repo directory where you're keeping class notes. You can start a jupyter notebook server in the directory (using bash) and then select this file (within jupyter) to open.which python3.