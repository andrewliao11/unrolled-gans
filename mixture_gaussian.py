import numpy as np
import matplotlib.pyplot as plt
import seaborn
import ipdb


"""
    generate 2d gaussian around a circle
"""
class data_generator(object):
    def __init__(self):

        n = 8
        radius = 5
        std = 0.5
        delta_theta = 2*np.pi / n

        centers_x = []
        centers_y = []
        for i in range(n):
            centers_x.append(radius*np.cos(i*delta_theta))
            centers_y.append(radius*np.sin(i*delta_theta))

        centers_x = np.expand_dims(np.array(centers_x), 1)
        centers_y = np.expand_dims(np.array(centers_y), 1)

        self.size = 2
        self.n = n
        self.std = std
        self.centers = np.concatenate([centers_x, centers_y], 1)

    def sample(self, N):
        n = self.n
        std = self.std
        centers = self.centers

        ith_center = np.random.choice(n, N)
        sample_centers = centers[ith_center, :]
        sample_points = np.random.normal(loc=sample_centers, scale=std)
        return sample_points.astype('float32')


def plot(points):
    plt.scatter(points[:, 0], points[:, 1], c=[0.3 for i in range(1000)], alpha=0.5)
    plt.show()
    plt.close()

def main():
    gen = data_generator()
    sample_points = gen.sample(1000)
    plot(sample_points)

if __name__ == '__main__':
    main()
