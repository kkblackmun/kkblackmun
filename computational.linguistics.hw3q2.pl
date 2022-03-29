% Just a sample transition. You can use it or delete it.

transition(1, S, 1, S) :-
    S \= eps,
    S \= '^'.

transition(1,V, 2,V):-
		voiced(V),
    nonsibilant(V).
transition(2, '^', 3, eps).
transition(3, s, 4, z).
transition(4, '#', 1, '#').

transition(1, N, 5, N):-
		nonsibilant(N),
		\+ voiced(N).
transition(5, '^', 6, eps).
transition(6, s, 7, s).
transition(7, '#', 1, '#').

transition(1, S, 8, S):-
		sibilant(S).
transition(8, '^', 9, eps).
transition(9, eps, 10, ih).
transition(10, s, 11, z).
transition(11, '#', 1, '#').

% ENTER ADDITIONAL TRANSITIONS HERE

% Adjust your initial and final states if needed.

initial(1).
final(1).

% Potentially useful features

voiced(aa).
voiced(ae).
voiced(ah).
voiced(ao).
voiced(aw).
voiced(ay).
voiced(b).
%voiced(d).
voiced(dh).
voiced(dx).
voiced(eh).
voiced(el).
voiced(em).
voiced(en).
voiced(er).
voiced(ey).
voiced(g).
voiced(jh).
voiced(l).
voiced(m).
voiced(n).
voiced(ng).
voiced(r).
voiced(v).
voiced(w).
voiced(wh).
voiced(y).
voiced(ih).
voiced(iy).
voiced(ow).
voiced(oy).
voiced(uh).
voiced(uw).
voiced(z).
voiced(zh).

sibilant(ch).
sibilant(s).
sibilant(sh).
sibilant(jh).
sibilant(z).
sibilant(zh).

% Once we have listed the sibilants,
% we can define what a nonsibilant is.
% Here we can assume that the alphabet
% is the symbols in the arpabet, ^ and #.
% In summary, the following says that a
% symbols S corresponds to a nonsibilant
% if S is not '^', S is not '#', S is not
% epsilon, and S is not a sibilant. To
% say that S is not a sibilant, here we
% are using the "not" operator \+ just to
% show how this can be done. Another easy
% way to define the nonsibilants would be
% just to list them all, instead of
% saying what they are not.
nonsibilant(S) :-
    S \= eps,
    S \= '^',
    S \= '#',
    \+ sibilant(S).