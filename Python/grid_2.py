import py5

seed = 1

#introducing random
def setup():
    py5.size(700, 980)

def draw():
    py5.random_seed(seed)
    py5.background(0, 0, 100)
    py5.stroke(255)
    for i in range(3):
        grid(100, 6, 8)

def grid(margin_x, columns, rows):
    w = (py5.width - 2 * margin_x) / columns
    margin_y = (py5.height - w * rows) / 2
    
    for j in range(rows):
        for i in range(columns):
            y = margin_y + j * w + w / 2
            x = margin_x + i * w + w / 2
            r = py5.random_int(0, 128)
            g = py5.random_int(128, 255)
            b = py5.random_int(0, 255)

            randomizer = py5.random_int(1, 6)
            if randomizer == 1:
                py5.fill(r, g, b, 128)
                ra = py5.random(w / 20, w / 2)
                rb = py5.random(1, w / 2)
                np = py5.random_int(4, 10)
                star(x, y , ra, rb, np)
            elif 1 < randomizer < 4:
                py5.fill(255, 64)
                dr = py5.random_int(0, 1) * w / 2
                py5.rect(x - dr, y-dr, w / 2, w / 2 )
            elif 4<= randomizer < 6:
                py5.fill(200,64)
                py5.rect(x - w / 2, y - w / 2, w, w)
            else:
                py5.fill(r, g, b, 64)
                py5.circle(x, y, py5.random_int(1,2) * w/4)

def star(cx, cy, ra, rb, np, start_ang=0):
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

def mouse_pressed():
    global seed
    seed = seed + 1
    print(f'random seed: {seed}')

def key_pressed():
    if py5.key == 's':
        py5.save_frame(f'output-{seed}.png')
        print('saved png')

py5.run_sketch()