% the sentence rule
% the subject should have nominative case
% (denoted in the grammar as np_subj)
s --> np_subj_3s, vp_3s_trans.
s --> np_subj_3s, vp_3s_intrans.
s --> np_subj_other, vp_other_trans.
s --> np_subj_other, vp_other_intrans.

% noun phrase rules
np_subj_3s --> det, n_3s.
np_subj_3s --> pro_subj_3s.
np_subj_other --> det, n_other.
np_subj_other --> pro_subj_other.
np_obj --> det, n_3s.
np_obj --> det, n_other.
np_obj --> pro_obj.

% verb phrase with intransitive verb
vp_other_trans --> v_other_intrans.
vp_other_intrans --> v_other_trans, np_obj.
vp_3s_intrans --> v_3s_intrans.
vp_3s_trans --> v_3s_trans, np_obj.

% verb phrase with transitive verb
% the object should have accusative case
% (denoted in the grammar as np_obj)

% lexical rules
det --> [the].
n_3s --> [dog].
n_other --> [dogs].
pro_subj_3s --> [she].
pro_obj --> [her].
pro_obj --> [them].
pro_subj_other --> [they].
pro_subj_other --> [i].
pro_subj_other --> [we].
v_3s_trans --> [likes].
v_3s_intrans --> [arrived].
v_other_intrans --> [arrived].
v_other_trans --> [like].