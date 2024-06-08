import py5

#introducing random
def setup():
    py5.size(980, 980)
    py5.background(240)

    py5.fill(0)
    py5.no_stroke()
    for x in range(50, 930, 50):
        d = py5.random(10,50)
        py5.circle(x, 50, d)
    
    for x in range(50, 930, 50):
        i = py5.random_int(1,4)
        py5.circle(x, 150, 10+i * 10)
    
    for x in range(50, 930, 50):
        r = py5.random_int(255)
        g = py5.random_int(255)
        b = py5.random_int(255)
        py5.fill(r,g,b)
        py5.circle(x, 250, 45)

    for x in range(50, 930, 50):
        r = 0
        g = py5.random_int(255)
        b = py5.random_int(255)
        py5.fill(r,g,b)
        py5.circle(x, 350, 45)

    for x in range(50, 930, 50):
        r = 0
        g = py5.random_int(128, 255)
        b = 128
        py5.fill(r,g,b)
        py5.circle(x, 450, 45)

    colors = [
        py5.color(255, 200, 0),
        py5.color(0, 128, 255),
        py5.color(128, 255, 0)
    ]

    for x in range(50, 930, 50):
        py5.fill(py5.random_choice(colors))
        py5.circle(x, 550, 45)
    
    for x in range(50, 930, 100):
        v = py5.random_int(1,7)
        if v == 1:
            py5.circle(x, 650, 50)
        elif v == 2:
            py5.square(x, 650, 50)
        else:
            r = py5.random_choice((10,25,40))
            star_comp(x, 650, r, 30, v)



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