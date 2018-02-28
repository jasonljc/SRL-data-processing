'''
Reform the tree structure in ClearNLP.

'''

import tree_util


class Config:
    '''
    Configuration of the inputs.
    
    Enables batch inputs from files here.
    '''
    pass

    
class TreeBuilder:
    def __init__(self):
        self.config = ''
        self.filename = '' # Current file
        self.paragraph_index = 0 # Current paragraph
    
    def set_config(self, config):
        pass    
    
    def get_lines(self):
        pass

    def get_paragraph(self):
        '''
        Generate SRL labels of a paragraph.
        The paragraph is located by self.filename and self.paragraph_index.
        '''
        if self.config == 'file':
            pass
        
            
                    
    def get_paragraph_from_file(self):
        with open(self.filename) as f:
            count, cnt = 0, 0
            for _, line in enumerate(f):
                cnt +=1
                if '\t' not in line:
                    count += 1
            return count
    
    def build_tree(self):
        '''
        Build tree from the current get_lines().
        
        Returns:
            Root node of the new tree. tree_util.Node
        '''
        # Create nodes and index.
        _dict = {}
        for line in self.get_paragraph():
            fields = line.split('/t')
            _label = {
                'id':int(fields[0]),
                'form':fields[1],
                'lemma':fields[2],
                'pos':int(fields[3]),
                'feats':fields[4],
                'head':int(fields[5]),
                'deprel':fields[6],
                'sheads':fields[7],
            }
            _dict[fields[0]] = tree_util.Node(_label)
        
        # Connect nodes.
        root = None
        for _, n in _dict:
            if n.label.head != 0:
                _dict[n.label.head].add_children([n])
            else:
                root = n
        
        return root
        
    
    def build_from_config(self):
        '''
        A interface for building all files and paragraphs from config.
        '''
        
        if self.config.source == 'file':
            for i in range(len(self.config.filenames)):
                pass