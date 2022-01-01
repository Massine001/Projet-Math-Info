import projetv2 as mp
import unittest

class TestMonProjet(unittest.TestCase):

            

#Le test de epsilon l'erreur = la somme des erreurs entre lae
#  sol[ti] - Euler[ti] div N (le vecteur)
    
    def test_resultats(self):
        y_euler, t_euler = mp.Euler(mp.y0, mp.n, mp.t0, mp.T) 
        y_sol = mp.sol(mp.t)
        erreur = 0
        for i in range(mp.n):
            erreur = erreur+y_euler[i]-y_sol[i]
        erreur = erreur/mp.n
        print(erreur)
        self.assertLessEqual(erreur,0.10)               #Erreur moyenne de max 10 %
    
        
    def domaine_de_definition(self):                    #Domaine de definition des fonctions
        if mp.choix == 1:
            self.assertGreaterEqual(mp.t,0)                  # Le temps est possitif
        if mp.choix == 2:
            self.assertGreaterEqual(mp.t,1)                  # La fonction Ln n'est pas definie a t = 0
        if mp.choix == 3:
            self.assertGreaterEqual(mp.t,1)         
        if mp.choix == 4:
            self.assertGreaterEqual(mp.t,0)
            self.assertGreater(mp.y0,0)  


if __name__ == "__main__":
    unittest.main()
