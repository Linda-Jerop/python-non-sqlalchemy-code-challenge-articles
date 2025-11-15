class Author:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if hasattr(self, '_name'):
            return  
        if isinstance(value, str) and len(value) > 0:
            self._name = value
        else:
            self._name = value  #_name prevents infinite recursion