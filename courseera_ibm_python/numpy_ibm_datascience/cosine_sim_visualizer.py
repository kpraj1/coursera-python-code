import matplotlib.pyplot as plt
import numpy as np

# Two 2D vectors
v1 = np.array([1, 3])
v2 = np.array([-1, -3])

# Create plot
plt.figure()
plt.quiver(0, 0, v1[0], v1[1], angles='xy', scale_units='xy', scale=1, color='r', label='v1')
plt.quiver(0, 0, v2[0], v2[1], angles='xy', scale_units='xy', scale=1, color='b', label='v2')

# Setup plot limits and grid
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.grid(True)
plt.gca().set_aspect('equal')
plt.axhline(0, color='gray')
plt.axvline(0, color='gray')
plt.title("Cosine Similarity: Angle Between Vectors")
plt.legend()
plt.show()

# Compute cosine similarity
dot = np.dot(v1, v2)
norm_v1 = np.linalg.norm(v1)
norm_v2 = np.linalg.norm(v2)
cos_sim = dot / (norm_v1 * norm_v2)

print("Cosine Similarity:", cos_sim)