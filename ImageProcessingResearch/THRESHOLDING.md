Thresholding is a method of converting a grayscale image into a binary image, using a threshold value
g(x,y) = 1 if f(x,y) > T 
and g(x,y) = 0 if f(x,y) ≤ T.


histogram - count how many pixels have each value.
## Otsu's Thresholding Method
Otsu's method finds a threshold **automatically**. It separates objects or similar intensity pixels into classes.

within-class variance → LOW 
between-class variance → HIGH

Class 0:
10  12  11  13  15
      ↑
very similar
					Class 0 mean ≠ Class 1 mean

Class 1:
220 225 218 230 222
        ↑
very similar

Mathematically:
C0​=[0,t] C1​=[t+1,255]

Probability of each class: 
w0(t) and w1​(t)

1000 pixels total

Class 0 = 600 pixels
Class 1 = 400 pixels

w0 = 0.6
w1 = 0.4

σB2​=w0​w1​(μ0​−μ1​) -> btwn class mean


## Otsu's Method Algorithm

1. Compute the normalized histogram of the input image. Denote the components of the histogram by pi.
2. Compute the cumulative sums P1(k).
3. Compute the cumulative mean m(k). 
4. Compute the global intensity mean mG.
5. Compute the between-class variance σB2(k).
6. Obtain the optimum threshold k' for which between-class variance is maximum by iterating over values of k. If more than one maximum exists, obtain k' by averaging over these values.
7. Segment the image using the threshold k' as g(x,y) = 1 if f(x,y)>k' and g(x,y) = 0 if f(x,y)≤k'.