female(pam).
female(liz).
female(ann).

male(tom).
male(bob).

parent(pam,bob).
parent(tom,bob).
parent(tom,liz).
parent(bob,ann).

mother(X,Y):-
    female(X),
    parent(X,Y).

father(X,Y):-
    male(X),
    parent(X,Y).

grandfather(X,Y):-
    male(X),
    parent(X,Z),
    parent(Z,Y).