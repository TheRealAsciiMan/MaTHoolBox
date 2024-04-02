from math import sqrt
from time import sleep

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
        s1 = (-b - sqrt(Δ)) / (2 * a)
        s2 = (-b + sqrt(Δ)) / (2 * a)
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


def integrale(a=0.0, b=5.0, fonc=lambda x: x ** 3, n=15):
    """Calcul l'intégrale d'une fonction entre le point a et le point b
    @params :
    - fonc : fonction python
    - a : 1ère borne de l'intervalle
    - b : 2ème borne de l'intervalle
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

def integrale_rec(a=0.0, b=5.0, fonc=lambda x: x ** 3, p=1e-6):
    """Calcul l'intégrale d'une fonction entre le point a et le point b de façon récursive
    @params :
    - fonc : fonction python
    - a : 1ère borne de l'intervalle
    - h : 2ème borne de l'intervalle
    - p : Précision voulue
    @returns :
    - Une valeur approchée de l'intégrale
    """
    if a > b: a, b = b, a
    if b-a < p :
        return (b-a)*fonc((b+a)/2)
    else:
        return integrale_rec(a, b-((b-a)/2), fonc, p) + integrale_rec(a+((b-a)/2), b, fonc, p)


print("""Bienvenue sur MaTHoolBox !
Un programme qui permet de résoudre certains problèmes de Mathématiques Appliquées
""")

def menu():
    print("""
Veuillez choisir l'outil à utiliser :
1. Résolution d'équation de degré 2
2. Résolution d'équation de degré n par dichotomie
3. Calcule la dérivée d'une fonction en un point
4. Calcule l'intégral d'une fonction d'un point a à un point b
5. Quitter
    
    """)

def degre2_menu():
    while True:
        print("\nRésolution d'équation de la forme ax²+bx+c=0, veuillez choisir les facteurs :")
        try:
            a = float(input("a : "))
            b = float(input("b : "))
            c = float(input("c : "))
            break
        except:
            print("Ce ne sont pas des nombres, veuillez réessayer !")
    print(f"Les solutions de l'équation {a}x²+{b}x+{c}=0 sont : {racine2(a, b, c)}")
    sleep(2)

def degren_menu():
    while True:
        print("\nRésolution d'équation ...=0, veuillez choisir une borne inférieure, une borne supérieure, une fonction et une précision (optionnel)")
        try:
            a = float(input("Borne inférieure : "))
            b = float(input("Borne supérieure : "))
            temp = input("La fonction (par exemple : 5+x**2) : ")
            c = eval(f"lambda x: {temp}")
            p = input("Précision (par défaut : 1e-6) : ")
            if p != "":
                p = float(p)
            rec = input("Utiliser la méthode récursive (conseillée) ? Oui/Non : ")
            if rec == '':
                rec = "o"
            else:
                rec = rec.lower()[0]
                if rec != 'o' and rec != 'n':
                    raise ValueError
            break
        except:
            print("Ce ne sont pas des nombres ou ce n'est pas une fonction, veuillez réessayer !")
    if p == "":
        if rec == "o":
            print(f"Une solution de l'équation {temp}=0 entre {a} et {b} est environ : {racine_rec(a, b, c)}")
        else:
            print(f"Une solution de l'équation {temp}=0 entre {a} et {b} est environ : {racine(a, b, c)}")
    else:
        if rec == "o":
            print(f"Une solution de l'équation {temp}=0 entre {a} et {b} est environ : {racine_rec(a, b, c, p)}")
        else:
            print(f"Une solution de l'équation {temp}=0 entre {a} et {b} est environ : {racine(a, b, c, p)}")
    sleep(2)


def derive_menu():
    while True:
        print("\nCalcul du nombre dérivé d’une fonction en un point")
        try:
            a = float(input("Coordonnée x du point : "))
            temp = input("La fonction (par exemple : 5+x**2) : ")
            c = eval(f"lambda x: {temp}")
            p = input("Précision (par défaut : 1e-6) : ")
            if p != "":
                p = float(p)
            break
        except:
            print("Ce ne sont pas des nombres ou ce n'est pas une fonction, veuillez réessayer !")
    if p == "":
        print(f"La dérivée de la fonction f(x)={temp} au point d'abscisse {a} est d'environ : {derive(a, c)}")
    else:
        print(f"La dérivée de la fonction f(x)={temp} au point d'abscisse {a} est d'environ : {derive(a, c, p=p)}")
    sleep(2)

def integrale_menu():
    while True:
        print("\nCalcul de l'intégrale d'une fonction dans un intervalle")
        try:
            a = float(input("Borne inférieure : "))
            b = float(input("Borne supérieure : "))
            temp = input("La fonction (par exemple : 5+x**2) : ")
            c = eval(f"lambda x: {temp}")
            rec = input("Utiliser la méthode récursive (conseillée) ? Oui/Non : ")
            if rec == '':
                rec = "o"
                p = input("Précision (par défaut : 1e-6) : ")
                if p != "":
                    p = float(p)
            else:
                rec = rec.lower()[0]
                if rec != 'o' and rec != 'n':
                    raise ValueError
                n = input("Nombre de division de la fonction en trapèzes (par défaut : 15) : ")
                if n != "":
                    n = int(n)
            break
        except:
            print("Ce ne sont pas des nombres ou ce n'est pas une fonction, veuillez réessayer !")
    if rec == "o":
        if p == '':
            print(f"L'intégral de la fonction {temp} entre {a} et {b} est de : {integrale_rec(a, b, c)}")
        else:
            print(f"L'intégral de la fonction {temp} entre {a} et {b} est de : {integrale_rec(a, b, c, p)}")
    else:
        if n == '':
            print(f"L'intégral de la fonction {temp} entre {a} et {b} est de : {integrale(a, b, c)}")
        else:
            print(f"L'intégral de la fonction {temp} entre {a} et {b} est de : {integrale(a, b, c, n)}")
    sleep(2)



if __name__ == "__main__":
    while True:
        menu()
        reponse = input()
        if reponse == "1":
            degre2_menu()
        elif reponse == "2":
            degren_menu()
        elif reponse == "3":
            derive_menu()
        elif reponse == "4":
            integrale_menu()
        elif reponse == "5":
            print("Au revoir !")
            sleep(2)
            break
        else:
            print("Erreur, veuillez choisir une option du menu")