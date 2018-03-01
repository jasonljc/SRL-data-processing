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
        '''
        Generate each paragraph as a list of lines.
        '''
        with open(self.filename) as f:
            count = 0
            buf = []
            for _, line in enumerate(f):
                if '\t' not in line:
                    count += 1
                    yield buf
                    buf = []
                else:
                    buf.append(line)
            yield buf
    
    def build_tree(self, paragraph):
        '''
        Build tree from the current get_lines().
        
        Returns:
            Root node of the new tree. tree_util.Node
        '''
        # Create nodes and index.
        _dict = {}
        for line in paragraph:
            fields = line.split('\t')
            if len(fields) <2:
                continue
            _label = {
                'id':int(fields[0]),
                'form':fields[1],
                'lemma':fields[2],
                'pos':fields[3],
                'feats':fields[4],
                'head':int(fields[5]),
                'deprel':fields[6],
                'sheads':fields[7],
            }
            print 'adding %s'%fields[0]
            _dict[int(fields[0])] = tree_util.Node(label=_label, children=[])
        
        print len(_dict)
        
        # Connect nodes.
        root = None
        for _, n in _dict.items():
            if n.label['head'] != 0:
                _dict[n.label['head']].add_child(n)
            else:
                root = n
        
        return root
        
    
    # def build_from_config(self):
    #     '''
    #     A interface for building all files and paragraphs from config.
    #     '''
        
    #     if self.config.source == 'file':
    #         for i in range(len(self.config.filenames)):
    #             pass