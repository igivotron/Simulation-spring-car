from main import v_t_sim, x_t_sim, tt_sim

def main(filename):
    """
    Ecrit un fichier avec les données pouvant être lu sur import_track.py
    :param filename: Nom du fichier à exporter
    :return: Ecrit le fichier avec chaque liste en colonne, chaques valeurs espacées d'un espace avec dans l'ordre t, x_t, v_t
    """
    l = ["t(s)"+9*" ","x(s)"+" "*9,"v(s)"+" "*9]
    for i in range(len(v_t_sim)):
        a = str(tt_sim[i])+" "
        b = str(v_t_sim[i])+" "
        c = str(x_t_sim[i])+" "

        l += [a, b, c,"\n"]
    with open(filename, "w") as f:
        f.writelines(l)

main("test.txt")