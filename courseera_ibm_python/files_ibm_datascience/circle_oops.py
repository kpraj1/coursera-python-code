import matplotlib.pyplot as plt

class Circle():
    def __init__(self, radius=3, color='blue'):
        self.radius = radius
        self.color = color

    def drawCircle(self, title="Circle"):
        fig = plt.figure()  # Create a new figure window
        ax = fig.add_subplot(1, 1, 1)
        ax.add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
        ax.set_aspect('equal')
        ax.set_xlim(-self.radius - 2, self.radius + 2)
        ax.set_ylim(-self.radius - 2, self.radius + 2)
        plt.title(title)
        #plt.grid(True)


class Rectangle(object):

    # Constructor
    def __init__(self, width=2, height=3, color='red'):
        self.height = height
        self.width = width
        self.color = color

    # Method
    def drawRectangle(self,title="Rectangle"):
        fig = plt.figure()  # Create a new figure window
        ax = fig.add_subplot(1, 1, 1)
        x = -self.width / 2
        y = -self.height / 2
        ax.add_patch(plt.Rectangle((x, y), self.width, self.height, fc=self.color))
        ax.set_aspect('equal')
        ax.set_xlim(-self.width, self.width)
        ax.set_ylim(-self.height, self.height)
        plt.title(title)


# Create and draw circles
c = Circle(5, 'red')
d = Circle(10, 'blue')
e = Rectangle(3,15)
c.drawCircle("Red Circle")
d.drawCircle("Blue Circle")
e.drawRectangle("rectangle shape")

# Block until all figure windows are manually closed
plt.show()
