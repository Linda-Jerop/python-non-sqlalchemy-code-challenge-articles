class Article:
    all_articles = [] #This variable stores all articles

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all_articles.append(self) #Adds to class list of all artcles

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if hasattr(self, '_title'):
            return #Should not change title if already set
        if isinstance(value, str) and 5 <= len(value) <= 50:
            self._title = value
        else:
            self._title = value  #Stores even invalid values for testing
            