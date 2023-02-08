red = 20 / 255.0
green = 150 / 255.0
blue = 20 / 255.0

tab_color_HSV = [0, 0, 0]

cMax = max(red, green, blue)
cMin = min(red, green, blue)

alpha = cMax - cMin

# teinte
if alpha == 0:
    tab_color_HSV[0] = 0
if cMax == red:
    tab_color_HSV[0] = 60 * ((green - blue) / alpha) % 6
if cMax == green:
    tab_color_HSV[0] = 60 * (((blue - red) / alpha) + 2)
if cMax == blue:
    tab_color_HSV[0] = 60 * (((red - green) / alpha) + 4)

# saturation
if cMax == 0:
    tab_color_HSV[1] = 0
else:
    tab_color_HSV[1] = alpha / cMax

# value
tab_color_HSV[2] = cMax

print(tab_color_HSV)
