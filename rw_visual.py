import matplotlib as plt

from randdom_walk import Randomwalk

#Make a random walk
While True:
    rw = Randomwalk()
    rw.fill_walk()

#Plot the points in the walk.
    plt.style.use('classic')
    fig, ax = plt.subplots()
    ax.scatter(rw.x_values, rw.y_values, s=15)
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
    break