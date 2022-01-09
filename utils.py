import matplotlib.pyplot as plt

def plotout(inputlist, ylabel="numberbetween", xlabel="value", title="run"):
    plt.hist(inputlist)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.title(title)
    plt.show()
