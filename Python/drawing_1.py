import py5

def setup():
    py5.size(980, 980)
    py5.background(240)
    margin = 50

    for i in range(20):
        py5.line(margin + i * 8, 150, margin + i * 16, 600)

py5.run_sketch()