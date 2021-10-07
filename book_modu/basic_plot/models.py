import matplotlib.pyplot as plt


class BasicPlot(object):

    def plot_show(self):
        plt.title("Plotting")
        plt.plot([10, 20, 30, 40], color='r', ls='--', label='asc')
        plt.plot([40, 30, 20, 10], color='g', ls=':', label='desc')
        plt.legend()
        plt.show()


    def plot_two_list_show(self):
        plt.plot([1, 2, 3, 4], [12, 43, 25, 15])
        plt.show()



    def scatter(self):
        plt.title('Marker')
        plt.plot([10, 20, 30, 40], 'r.', label='Circle')
        plt.plot([40, 30, 20, 10], 'g^', label='Triangle_up')
        plt.legend
        plt.show()