import random
import string

class Generator :

    def __init__(self, n):
        self.n = n		#Number of Cubes
        self.l = [str(x) for x in string.ascii_uppercase[:n]]	#Change it if you want number and not alphabet
    
    def generate(self):
        keep = self.l
	stack = []
	random.seed()		#take a seed for random
       	random.shuffle(keep)	#shuffle the keep
        while (len(keep) != 0) :		#until length
            s = random.randrange(1, self.n+1)	
            if (s > len(keep)):
                s = len(keep)
            stack += [keep[:s]]		
            keep = keep[s:]		
	rand_state = tuple(tuple(x) for x in stack)	#make a tuple of tuples
        return rand_state				#return rand state
