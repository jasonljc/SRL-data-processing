'''
Basic implementation of SRL processing tasks discussed on Feb 16.
'''

import tree_builder as tb
import coref_resolution as cr

def file_loader(filename, col=0):
    '''
    Read certain coloumn from text file.
    '''
    with open(filename) as fp:
        ret = fp.readlines()
        ret = [line.split()[col] for line in ret]
        return ret
    return None

base_forms = []
stative_verbs = []
actors = []


def main():
    
    base_forms = file_loader('params/states.txt')
    stative_verbs = file_loader('params/stativewords.txt')
    
    actors = file_loader('params/countr_map.txt')
    
    t = tb.TreeBuilder()
    c = cr.CorefResoluter()
    
    # process single file
    
    t.filename = 'data/newsText1.txt.srl'
    c.load_file('data/newsText1.xml')
    
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
        possesive_pronoun_node = stative_verb_node.find('deprel', 'poss')
        if not possesive_pronoun_node:
            print 'no possesive pronoun found'
            # find actor directly.
            
            
        else:
            # find actor through corenlp.
            pass
        
        # return actor, state, stative verb


if __name__ == '__main__':
	main()