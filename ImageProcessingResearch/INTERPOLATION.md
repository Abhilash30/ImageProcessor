Linear interpolation

P=(1−t)A+tB
t = 0 → A 
t = 0.25 → quarter way 
t = 0.5 → halfway 
t = 1 → B

Bilinear interpolation
Perform linear interpolation horizontally, then vertically.
A ───────── B
│                             │
│            P               │
│                             │
C ───────── D

p = Ptoprow + Pbottomrow 
P=(1−tx​)(1−ty​)A+tx​(1−ty​)B+(1−tx​)ty​C+tx​ty​D

Why bilinear produces smoother images
100 125 175 200 150 175 225 250 250 275 325 350 300 325 375 400
100 → 125 → 150 → ... → 200
smooth result
Nearest neighbour 
100 100 200 200
100 100 200 200
300 300 400 400
300 300 400 400

