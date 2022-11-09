def main(filename):
    """
    Retourne 3 listes avec le temps, la vitesse et la position
    :param filename: Un document texte contenant 3 listes séparées en colonne de même longueur avec dans l'ordre le temps, la position et la vitesse
    :return: tt une liste des temps, x_t une liste des positions en fonction du temps et v_t une liste des vitesse en fonction du temps.
    """
    tt = []
    v_t = []
    x_t = []
    with open(filename,"r") as f:
        for line in f:
            a = f.read()
            l1 = a.split()
        for i in range(len(l1)//3):
            t = l1[0+3*i]
            t = t.replace(",", ".")
            v = l1[1+3*i]
            v = v.replace(",", ".")
            x = l1[2+3*i]
            x = x.replace(",", ".")
            tt.append(float(t))
            v_t.append(float(v))
            x_t.append(float(x))

    return tt,x_t,v_t


main("donneesTracker.txt")