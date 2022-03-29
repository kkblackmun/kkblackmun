transition(1, Sym, 1, Sym) :- Sym\= eps; Sym\=p; Sym\=k; Sym\=t; Sym\=s.
transition(1, s, 2, s).
transition(2, S, 1, S) :- S\= eps.

transition(3, aa1, 1, aa1).
transition(3, ae1, 1, ae1).
transition(3, ah1, 1, ah1).
transition(3, ay1, 1, ay1).
transition(3, ao1, 1, ao1).
transition(3, aw1, 1, aw1).
transition(3, eh1, 1, eh1).
transition(3, er1, 1, er1).
transition(3, ey1, 1, ey1).
transition(3, ih1, 1, ih1).
transition(3, iy1, 1, iy1).
transition(3, ow1, 1, ow1).
transition(3, oy1, 1, oy1).
transition(3, uh1, 1, uh1).
transition(3, uw1, 1, uw1).

transition(1, p, 3, p_h).
transition(1, k, 3, k_h).
transition(1, t, 3, t_h).

transition(1, p, 4, p).
transition(1, k, 4, k).
transition(1, t, 4, t).
transition(4, W, 1, W):- W\= eps; W\=aa1; W\= ae1; W\= ah1; W \=ay1; W\=ao1; W\=aw1; W\=eh1; W\=er1; W\=ey1; W\=ih1; W\=iy1; W\=ow1; W\=oy1; W\=uh1; W\=uw1.
initial(1).
final(1).
final(2).
final(4).