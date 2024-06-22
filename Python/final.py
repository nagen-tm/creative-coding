import py5

seed = 1

#introducing random
def setup():
    py5.size(700, 950)

def draw():
    py5.random_seed(seed)
    py5.background(1, 22, 39)
    py5.no_stroke()
    w = 700
    h = 980
    dot_grid(50, 16, 28, w, h)
    for i in range(6):
        py5.no_stroke()
        points = [(py5.random_int(int(w / 4 - 150), int(w / 4 + 150)), py5.random_int(int(h / 5 - 75), int(h / 5 + 150))), 
              (py5.random_int(int(w / 2 - 75), int(w / 2 + 150)), py5.random_int(int(h * .15), int(h * .25))), 
              (py5.random_int(int(w * .70), int(w * .9)), py5.random_int(int(h * .3), int(h / 2))), 
              (py5.random_int(int(w / 2 - 75), int(w / 2 + 150)), py5.random_int(int(h / 2), int(h * .75))), 
              (py5.random_int(int(w / 4 - 75), int(w / 2)), py5.random_int(h - int(h/3), h - 75))]
        polygon(points)
    for i in range(14):
        py5.stroke(255, 80)
        py5.stroke_weight(py5.random_int(1,9))
        py5.no_fill()
        py5.circle(w/2, h/2, py5.random_int(50, 500))
    for i in range(50, 600, 50):
        py5.stroke(255, 10)
        py5.stroke_weight(2)
        py5.arc(0,0, w/4 + i,w/4 + i, 0,py5.PI/2)
    for i in range(350, 700, 17):
        py5.line(i, h/2, i, h)

def polygon(points):
    r = py5.random_int(0, 128)
    g = py5.random_int(128, 255)
    b = py5.random_int(0, 255)
    py5.fill(r, g, b, 64)
    py5.begin_shape()
    for x, y, in points:
        py5.vertex(x, y)
    py5.end_shape(py5.CLOSE)

def dot_grid(margin_x, columns, rows, tw, th):
    w = (py5.width - 2 * margin_x) / columns
    margin_y = (py5.height - w * rows) / 2
    
    for j in range(rows):
        for i in range(columns):
            y = margin_y + j * w + w / 2
            x = margin_x + i * w + w / 2
            r = py5.random_int(0, 128)
            g = py5.random_int(128, 255)
            b = py5.random_int(0, 255)
            py5.fill(r, g, b, 64)
            py5.circle(x, y, 1 * w/4)
    py5.fill(1, 22, 39)
    py5.no_stroke()
    py5.rect(0, 0, int(tw/2), int(th/2))
    py5.rect(tw/2, th/2, int(tw/2), int(th/2))

def mouse_pressed():
    global seed
    seed = seed + 1

def key_pressed():
    if py5.key == 's':
        py5.save_frame(f'output-{seed}.png')
        print('saved png')

py5.run_sketch()