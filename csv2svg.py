import csv
import svgwrite
import sys
import os

# Get the command line argument for the CSV file
csv_file = sys.argv[1]

# Function to generate SVG file
def generate_svg(address, filename, font_family, font_size=14, width=350, height=100):

    # Make sure there is a directory called 'output_svg' to save the SVG files
    # If not, create it
    if not os.path.exists('output_svg'):
        os.makedirs('output_svg')

    dwg = svgwrite.Drawing('output_svg/' + filename, profile='tiny', size=(f"{width}px", f"{height}px"))
    # dwg.add(dwg.text(address, insert=(10, 20), font_family=font_family, font_size=14))
    # Adding text lines to SVG
    lines = address.split('\n')
    for i, line in enumerate(lines):
        dwg.add(dwg.text(line, insert=(10, 20 + i * 20), font_family=font_family, font_size=font_size, font_style=font_style))

    dwg.save()

# Main function to read CSV and generate SVGs
def main(csv_file, font_family):
    with open(csv_file, 'r', newline='') as file:
        reader = csv.reader(file)
        for i, row in enumerate(reader):
            name = row[0]
            street1 = row[2]
            street2 = row[3]
            city = row[4]
            state = row[5]
            zip_code = row[6]
            # Zero pad zip code if it is not 5 digits
            zip_code = zip_code.zfill(5)

            # If we don't have anything in street 1, skip this one
            if (street1 == ''):
                continue

            if (street2 == ''):
                address = f"{name}\n{street1}\n{city}, {state} {zip_code}"
            else:
                address = f"{name}\n{street1}\n{street2}\n{city}, {state} {zip_code}"

            # Generate SVG filename
            svg_filename = f"address_{i}.svg"
            generate_svg(address, svg_filename, font_family, font_size)
            
            

            
            print(f"Generated {svg_filename}")

if __name__ == "__main__":
    # Specify the CSV file and the font family to use
    if csv_file == '':
        csv_file = 'addresses.csv'
    # font_family = 'Segoe Script'
    # font_family = 'Wonderful Christmas PERSONAL'
    font_family = 'Arial'
    font_size = 16

    # font style can be 'normal', 'italic', 'oblique'
    font_style = 'italic'
    main(csv_file, font_family)
