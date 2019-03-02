####################################################
## D-separation in Bayesian Networks
## Lingxue Zhu
## 2017/02/05
####################################################
##
## Description:
##
## Given a Bayesian Network, and several queries in the form of X Y | Z
## where X, Y are two query nodes, Z is a set of observed nodes,
## the algorithm checks whether X and Y are d-separated given Z.
##
## Reference: Koller and Friedman (2009), 
## Probabilistic Graphical Models: Principles and Techniques
##
####################################################

import sys
from BN import *

if __name__ == "__main__":
    
    # edges
    edges = [['A', 'E'],['B', 'F'],['B', 'G'],['C', 'G'],['D', 'I'],['E', 'J'],['F', 'K'],['G', 'K'],['G', 'L'],['H', 'L'],['H', 'M'],['I', 'H'],['I', 'M'],['K', 'E'],['L', 'N']]
    myBN = BN()

    for edge in edges:
        myBN.add_edge(edge)

    print("A d-separation query should have the format \"Node1 Node2 | Node3 Node4 ... NodeN\" ")
    print("For example, \"A H | \" returns True" )
    print("and  \"A H | J N\" returns False")

    numCorrect = 0
    numAnswered = 0

    while numCorrect < 50 or numCorrect/numAnswered < 0.8:

        print("Please enter a d-separation query: ")
        query = sys.stdin.readline().rstrip().split(" ")
        (start, end, observed) = (query[0], query[1], query[3:])

        print("Please enter either t if you think the nodes are d-separated. Otherwise please enter f")
        answer = sys.stdin.readline().rstrip()

        if answer == "True" or answer == "true" or answer == "t" or answer == "T":
            answer = True
        elif answer == "False" or answer == "false" or answer == "f"  or answer == "F":
            answer = False
        else:
            print("invalid answer")

        numAnswered += 1

        if answer == myBN.is_dsep(start, end, observed):
            numCorrect += 1
            print("That is correct.")
            print("Your Score: " + str(numCorrect) + "/" + str(numAnswered))    

        else:
            print("That is incorrect. The answer was "+str(myBN.is_dsep(start, end, observed)))
            print("Your Score: " + str(numCorrect) + "/" + str(numAnswered))

    print("Great Work! \nI think you have a good enough understanding of d-separation")

