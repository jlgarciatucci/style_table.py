# style_table.py

![Your Library Logo](https://img.shields.io/badge/Version-0.1.0-blue.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

`style_table` is a Python package designed to provide an easy way to style pandas DataFrames in Jupyter Notebooks. It supports custom styling for headers, cell backgrounds, and gradients, with additional options for formatting and display.

## Key Features

- **Customizable table styles:** Set the width, row height, borders, and more.
- **Apply gradients:** Use colormaps to add color gradients to columns.
- **Flexible options:** Hide the index, reverse color maps, and adjust other table properties.
- **Centered display:** Automatically centers the table output in Jupyter Notebooks.

## Installation

You can install this package directly from PyPI:

```bash
pip install style_table
```

## Parameters
- **data:** The DataFrame or dictionary to style.
- **caption:** A title or subtitle for the table.
- **column_cmap:** A dictionary where keys are column names and values are colormaps.
- **width:** Width of each column (default is "100px").
- **border:** Border style for cells (default is "1px solid black").
- **header_background:** Background color for the table header (default is "lightblue").
- **row_height:** Row height (default is "15px").
- **hide_index:** Whether to hide the DataFrame index (default is False).
- **reverse_cmap:** Reverse the colormap (default is False).
- **font_size:** Font size for the table content (default is "14px").
- **font_family:** Font family for the table content (default is "Arial").


## 1. Basic Styling with Custom Fonts
This example demonstrates how to load the Iris dataset and apply basic styling with custom font size and font family.
```python
import style_table
import pandas as pd
from sklearn.datasets import load_iris

# Load the Iris dataset
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)

# Apply styling with custom font size and font family
style_table(df.head(10), caption="Iris Flower Dataset with Custom Fonts", font_size="16px", font_family="Verdana")
```
<div align="center"> <img src="https://github.com/user-attachments/assets/03d8f00e-816d-431a-ada2-b65460512a59" alt="Centered Image" /> </div>

## 2. Styling with Column Gradients and Custom Fonts
In this example, we apply color gradients to the sepal length and petal length columns, along with customized fonts.
```python
import style_table
import pandas as pd
from sklearn.datasets import load_iris

# Load the Iris dataset
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)

# Apply a gradient and custom font
style_table(df.head(10), caption="Iris Dataset with Gradients and Fonts", column_cmap={
    "sepal length (cm)": "Blues",
    "petal length (cm)": "Greens"
}, font_size="14px", font_family="Helvetica")
```
<div align="center"> <img src="https://github.com/user-attachments/assets/72ac0470-1fbf-4aa1-a483-bc034221cd52" alt="Centered Image" /> </div>

## 3. Reversed Gradients with Large Font
This example demonstrates how to reverse a colormap for the petal width column while using a larger font size.
```python
import style_table
import pandas as pd
from sklearn.datasets import load_iris

# Load the Iris dataset
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)

# Apply reversed gradient to 'petal width' and set larger font size
style_table(df.head(10), caption="Iris Dataset with Reversed Gradient and Large Font", column_cmap={
    "petal width (cm)": "Oranges"
}, reverse_cmap=True, font_size="18px", font_family="Georgia")
```
<div align="center"> <img src="https://github.com/user-attachments/assets/d098e627-4e62-455d-a069-eb757c33eac7" alt="Centered Image" /> </div>

## 4. Hiding the Index with Custom Fonts
In this example, we hide the DataFrame index, use a larger font size, and apply a custom font family.
```python
import style_table
import pandas as pd
from sklearn.datasets import load_iris

# Load the Iris dataset
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)

# Hide the index and use custom fonts
style_table(df.head(10), caption="Iris Dataset (Index Hidden, Custom Fonts)", hide_index=True, font_size="16px", font_family="Courier New")
```
<div align="center"> <img src="https://github.com/user-attachments/assets/2f403b56-393f-48ca-9d58-1fca963218ca" alt="Centered Image" /> </div>

## 5. Combining All Features: Gradients, Hidden Index, and Fonts
In this final example, we apply gradients, hide the index, and customize both the font size and family for a fully styled table.
```pyhton
import style_table
import pandas as pd
from sklearn.datasets import load_iris

# Load the Iris dataset
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)

# Apply all customizations: gradients, hidden index, and fonts
style_table(df.head(10), caption="Fully Styled Iris Dataset", column_cmap={
    "sepal length (cm)": "Blues",
    "petal length (cm)": "Greens",
    "petal width (cm)": "Oranges"
}, width="200px", border="3px dotted",hide_index=True, header_background="aliceblue", font_size="12px", font_family="Calibri")
```
<div align="center"> <img src="https://github.com/user-attachments/assets/265f3905-abd6-41c3-ae58-80ea62b5e652" alt="Centered Image" /> </div>


