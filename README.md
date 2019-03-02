# bayes-net
A python implemention for practicing d-separation. 

## D-separation
Given a Bayesian Network, and several queries in the form of `X Y | Z`
where `X`, `Y` are two query nodes and `Z` is a set of observed nodes,
`src/dsep.py` checks whether `X` and `Y` are d-separated given `Z` and prints `True` or `False`.

This mainly follows the `"Reachable"` procedure in 
> Koller and Friedman (2009), "Probabilistic Graphical Models: Principles and Techniques" (page 75)

To run the code, try
```
cd src
python dsep.py < ../tests/dsep/test1.in
```
The program assumes that we have the bayesian network depicted below
![Alt text](https://github.com/kai-pinckard/bayes-net/blob/master/Screenshot%20from%202019-03-02%2011-05-51.png?raw=true "Network")

```
