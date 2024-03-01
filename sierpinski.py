import matplotlib.pyplot as plt
import numpy as np

def midpoint(point1, point2):
    return ((point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2)

def sierpinski_triangle(ax, order, p1, p2, p3):
    if order == 0:
        
        ax.fill([p1[0], p2[0], p3[0]], [p1[1], p2[1], p3[1]], 'k')
    else:
        mp1 = midpoint(p1, p2)
        mp2 = midpoint(p2, p3)
        mp3 = midpoint(p3, p1)

        sierpinski_triangle(ax, order-1, p1, mp1, mp3)
        sierpinski_triangle(ax, order-1, mp1, p2, mp2)
        sierpinski_triangle(ax, order-1, mp3, mp2, p3)


triangle_size = 1
triangle_height = triangle_size * np.sqrt(3) / 2
p1 = (0, 0)
p2 = (triangle_size, 0)
p3 = (triangle_size / 2, triangle_height)


order = 6


fig, ax = plt.subplots()
sierpinski_triangle(ax, order, p1, p2, p3)


plt.title('Triangle de Sierpinski')
plt.axis('equal')
plt.axis('off')

plt.show()