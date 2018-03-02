'''
Basic implementation of SRL processing tasks discussed on Feb 16.
'''

import tree_builder as tb
t = tb.TreeBuilder()

base_forms = []
stative_verbs = []
possesive_pronouns = []


# process single file

t.filename = 'newsText1.txt.srl'

for p in t.get_paragraph_from_file():
    # process single paragraph
    
    r = t.build_tree(p)
    state_node = r.find_list('form', base_forms)
    if not state_node:
        print 'no state found'
        continue
    stative_verb_node = state_node.find_list('form', stative_verbs)
    if not stative_verb_node:
        print 'no stative verb found'
        continue
    possesive_pronoun_node = stative_verb_node.find_list('form', possesive_pronouns)
    if not possesive_pronouns:
        print 'no possesive pronoun found'
        # find actor directly.
        
        
    else:
        # find actor through corenlp.
        pass
    
    # return actor, state, stative verb
    