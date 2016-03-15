
from Cubes import *
from Generator import *

print "\n\n---This programm is created to solve the ***Block World Problem***! So the user is called to give an input\n", \
	"   of the test state and the goal state the states must be given in programm from the screen or from a file \n", \
	"   that is created -user choice.The codec of the states are being referred in the theoretical part of the exercise \n", \
	"   but in a summary each case is represented as tuple of tuples with the second one to be the stacks of \n ", \
	" cubes starting from the top to the bottom. An important thing to notice is for the stacks that have only one cube\n", \
	" the documented form is somthing like ('B',) with a comma as tuples with one element are represented in python documentation---\n\n"

ask = input("Give me 1 if you want to run a random test or 2 for a user settled problem\n")

if ask == 1 :
	number = input("Give the magnitude of the Problem - Number of Cubes!\n")
	r = Generator(number)
	test_state = r.generate()
	goal_state = r.generate()
	print "The test state created from random generator is:\n",test_state,"\nThe goal_state created from random generator is:\n",goal_state
elif ask == 2:
	test_state = input("Give me the state you want to test in tuples of tuples:\n")
	goal_state = input("Give me the goal state you want to reach:\n")	
else:
	print >> sys.stderr, "Unknown behaviour for initializing Problem!\n"
	sys.exit(1)
p = Cubes(test_state,goal_state)

heuristic = input("Select the number (1-3) of the Heuristic that you want to use as these are represented in theoretical section or in Main File\n")

if heuristic == 1:
	s = astar_search(p,p.h1)	# return 1 Approach
elif heuristic == 2:
	s = astar_search(p,p.h2)	# Wrong Place base on the Cube under
elif heuristic == 3:
	s = astar_search(p,p.h3)	# Height and Column Difference
else:
	print >> sys.stderr, "Heuristic Function couldn't be found!"
  	sys.exit(1)
print "\n"
sol = s.solution() # The sequence of actions to go from the root to this node
path = s.path() # The nodes that form the path from the root to this node
print "Solution: \n+{0}+\n|Action\t|\t\t State \t\t\t|Path Cost |\n+{0}+".format('-'*42)
for i in range(len(path)) :
        state = path[i].state
        cost = path[i].path_cost
        action = " "
        if i > 0 : # The initial state has not an action that results to it
                action = sol[i-1]
        print "|{0}\t|{1} \t|{2} \t   |".format(action, state, cost)
print "+{0}+".format('-'*42)
