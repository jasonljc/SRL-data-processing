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
        if self.corefs is None:
            print('file not loaded')
            raise CoreNLPOutputNotLoadedException
        for coref in self.corefs.findall('coreference'):
            # A block of coreference
            for mention in coref.findall('mention'):
                # Find if any items matches the given arguments.
                if (sentence == int(mention[0].text) and 
                    start == int(mention[1].text) and
                    end == int(mention[2].text)):
                    break
            else:
                continue
            
            # Found coreference
            ret = []
            for mention in coref.findall('mention'):
                if not (sentence == int(mention[0].text) and 
                    start == int(mention[1].text) and
                    end == int(mention[2].text)):
                    ret.append(mention[0].text,
                               mention[0].text,
                               mention[0].text)
            return ret
                        
                        
                
            import pdb; pdb.set_trace()

def main():
    c = CorefResoluter()
    c.load_file('newsText1.xml')
    c.find_corefs(1,2,3)
    
if __name__ == '__main__':
	main()