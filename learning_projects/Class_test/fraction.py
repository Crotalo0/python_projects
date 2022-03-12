import mcd


class Fraction:

    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num) + '/' + str(self.den)

    def simplify(self):
        common = mcd.mcd(self.num, self.den)
        self.num = self.num // common
        self.den = self.den // common

    def __add__(self, other_frac):
        new_num = (self.num * other_frac.den) + (self.den * other_frac.num)
        new_den = (self.den * other_frac.den)
        new_frac = Fraction(new_num, new_den)
        new_frac.simplify()
        return new_frac


myfrac = Fraction(126, 168)
myfrac.simplify()
print(myfrac)

f1 = Fraction(1, 2)
f2 = Fraction(1, 2)
f3 = f1 + f2
print(f3)
