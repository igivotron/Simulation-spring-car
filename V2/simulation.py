import matplotlib.pyplot as plt


class Engin:
    def __init__(self):
        self.k = 865.6 * 4
        self.ratio = 2 / 5
        self.f_eng = 1
        self.f_air = 1
        self.dx_res = pow(10 / self.k, 1 / 2)
        self.n = 5
        self.m = 0.3

    def frot_engr(self, v):
        """
        Calcul les frottements des engrenages
        :param v: vitesse de l'engin, float
        :return: force de frottement, float
        """
        return -self.f_eng * v

    def frot_air(self, v):
        """
        Calcul les frottements externes
        :param v: vitesse de l'engin, float
        :return: force de frottement, float
        """
        return -self.f_air * v

    def relachement_ressort(self, r):
        """
        Calcul l'élongation du ressort
        :param r: relachement du ressort, float
        :return: nouvelle élongation du ressort, float
        """
        self.dx_res -= r

    def force_ressort(self):
        """
        Calcul la force du ressort en fonction de son élongation
        :return: force du ressort, float
        """
        return self.k * self.dx_res

    def ratio(self):
        """
        Calcul la réduction de la boite en fonction du ration et du nombre d'engrenage
        :return: réduction du moteur
        """
        return pow(self.ratio, self.n)

    def acceleration(self, v):
        """
        Calcul l'accélération de l'engin
        :param v: vitesse de l'engin
        :return: accélération de l'engin
        """
        return (((self.force_ressort() - self.frot_engr(v)) / self.ratio) - self.frot_air(v)) / self.m


class Simu:
    def __init__(self, engin, dt, sigma):
        self.dt = dt
        self.g = 9.81
        self.x = 0
        self.v = 0
        self.sigma = sigma
        self.loop = True
        self.engin = engin

        self.l_x = [0]
        self.l_v = [0]

    def test_loop(self):
        """
        Test si l'elongation du ressort est inferieur au seuil (sigma)
        :return: False si vitesse inferieur à sigma sinon True
        """
        if self.engin.dx_res < self.sigma:
            self.loop = False

    def calc1(self):
        """
        Calcul la vitesse et la position en fonction du temps
        Phase 1 : l'elongation est superieur à sigma, le moteur tourne
        Phase 2 : l'elongation est inférieur à sigma, le moteur ne tourne plus
        :return:
        """
        v = 0
        x = 0
        while self.loop:
            v += self.engin.acceleration(v) * self.dt
            x += v * self.dt
            self.l_v.append(v)
            self.l_x.append(x)
            self.engin.relachement_ressort(x)
            self.test_loop()

        while v > self.sigma:
            v += self.engin.frot_air(v) * self.dt
            x += v * self.dt
            self.l_v.append(v)
            self.l_x.append(x)

        return (self.l_x, self.l_v)

    def lst_x(self):
        """
        Recupere la liste des positions x
        :return:liste des positions en x
        """
        a = self.calc1()
        return a[0]

    def lst_v(self):
        """
        Recupere la liste des positions y
        :return: liste des positions y
        """
        a = self.calc1()
        return a[1]

    def export(self,filename):
        with open(filename,'w') as f:
            a = len(self.lst_x())
            print(a)
            for i in range(a):
                f.write(str(self.l_x[i]) + ";" + str(self.l_v[i])+"\n")




class Graph:
    def __init__(self, t, simu, n_x="Temps [ms]", n_y="Position"):
        self.title = t
        self.n_x = n_x
        self.n_y = n_y
        self.simu = simu

    def f_title(self):
        plt.title(self.title)

    def legend(self):
        plt.xlabel(self.n_x)
        plt.ylabel(self.n_y)
        plt.legend()

    def plot_x(self):
        plt.plot(self.simu.lst_x(), label="position en [m]")
        self.f_title()
        self.legend()
        plt.show()

    def plot_v(self):
        plt.plot(self.simu.lst_v(), label="vitesse en [m/s]")
        self.f_title()
        self.legend()
        plt.show()

    def plot_both(self):
        plt.plot(self.simu.lst_x(), label="position en [m]")
        plt.plot(self.simu.lst_v(), label="vitesse en [m/s]")
        self.f_title()
        self.legend()
        plt.show()

voiture = Engin()
simulation = Simu(voiture,0.001,0.0001)
simulation.export("data.csv")
graphique = Graph("Simulation", simulation)
graphique.plot_both()
