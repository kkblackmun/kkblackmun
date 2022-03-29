% sentence
% we need to enforce subject-verb agreement
% (person and number need to match for NP and VP),
% and we need the right case
s --> np(subj, P, N), vp(P, N).

% noun phrase
% ADD THE NP RULES
np(S, Person, Number) --> det, n(S, Person, Number).
np(S, Person, Number) --> pro(S, Person, Number).
np(S, P, plural) --> n(S, P, plural).
% verb phrase
% VP with intransitive verb
% the VP gets Person and Number from the V
vp(P, Number) --> v(intransitive, P, Number).
vp(P, Number) --> v(transitive, P, Number), np(obj, _, _).
% VP with transitive verb
% ADD THE TRANSITIVE VP RULE

% lexical rules

det --> [the].

% pronoun, subjective case, third person singular
pro(subj, third, singular) --> [she].
pro(obj, third, singular) --> [her].
pro(obj, third, plural) --> [them].
pro(subj, third, plural) --> [they].
pro(subj, first, singular) --> [i].
pro(subj, first, plural) --> [we].


% WRITE THE LEXICAL ENTRIES FOR:
% her, they, them, i, we

% here the underscore means that case can be
% anything. (dog is the same, whether it is
% subj or obj.)
n(_, third, singular) --> [dog].
n(_, third, plural) --> [dogs].

% WRITE THE LEXICAL ENTRY FOR dogs

% verb features:
% - transitive/instransitive
% - person: first, second, third
% - number: plural, singular

% the underscores here mean that Person can
% be anything, and Number can be anything
v(intransitive, _, _) --> [arrived].
v(transitive, third, singular) --> [likes].

% here we need to ensure person/number is
% third singular
% WRITE THE LEXICAL ENTRY FOR likes (transitive)

% person/number can be anything (first/second/third, singular/plural), except for
% third singular
v(transitive, first, _) --> [like].
v(transitive, second, _) --> [like].
v(transitive, third, plural) --> [like].