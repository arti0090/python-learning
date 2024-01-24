from sys import path

path.append('..\\packages')

import extra.iota
print(extra.iota.funI())

import extra.good.best.sigma
from extra.good.best.tau import funT

print(extra.good.best.sigma.funS())
print(funT())