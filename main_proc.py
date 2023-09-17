import math
import sys


class Sq_Roots:
    """Класс коэффициентов"""
    def __init__(self):
        self.A = 0.0
        self.B = 0.0
        self.C = 0.0
        #self.num_of_roots = 0
        self.root_list = set()

    def check_root(self, ind):
        try:
            coef = sys.argv[ind]
        except:
            print("Введите коэффициент {} :".format(ind) )
            try:
                coef = input()
            except (coef == 0 and ind == 1):
                print("Введите ненулевой коэффициент A {} :".format(ind))
        return float(coef)

    def get_roots(self):
        self.A = self.check_root(1)
        self.B = self.check_root(2)
        self.C = self.check_root(3)

    def calculation(self):

        D = self.B**2 - 4*self.A*self.C
        self.root_list.add( (-self.B + math.sqrt(D))/ (2*self.A) )
        self.root_list.add( (-self.B - math.sqrt(D))/ (2*self.A) )

    def print_ans(self):
        print("Корни: \n")
        for e in self.root_list:
            print(e, '\n')

def main():
    sr = Sq_Roots()
    sr.get_roots()
    sr.calculation()
    sr.print_ans()

if __name__ == "__main__":
    main()