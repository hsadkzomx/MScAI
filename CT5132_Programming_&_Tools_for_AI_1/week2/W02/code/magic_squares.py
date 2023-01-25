           
import itertools
for p in itertools.permutations(list(range(1, 10))):
    if (p[0]+p[1]+p[2] == p[3]+p[4]+p[5] == p[6]+p[7]+p[8] ==
        p[0]+p[3]+p[6] == p[1]+p[4]+p[7] == p[2]+p[5]+p[8]):

        print(p[:3])
        print(p[3:6])
        print(p[6:])
        print("")
