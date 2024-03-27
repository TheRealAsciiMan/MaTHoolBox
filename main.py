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
        a, b, c = float(a), float(b), float(c)
    except:
        print("a, b et c ne sont pas des nombres")
    Δ = b ** 2 - 4 * a * c
    if Δ == 0:
        s = (-b) / (2 * a)
        return s
    elif Δ > 0:
        s1 = (-b - math.sqrt(Δ)) / (2 * a)
        s2 = (-b + math.sqrt(Δ)) / (2 * a)
        return [s1, s2]
    elif Δ < 0:
        return None


def racine(a, b, fonc=lambda x: x ** 3, p=1e-6):
    """Calcul de la racine d'une fonction par dichotomie
    @params :
    - fonc : fonction python
    - a : borne plus petite que la racine
    - b : borne plus grande que la racine
    - p : précision (ou écart max entre la solution et valeur théorique)
    @returns :
    - Une valeur approchée de la racine
    """
    T = b - a
    while T > p:
        x = (a + b) / 2
        y = fonc(x)
        if y > 0:
            b = x
        else:
            a = x
        T = b - a
    return a


def racine_rec(a, b, fonc=lambda x: x ** 3, p=1e-6):
    """Calcul de la racine d'une fonction par dichotomie (version récursive)
    @params :
    - fonc : fonction python
    - a : borne plus petite que la racine
    - b : borne plus grande que la racine
    - p : précision (ou écart max entre la solution et valeur théorique)
    @returns :
    - Une valeur approchée de la racine
    """
    T = b - a
    x = (a + b) / 2
    y = fonc(x)
    if T <= p:
        return a
    elif y > 0:
        return racine_rec(a, x, fonc, p)
    else:
        return racine_rec(x, b, fonc, p)


def derive(a, fonc=lambda x: x ** 3, h=1e-3, p=1e-6):
    """Calcul du nombre dérivé d’une fonction en un point
    On divise par deux l’intervalle à chaque itération
    @params :
    - fonc : fonction python
    - a : point dont on veut la valeur du dérivé
    - h : écart initial
    - p : précision voulue (ou écart entre deux valeurs de dérivé
    successives)
    @returns :
    - Une valeur approchée du nombre dérivé
    """
    deriv = (fonc(a + h) - fonc(a)) / h
    while (fonc(a)-fonc(a+h))/h > p:
        h /= 2
        deriv = (fonc(a + h) - fonc(a)) / h
    return deriv


def integrale(a=0, b=5, fonc=lambda x: x ** 3, n=15):
    """Calcul l'intégrale d'une fonction entre le point a et le point b
    @params :
    - fonc : fonction python
    - a : 1ère borne de l'intervalle
    - h : 2ème borne de l'intervalle
    - n : Nombre de trapèzes
    @returns :
    - Une valeur approchée de l'intégrale
    """
    surf = 0
    if a > b : a, b = b, a
    dist = (b - a) / n
    for i in range(n):
        g = a + dist * i
        d = g + dist
        surf += (dist * (fonc(d)+fonc(g) )) / 2
    return surf