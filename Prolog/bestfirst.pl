edge(a,b,2).
edge(a,c,4).
edge(b,d,1).
edge(c,e,3).

best_first(X,Y):-
    edge(X,Y,_).