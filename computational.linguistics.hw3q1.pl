% Second-level FST from the two-level morphology example in
% Jurafsky & Martin

% Transitions out of state 0

transition(0, '#', 0, '#').
transition(0, '^', 0, eps).

% S below can be anything, except for '#', '^', z, s, x, eps.
% Pay close attention to how to interpret how J&M
% "other" and "#" in transitions.

% We use a variable S in the transition,
% and restrict its possible values by naming
% the symbols that S cannot be.

transition(0, S, 0, S) :-
    S \= z,
    S \= x,
    S \= s,
    S \= '#',
    S \= '^',
    S \= eps.

% These are straightforward transitions

transition(0, z, 1, z).
transition(0, s, 1, s).
transition(0, x, 1, x).

% Transitions out of state 1

transition(1, S, 0, S) :-
    % FILL IN LINES HERE THAT RESTRICT WHAT S CAN BE
    S \= z,
    S \= x,
    S \= s,
    S \= '#',
    S \= '^',
    S \= eps.

% ADD THE OTHER TRANSITIONS OUT OF STATE 1
transition(1, '#', 0, '#').
transition(1, z, 1, z).
transition(1, s, 1, s).
transition(1, x, 1, x).
transition(1, '^', 2, eps).

% Transitions out of state 2

transition(2, z, 1, z).
transition(2, x, 1, x).
transition(2, s, 5, s).
transition(2, S, 2, S):-
		S \= z,
    S \= x,
    S \= s,
    S \= '#',
    S \= '^',
    S \= eps.
transition(2, '#', 0, '#').
transition(2, eps, 3, e).

% transitions out of state 3

transition(3, s, 4, s).

% transitions out of state 4

transition(4, '#', 0, '#').

% transitions out of state 5

transition(5, S, 0, S):-
		S \= z,
    S \= x,
    S \= s,
    S \= '#',
    S \= '^',
    S \= eps.
transition(5, z, 1, z).
transition(5, s, 1, s).
transition(5, x, 1, x).
transition(5, '^', 2, eps).

initial(0).

% FILL IN FINAL STATES
final(0).
final(1).
final(2).