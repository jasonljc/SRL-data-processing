import xml.etree.ElementTree as ET

class CoreNLPOutputNotLoadedException(BaseException):
    pass

class CorefResoluter(object):
    def __init__(self):
        self.corefs = None
    
    def load_file(self, filename):
        tree = ET.parse(filename)
        root = tree.getroot()
        self.corefs = root[0].find('coreference')
    
    def find_corefs(self, sentence, start, end):
        # Find coreferences if file is loaded
        if not self.corefs:
            print('file not loaded')
            raise CoreNLPOutputNotLoadedException
            
        for coref in self.corefs.findall('coreference'):
            # A block of coreference
            for mention in coref.findall('mentions'):
                # Find if any items matches the given arguments.
                pass

def main():
    c = CorefResoluter()
    c.load_file('newsText1.xml')
    c.find_corefs(1,2,3)
    
if __name__ == '__main__':
	main()