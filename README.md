# pyclick
This is a library for generating human-like mouse movements.
The movements are based on the concept of bezier curve:
https://en.wikipedia.org/wiki/B%C3%A9zier_curve

### Simple Example:
```
from pyclick import HumanClicker

# initialize HumanClicker object
hc = HumanClicker()

# move the mouse to position (100,100) on the screen in approximately 2 seconds
hc.move((100,100),2)

# mouse click(left button)
hc.click()
```
You can also customize the mouse curve by passing a HumanCurve to HumanClicker. You can control:
- number of internal knots, to change the overall shape of the curve,
- distortion to simulate shivering,
- tween to simulate acceleration and speed of movement

