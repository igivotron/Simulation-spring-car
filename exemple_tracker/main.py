import ex_simu
import import_track
import matplotlib.pyplot as plt


### Paramètres ###
v = 10 #m/s
x = 0
k = 0.5
m = 0.3
ligma = 0.00001 # erreur acceptée
dt = 0.01
filename = "donneesTracker.txt"


v_t_sim, x_t_sim, tt_sim = ex_simu.main(x, v, ligma, k, dt, m)
tt_track, x_t_track, v_t_track = import_track.main(filename)

if __name__ == '__main__':

    plt.title("Simulation du véhicule d'exemple tracker")
    plt.xlabel("Temps [s]")
    plt.ylabel("Position [m]")
    plt.grid()

    plt.plot(tt_sim,x_t_sim, label= "Postion simulation [m]")
    plt.plot(tt_sim,v_t_sim,label= "Vitesse simulation [m/s]")

    plt.plot(tt_track, x_t_track, label="Position avec Trackeur")
    plt.plot(tt_track, v_t_track, label="Vitesse avec Trackeur")

    plt.legend()
    plt.show()
