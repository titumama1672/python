"""16. Python program to implement different Linear algebra function using NUMPY

 Python program to implement different types of plots using Matplotlib : Line plot, Bar-
plots
 Scatter-plots
 Histograms"""


# Import the necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# Create some data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Line plot
plt.figure(figsize=(14, 7))
plt.subplot(221)
plt.plot(x, y)
plt.title('Line plot')

# Bar plot
plt.subplot(222)
counts, bins, patches = plt.hist(y, bins=10, orientation='vertical')
plt.title('Bar plot')

# Scatter plot
plt.subplot(223)
plt.scatter(x, y)
plt.title('Scatter plot')

# Histogram
plt.subplot(224)
plt.hist(y, bins=20)
plt.title('Histogram')

# Display the plots
plt.tight_layout()
plt.show()
