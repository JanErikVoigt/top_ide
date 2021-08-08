import matplotlib
matplotlib.use('TkAgg')
import pylab
import matplotlib.pyplot as plt
from matplotlib import rc

plt.clf()
plt.rc('text', usetex=True)
plt.rcParams["figure.figsize"] = (8, 5)
plt.rc('font', **{'family':'serif', 'serif':['Computer Modern Roman'], 'size': 16})
plt.axis("off")
plt.text(0.5, 0.5, "Maths $e = mc^2$")


plt.show()