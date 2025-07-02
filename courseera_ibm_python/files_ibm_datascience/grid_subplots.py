# import matplotlib.pyplot as plt
#
# # Create a figure
# fig = plt.figure(figsize=(8, 8))  # Optional: make it bigger
#
# # ---- Top-left: Red Circle ----
# ax1 = fig.add_subplot(2, 2, 1)
# ax1.add_patch(plt.Circle((0, 0), radius=2, fc='red'))
# ax1.set_xlim(-3, 3)
# ax1.set_ylim(-3, 3)
# ax1.set_aspect('equal')
# ax1.set_title("Red Circle")
#
# # ---- Top-right: Blue Rectangle ----
# ax2 = fig.add_subplot(2, 2, 2)
# ax2.add_patch(plt.Rectangle((-1, -1), 2, 3, fc='blue'))
# ax2.set_xlim(-3, 3)
# ax2.set_ylim(-3, 3)
# ax2.set_aspect('equal')
# ax2.set_title("Blue Rectangle")
#
# # ---- Bottom-left: Blue Rectangle ----
# ax3 = fig.add_subplot(2, 2, 3)
# ax3.add_patch(plt.Rectangle((-2, -1.5), 4, 2, fc='blue'))
# ax3.set_xlim(-3, 3)
# ax3.set_ylim(-3, 3)
# ax3.set_aspect('equal')
# ax3.set_title("Blue Rectangle")
#
# # ---- Bottom-right: Red Circle ----
# ax4 = fig.add_subplot(2, 2, 4)
# ax4.add_patch(plt.Circle((0, 0), radius=2.5, fc='red'))
# ax4.set_xlim(-3, 3)
# ax4.set_ylim(-3, 3)
# ax4.set_aspect('equal')
# ax4.set_title("Red Circle")
#
# # Adjust layout
# plt.tight_layout()
# plt.show()

import matplotlib.pyplot as plt

class Circle():
    def __init__(self, radius=3, color='blue'):
        self.radius = radius
        self.color = color

    def draw(self, ax, title="Circle"):
        ax.add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
        ax.set_xlim(-self.radius - 1, self.radius + 1)
        ax.set_ylim(-self.radius - 1, self.radius + 1)
        ax.set_aspect('equal')
        ax.set_title(title)

class Rectangle():
    def __init__(self, width=2, height=3, color='red'):
        self.width = width
        self.height = height
        self.color = color

    def draw(self, ax, title="Rectangle"):
        ax.add_patch(plt.Rectangle((-self.width/2, -self.height/2), self.width, self.height, fc=self.color))
        ax.set_xlim(-self.width - 1, self.width + 1)
        ax.set_ylim(-self.height - 1, self.height + 1)
        ax.set_aspect('equal')
        ax.set_title(title)

# Create figure and subplots
fig, axs = plt.subplots(2, 2, figsize=(8, 8))

# Create shape objects
circle1 = Circle(1, 'red')
rect1 = Rectangle(2, 3, 'blue')
rect2 = Rectangle(3, 9, 'blue')
circle2 = Circle(4, 'red')

# Draw them in their respective subplot positions
circle1.draw(axs[0, 0], "Red Circle ")
rect1.draw(axs[0, 1], "Blue Rectangle ")
rect2.draw(axs[1, 0], "Blue Rectangle ")
circle2.draw(axs[1, 1], "Red Circle ")

# Improve layout and show
plt.tight_layout()
plt.show()
