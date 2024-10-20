from IPython.display import display, HTML
import pandas as pd

def style_table(data, caption, column_cmap=None, width="100px", border="1px solid black", 
                header_background="lightblue", row_height="15px", hide_index=False, 
                reverse_cmap=False, font_size="14px", font_family="Arial"):
    """
    Function to style and center a DataFrame or a dictionary in a Jupyter Notebook with customization options for the header background, row height, column gradients,
    font size/type, and an option to hide the index.

    Parameters:
    - data: Can be a dictionary or DataFrame to style.
    - caption: The title or subtitle of the table.
    - column_cmap: A dictionary where the keys are column names (or indices) and the values are colormaps to apply.
    - width: Column width (default is "100px").
    - border: Border style for the cells (default is "1px solid black").
    - header_background: Background color for the headers (default is "lightblue").
    - row_height: Row height of the table (default is "15px").
    - hide_index: Boolean to determine whether to hide the index (default is False).
    - reverse_cmap: Boolean flag to reverse the colormap for all columns where cmap is applied (default is False).
    - font_size: Font size for the table content (default is "14px").
    - font_family: Font family for the table content (default is "Arial").
    """

    # Convert the data to a DataFrame if it's a dictionary
    if isinstance(data, dict):
        df = pd.DataFrame(data)
    else:
        df = data  # Assume it's already a DataFrame

    # Number of columns in the DataFrame
    num_columns = len(df.columns)

    # Create a list of styles for the table, with fonts, centered on all columns, with borders, header background, and row height
    table_styles = [
        {'selector': 'caption', 'props': [('font-size', '16px'), ('font-weight', 'bold'), ('color', 'black'), ('font-family', font_family)]},  # Bold title with font family
        {'selector': 'th', 'props': [('width', width), ('text-align', 'center'), ('border', border), 
                                     ('background-color', header_background), 
                                     ('font-size', font_size), ('font-family', font_family)]},  # Header background, font size, and font family
        {'selector': 'td', 'props': [('width', width), ('border', border), ('height', row_height), 
                                     ('font-size', font_size), ('font-family', font_family)]}  # Set width, border, row height, and font styles for data cells
    ]

    # Center the text in all columns
    for col in range(1, num_columns + 2):  
        table_styles.append({'selector': f'td:nth-child({col})', 'props': [('text-align', 'center'), ('border', border), 
                                                                           ('height', row_height), ('font-size', font_size), 
                                                                           ('font-family', font_family)]})

    # Apply the styles to the DataFrame
    styled_df = df.style.set_caption(caption).set_table_styles(table_styles)

    # Optionally hide the index
    if hide_index:
        styled_df = styled_df.hide(axis="index")

    # Apply gradients based on the column_cmap dictionary (if provided)
    if column_cmap:
        for col, cmap in column_cmap.items():
            # If reverse_cmap is True, reverse the colormap for all columns
            if reverse_cmap:
                styled_df = styled_df.background_gradient(cmap=cmap + '_r', subset=[col])
            else:
                styled_df = styled_df.background_gradient(cmap=cmap, subset=[col])

    # Convert the styled DataFrame to HTML
    styled_html = styled_df.to_html()

    # Display the HTML table centered
    display(HTML(f"""
    <div style="display: flex; justify-content: center;">
        {styled_html}
    </div>
    """))
