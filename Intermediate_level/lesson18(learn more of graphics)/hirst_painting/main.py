import colorgram
# EXTRACTING COLORS FROM THE IMAGE
colors = colorgram.extract('image.jpg',30)
rgb_colors = []
for color in colors:
    r= color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color =(r,g,b)
    rgb_colors.append(new_color)

print(rgb_colors)

color_list_extracted = [(233, 233, 232), (231, 233, 238), (237, 232, 234), (221, 232, 225), (208, 160, 81), (55, 89, 132), (145, 91, 40), (139, 26, 48), (222, 208, 104), (132, 177, 203), (45, 55, 104), (158, 45, 84), (169, 159, 39), (128, 189, 143), (84, 20, 44), (38, 43, 66), (186, 94, 106), (189, 138, 166), (84, 124, 182), (60, 39, 30), (79, 153, 165), (87, 157, 90), (195, 79, 72), (160, 201, 220), (45, 74, 77), (79, 74, 43), (59, 125, 113), (218, 176, 188), (167, 207, 166), (220, 181, 168)]
