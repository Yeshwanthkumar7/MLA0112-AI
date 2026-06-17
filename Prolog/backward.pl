parent(tom,bob).
parent(bob,ann).

grandparent(X,Y):-
    parent(X,Z),
    parent(Z,Y).