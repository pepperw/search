# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
Completed by Shiqin Wang 02/18/2016
"""

import util
import searchAgents
import copy


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def recursiveDFS(candidates,problem, temp, explored): 
     while candidates.isEmpty() == False:             
        current = candidates.pop()   
        explored.append(current[0])       
        if problem.isGoalState(current[0]):            
            temp.push(current)
            return (True,current)
        else:
            successors = problem.getSuccessors(current[0])
            for each in successors:
                if each[0] in explored:
                    pass
                else:
                    new = list(each)
                    new.insert(3,current[0])               
                    candidates.push(new)
            item1, item2 = recursiveDFS(candidates,problem, temp, explored)
            
            if item1 and item2[3]== current[0]: 
                current = tuple(current)
                temp.push(current)
                newCurrent = list(current)
                return (True,newCurrent)
            elif item1 and item2[3] != current[0]:
                return(True,item2)
     return (False, None)   

def depthFirstSearch(problem):
    start = problem.getStartState()
    candidates = util.Stack()
    rightPath = []
    temp = util.Stack()
    explored = []
    explored.append(start)
    if problem.isGoalState(start) == False:
        successors = problem.getSuccessors(start)
        
        if not successors:
            print"No solution"
        else:
            for each in successors:
                if each[0] in explored:
                    pass
                else:
                    new = list(each)
                    new.insert(3,start)
                    candidates.push(new)
    item1, item2 = recursiveDFS(candidates,problem,temp, explored)
    if item1:
        while temp.isEmpty()==False:
            item = temp.pop()
            rightPath.append(item[1])
    else:
        print 'no solutions'
    return rightPath
    
def recursiveBFS(candidates,problem, temp, explored):

  
    while candidates.isEmpty() == False:

        current = candidates.pop()

        if problem.isGoalState(current[0]):            
            temp.push(current)
            return (True,current)
        else:
            successors = problem.getSuccessors(current[0])
            for each in successors:
                if each[0] in explored:
                    pass
                else:
                    new = list(each)
                    new.insert(3,current[0])
                    explored.append(new[0])
                    candidates.push(new)
            item1, item2 = recursiveBFS(candidates,problem, temp, explored)
            
            if item1 and item2[3]== current[0]: 
                current = tuple(current)
                temp.push(current)
                newCurrent = list(current)
                return (True,newCurrent)
            elif item1 and item2[3] != current[0]:
                return(True,item2)
            

     
    return (False, None)   



def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
 
    start = problem.getStartState()
    candidates = util.Queue()
    rightPath = []
    temp = util.Stack()
    explored = []

    explored.append(start)
    if problem.isGoalState(start) == False:
        successors = problem.getSuccessors(start)
        if not successors:
            print"No solution"
        else:
            for each in successors:
                if each[0] in explored:
                    pass
                else:
                    new = list(each)
                    new.insert(3,start)
                    candidates.push(new)
                    explored.append(new[0])
    item1, item2 = recursiveBFS(candidates,problem,temp, explored)
    if item1:
        while temp.isEmpty()==False:
            item = temp.pop()
            rightPath.append(item[1])
    else:
        print 'no solutions'
    return rightPath
    

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    start = problem.getStartState()
    candidates = util.PriorityQueue()
    directionPath = util.PriorityQueue()
    path= []
    explored = []


    path.append([start])
    path.append(0)
    candidates.push(path,0)
    directionPath.push([],0)
    explored.append(start)


    while candidates.isEmpty() == False:
        current = candidates.pop()
        #print 'current',current
        #print 'explored',explored
        rightPath = directionPath.pop()
        
       
        if problem.isGoalState(current[-2][-1]):
            return rightPath
        else:
            temporary = copy.deepcopy(current)
          
            oldPath = copy.deepcopy(rightPath)
            successors = problem.getSuccessors(current[-2][-1])
            for each in successors:

                current[-2].append(each[0])
                rightPath.append(each[1])
                if each[0] in explored:
                    pass
                else:
                    cost = current[-1]+each[2]
                    current[-1]=cost
                    
                    candidates.push(current,cost)
                    directionPath.push(rightPath,cost)
                    if problem.isGoalState(each[0]) == False:
                        explored.append(each[0])
                current= copy.deepcopy(temporary)
                
                rightPath = copy.deepcopy(oldPath)


    return []
    

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0
"""
Heuristics take two arguments: a state in the search problem (the main argument), 
and the problem itself (for reference information). 
"""



def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    start = problem.getStartState()
    candidates = util.PriorityQueue()
    directionPath = util.PriorityQueue()
    path= []
    explored = []


    path.append([start])
    path.append(0)
    candidates.push(path,0)
    directionPath.push([],0)
   


    while candidates.isEmpty() == False:
        current = candidates.pop()
        
        #print 'current',current
        #print 'explored',explored
        rightPath = directionPath.pop()
        if current[0][-1] not in explored:

            explored.append(current[0][-1])
            
           
            if problem.isGoalState(current[-2][-1]):
                return rightPath
            else:
                temporary = copy.deepcopy(current)
              
                oldPath = copy.deepcopy(rightPath)
                successors = problem.getSuccessors(current[-2][-1])
                for each in successors:
                    #print'each',each

                    current[-2].append(each[0])
                    rightPath.append(each[1])
                    if each[0] in explored:
                        pass
                    else:
                        oldEstimate = heuristic(current[0][-2],problem)
                        estimate = heuristic(current[0][-1],problem)
                        cost = current[-1]+each[2]+ estimate-oldEstimate
                        current[-1]=cost
                        #print 'cost',cost
                        
                        candidates.push(current,cost)
                        directionPath.push(rightPath,cost)
                        
                    current= copy.deepcopy(temporary)
                    
                    rightPath = copy.deepcopy(oldPath)


    return []
    

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
