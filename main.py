import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm


def fern():
    def function1(x, y):
        return (0., 0.16*y)
    def function2(x, y):
        return (0.85*x + 0.04*y, -.04*x + .85*y + 1.6)
    def function3(x, y):
        return (.2*x - .26 * y, .23*x + .22*y + 1.6)
    def function(x, y):
        return (-.15*x + .28*y, .26*x + .24*y + .44)
    functions = [function1, function2, function3, function]

    points = 100000
    x, y = 0, 0
    x_list = []
    y_list = []

    width, height = 300, 300
    fern_image = np.zeros((width, height))

    for i in range(points):
        function = np.random.choice(functions, p=[.01, .85, .07, .07])
        x, y = function(x, y)
        ix, iy = int(width / 2 + x * width / 10), int(y * height / 12)
        fern_image[ix, iy] = 1
    plt.imshow(fern_image[::-1,:], cmap=cm.Greens)
    plt.show()

def sierpinski(save = False):
    def randpoint():
        return np.random.choice([0,1,2])
    
    rng = np.random.default_rng(1234567)
    x, y = 1000 * rng.random(), 1000 * rng.random()

    width, height = 300, 300
    sier_image = np.zeros((width, height))

    plist = [(10, 10), (500, 990), (990, 10)]

    points = 1000000

    x_list = []
    y_list = []

    for i in range(points):
        point = plist[randpoint()]
        tx, ty = (x + point[0]) / 2, (y + point[1]) / 2
        if i != 0:
            x_list.append(tx)
            y_list.append(ty)
        x = tx
        y = ty
        
    plt.scatter(x_list, y_list, s=1)
    plt.show()

    if save:
        plt.savefig('sierpinski_mpl.png')

#fern()
sierpinski(True)
