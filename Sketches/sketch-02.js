/*
  understanding context transformations
  https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D#transformations
  defining the shapes with just numerical value places them 
  at the x, y, width, height values; transformations move 
  the context object, just like it were a piece of paper, 
  and then it creates the shape
*/

const canvasSketch = require('canvas-sketch');

const settings = {
  dimensions: [1080, 1080],
  pixelsPerInch: 300
};

const sketch = () => {
  return ({ context, width, height }) => {
    context.fillStyle = 'white';
    context.fillRect(0, 0, width, height);
    
    context.fillStyle = 'black';

    const x = width * 0.5;
    const y = height * 0.5;
    const w = width * 0.3;
    const h = height * 0.3;

    // save the state before this
    context.save();
    context.translate(x ,y);
    context.rotate(0.3);

    context.beginPath();
    context.rect(-w*0.5, -h*0.5, w, h);
    context.fill();

    // restore the saved state
    context.restore();

  };
};

canvasSketch(sketch, settings);
