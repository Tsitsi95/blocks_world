 
"""Blocks World Problem"""

from search import * 							# This file imports utils.py so it should be in the same folder
import sys 								# System-specific parameters and functions

class Cubes(Problem) :
        """Subclass of search.Problem"""

        def __init__(self,state,goal_state):         			#Here we could pass an argument where we declare the number of Cubes
                """Sets initial state and goal."""
		state = sorted(state,key=lambda x: x[len(x)-1])		  #sorts according the base of the columns for the state
		state = tuple(tuple(x) for x in state)			  #makes it again tuple after the apply of sorted
		goal_state = sorted(goal_state,key=lambda x: x[len(x)-1]) #sorts like above in order for the problem to be deterministic
		goal_state = tuple(tuple(x) for x in goal_state)	  #makes it again a tuple
                super(Cubes, self).__init__(state,goal_state)
#_______________________________________________________________
	def actions(self,state) :
		if state :
			valid_actions = [(x,y) for x in range(1,len(state)+1) for y in range(0,len(state)+1) if x!=y]	#valid actions are being constructed 
			valid_actions.sort(key = lambda tuple : tuple[1])						#and sorted according the destination
		else :
			valid_actions = []
		return valid_actions
#_______________________________________________________________
	def result(self,state,action) :
		#Result will apply an action to the given state
		mutable_state = list(list(x) for x in state)				#creates a mutable state in order to use the state
		source_index = action[0]-1						#actions are created according length so have an offset that has to be substracted
		if mutable_state[source_index]:
			if action[1] != 0 :						#if destination is not the table
				target_index = action[1]-1
				target = mutable_state[source_index].pop(0)
				mutable_state[target_index].insert(0,target)
			else :								#if for the table
				target = mutable_state[source_index].pop(0)		#take the cube from source
				mutable_state.append(target)				#create a new column in the state
		i=0
		while i in range(len(mutable_state)) :					# a loop in order to clean the empty columns that stay as empty tuple
			if not mutable_state[i]:
				mutable_state.pop(i)
			else :
				i+=1
		mutable_state = sorted(mutable_state,key=lambda x: x[len(x)-1])		#again we use sort in order to become deterministic for the problem 
		new_state = tuple(tuple(x) for x in mutable_state)			#the new state list derives as a tuple of the mutable_state
		#print "The newly created state is ",new_state
		return new_state
#______________________________________________________
#The worst heuristic ever

	def h1(self,n) :
        	#A simple heuristic, not a good one, but it works
        	return 1

#______________________________________________________
#Wrong Place of a Cube in compare of the Cube under him
	"""In this heuristic must be justified that the dictionary of goal_state is created each time which in some way is time consuming 
        but this implementation was created so we dont mutate the files of Classes.The problem for example would be solved if we created the dictionary of goal_state as
        a member of the class and take it from there its time without creating.Using a dictionary we save a lot of time as the complexity stays in O(n) levels"""
	def h2(self,n):
		goal_state = self.goal                  #Take the goal state of the Problem
		state = n.state                         #Take the state to be examined
		state_dict = {}
		goal_dict = {}
		number_of_cubes = 0
		for i in range(0,len(goal_state)):                      #Checks all the columns of goal_state
			for j in range(0,len(goal_state[i])):           #Checks all the elements of its column
				if j+1 < len(goal_state[i]):		#If there is cube under the examining cube
					goal_dict[goal_state[i][j]] = goal_state[i][j+1]	#we add in dictionary at the specific cube the cube under him
				else:						#if there is not cube under the cube
					goal_dict[goal_state[i][j]] = 0		#table is represented with 0
		for i in range(0,len(state)):				#Same procedure for the state
			for j in range(0,len(state[i])):
				number_of_cubes += 1			#checking number of cubes that we will need for the calculation of the Wrong places
				if j+1 < len(state[i]):
					state_dict[state[i][j]] = state[i][j+1]
				else:
					state_dict[state[i][j]] = 0
		
		shared_items = set(goal_dict.items()) & set(state_dict.items())		#shared has the cubes that satisfy the criteria of the correct cube under
		return number_of_cubes-len(shared_items)				#number of wrong placed cubes

#______________________________________________________
#The height Difference between the Goal and State
	"""In this heuristic must be justified that the dictionary of goal_state is created each time which in some way is time consuming 
	but this implementation was created so we dont mutate the files of Classes.The problem for example would be solved if we created the dictionary of goal_state as
	a member of the class and take it from there its time without creating.Using a dictionary we save a lot of time as the complexity stays in O(n) levels"""
	def h3(self,n):
                goal_state = self.goal                  #Take the goal state of the Problem
                state = n.state                         #Take the state to be examined 
                false_counter = 0
		goal_dict = {}
		state_dict = {}
		for i in range(0,len(goal_state)):                      #Checks all the columns of goal_state
			for j in range(0,len(goal_state[i])):           #Checks all the elements of its column
				goal_dict[goal_state[i][j]] = (i,j)	#Same logic with the above heuristic but now for wach cube we store the position of it
		for i in range(0,len(state)):				#Same for state and goal_state
			for j in range(0,len(state[i])):
				state_dict[state[i][j]] = (i,j)
		for key in goal_dict:					#For each cube
			cube_position = goal_dict[key]			#find the position in goal_state
			state_position = state_dict[key] 		#find the position in state
			if cube_position[0] == state_position[0]:	#if the column is the same
				if cube_position[1] != state_position[1]:	#if the height is not the same
					false_counter += 2			
				else:						#if the height is the same
					false_counter += 0
			else:						#if the column is not the same
				false_counter += 1 
		print false_counter," ",state
                return false_counter

