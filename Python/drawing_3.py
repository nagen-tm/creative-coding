import py5

#creating polygons/stars
def setup():
    py5.size(980, 980)
    py5.background(240)
    points = [(200, 200), (500,100), (400, 400), (300, 200), (100, 500)]
    polygon(points)
    star(py5.width / 2, py5.height / 2, 200, 100)
    star_comp(600, 600, 150, 50, 11)

def polygon(points):
    py5.begin_shape()
    for x, y, in points:
        py5.vertex(x, y)
    py5.end_shape(py5.CLOSE)

def star(xcenter, ycenter, wa, wb):
    star = [(-wa, -wa), (0, -wb), (wa, -wa), 
    (wb, 0), (wa, wa), (0, wb), (-wa, wa), (-wb, 0)]

    py5.begin_shape()
    for x, y, in star:
        py5.vertex(xcenter + x, ycenter + y)
    py5.end_shape(py5.CLOSE)

def star_comp(cx, cy, ra, rb, np, start_ang=0):
    step = py5.TWO_PI / np
    py5.begin_shape()
    for i in range(np):
        ang = start_ang + step * i + py5.frame_count / 50.0 
        ax = cx + py5.cos(ang) * ra
        ay = cy + py5.sin(ang) * ra
        py5.vertex(ax, ay)
        bx = cx + py5.cos(ang + step / 2.0) * rb
        by = cy + py5.sin(ang + step / 2.0) * rb
        py5.vertex(bx, by)
    py5.end_shape(py5.CLOSE)


py5.run_sketch()