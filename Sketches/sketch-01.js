const canvasSketch = require('canvas-sketch');

const settings = {
  dimensions: [1080, 1080],
  pixelsPerInch: 300
};

const sketch = () => {
  return ({ context, width, height }) => {
    context.fillStyle = 'white';
    context.fillRect(0, 0, width, height);
    context.lineWidth = width * .01;
    // declare variables
    const w = width * .1;
    const h = height * .1;
    const gap = width * .03;
    const ix = width * .17;
    const iy = height * .17;
    const off = width * .02;

    let x, y;

    for(let i = 0; i < 5; i++){
      for(let j = 0; j < 5; j++){
        x = ix + (w + gap) * i;
        y = iy + (w + gap) * j;

        context.beginPath();
        context.rect(x, y, w, h);
        context.stroke();

        if (Math.random() > 0.5) {
          context.rect(x + off / 2, y + off / 2, w - off, h - off);
          context.stroke();
        }
      }
    };
  };
};

canvasSketch(sketch, settings);
