## Create graphical vector images from a CSV spreadsheet of addresses

This script is for converting/generating address labels as discrete SVG graphic files. It takes a spreadsheet csv (comma delimited) file in the following format:
Full Name, Last Name (only), Address 1, Address 2, City, State, Zip

This could be useful for doing certain types of mail merges, and for making address labels with something like a plotter or CNC machine,
which would benefit from a vector image.

## Usage

`python csv2svg.py [address.csv] [font size] [font family] [font style]`

The .csv file should be comma delimited.

## Output

A directory output_svg will be created, and populated with a single .svg file per valid address line in the provided .csv file.

## Defaults

If not specified, the following defaults are used:

- Font family: Arial
- Font size: 14
- Font style: none
- Width: 350
- Height: 100
