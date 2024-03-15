import math
def racine2(a, b, c):
    """Calcul de la racine d'une équation du 2nd degré ax²+bx+c
    @params :
    - a : coef du terme de degré 2
    - b : coef du terme de degré 1
    - c : coef du terme de degré 0
    @returns :
    - 2 ou 1 ou None
    """
    try:
        a = float(a)
        b = float(b)
        c = float(c)
    except:
        print("a, b et c ne sont pas des nombres")
    Δ = b**2-4*a*c
    if Δ == 0:
        s = (-b)/(2*a)
        return s
    elif Δ > 0:
        sqrt_delta = math.sqrt(Δ)
        s1 = (-b-sqrt_delta)/(2*a)
        s2 = (-b+sqrt_delta)/(2*a)
        return [s1, s2]
    elif Δ < 0:
        return None

def racine(fonc, a, b, p=1e-6):
    """Calcul de la racine d' une fonction par dichotomie
    @params :
    - fonc : fonction python
    - a : borne plus petite que la racine
    - b : borne plus grande que la racine
    - p : précision (ou écart max entre la sol. et valeur théorique)
    @returns :
    - Une valeur approchée de la racine
    """
    T = b - a
    while T > p:
        x = (a + b)/2
        y = fonc(x)
        if y > 0:
            b = x
        else:
            a = x
        T = b - a
    return  a

def derive(fonc, a, h=1e-3, p=1e-6):
    """Calcul du nombre dérivé d’ un fonction en un point
    On divise par deux l’ intervalle à chaque itération
    @params :
    - fonc : fonction python
    - a : point dont on veut la valeur du dérivé
    - h : écart initial
    - p : précision voulue (ou écart entre deux valeurs de dérivé
    successives)
    @returns :
    - Une valeur approchée du nombre dérivé
    """
