def calc_distance(point1, point2):
    """Calcule la distance entre deux points"""
    # Extraction des coordonnées des points
    x1, y1, z1 = point1
    x2, y2, z2 = point2
    
    # Calcul de la distance entre les points
    diff_distance = (x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2
    
    return diff_distance ** 0.5  # Retourne la racine carrée du résultat

def my_app(func, arg1, arg2):
    """
    Applique la fonction 'func' à chaque paire d'arguments dans les listes 'arg1' et 'arg2', renvoyant le résultat.
    """
    res = [] # Liste pour stocker les résultats
    for i, j in zip(arg1, arg2):
        res.append(func(i, j))
    return res

# Définition des listes de points
points1 = [(1.0, 1.0, 1.0), (2.0, 2.0, 2.0), (3.0, 3.0, 3.0)]
points2 = [(4.0, 4.0, 4.0), (5.0, 5.0, 5.0), (6.0, 6.0, 6.0)]

# Calcul des distances entre chaque paire de points
distances = my_app(calc_distance, points1, points2)

print(calc_distance.__doc__, points1, "et" , points2) #renvoie la documentation de la fonction
print(distances)