def brush_strokes(skyline):
    brushCount = 0
    prevHeight = 0

    for i in range(len(skyline)):
        if skyline[i] > prevHeight:
            brushCount = brushCount + (skyline[i] - prevHeight)
        prevHeight = skyline[i]

    return brushCount
