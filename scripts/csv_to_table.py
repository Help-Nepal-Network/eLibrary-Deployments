import pandas as pd

# Load CSV data into a DataFrame
csv_file = '../HeNN_eLibraries_Sheet.csv'
columns_to_include = ['Site Name', 'Location', 'Deployment Date']

df = pd.read_csv(csv_file, usecols=columns_to_include)

# Convert DataFrame to markdown table
markdown_table = df.to_markdown(index=False)

# Save markdown table to a file
markdown_path = 'markdown_table.md'
with open(markdown_path, 'w') as markdown_file:
    markdown_file.write(markdown_table)

html_table = df.to_html(index=False)

html_path = 'html_table.html'
with open(html_path, 'w') as markdown_file:
    markdown_file.write(html_table)

