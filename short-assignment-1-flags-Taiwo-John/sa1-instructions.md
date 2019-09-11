# SA 1 Instructions:

As a first attempt at using aluLib, let's draw a few simple, but important shapes. 
We will recreate the flags of three African countries: Benin, Guinea, and Niger.


 
## Academic Honor System:
Please make sure that you fully understand the Academic Honor System, and reach out if you need any clarifications. 
## What to turn in:
Make sure your git repository contains the following:
- A single python file which draws any of the three flags above. 
    - The file should contain 3 functions, called benin, guinea, and niger respectively
    - At the end of your file, you should draw one of the flags, but we should be able to draw any of the other three by 
    changing only that final, drawing line.
- A text file describing the following:
    - An acknowledgement of upholding the honor code, or information if any breach occured.
    - Any extra credits or additional features you attempted.
    - Any notes you want to bring to the attention of the grader. 
## Hints:
- Recall how the coordinate system works. The **TOP LEFT** point of the screen is at coordinates 0,0. Going to the right 
increases the x coordinate, going to the bottom increases the right coordinate.
- If you get stuck, draw the flag by hand. Think about what you've done, break it into small steps, 
and try to recreate it in code.
- Use variables! to get full marks, you'll need to use as few _magic numbers_ as possible. If you figure out how long a rectangle should be
make a variable for that.
## Extra credit ideas:
These are optional additional challenges to entice your curiosity, and crank up the difficulty of the assignment. 
None of these actually count for extra marks.
- **Correct color scheme**: You'll find that countries are very specific about what colors to use in their flag, can you 
match the original flags exactly?
- **Additional flags**: How would you draw the flag of Morocco? Uganda? The seychelles?
- **Animation**: You may have noticed from reading the description of the **_start_graphics(...)_** function: we can do 
animations. Right now, the function passed to start_graphics always draws the same thing: one of the flags. If you could
 find a way to change what the function does each time, you'd end up with an animation! You can try and make the flags wave, or alternate between multiple flags.

