# class Article:
#     def __init__(self, author, magazine, title):
#         self.author = author
#         self.magazine = magazine
#         self.title = title
        
# class Author:
#     def __init__(self, name):
#         self.name = name

#     def articles(self):
#         pass

#     def magazines(self):
#         pass

#     def add_article(self, magazine, title):
#         pass

#     def topic_areas(self):
#         pass

# class Magazine:
#     def __init__(self, name, category):
#         self.name = name
#         self.category = category

#     def articles(self):
#         pass

#     def contributors(self):
#         pass

#     def article_titles(self):
#         pass

#     def contributing_authors(self):
#         pass


class Article:
    # Think of this like a STORY in a magazine! 📖
    all = []  # A big toy box to keep ALL stories ever written
    
    def __init__(self, author, magazine, title):
        # When we write a new story, we need to know:
        self.author = author      # Who wrote it? (like "Mom")
        self.magazine = magazine  # Which magazine is it in? (like "Kids Today")  
        self.title = title        # What's the story called? (like "My Pet Dog")
        Article.all.append(self)  # Put this story in our big toy box

    @property
    def title(self):
        # This is like a name tag on the story
        return self._title
    
    @title.setter
    def title(self, value):
        # Once you write the story title, you can't change it!
        if hasattr(self, '_title'):
            return  # Story already has a title - can't change it!
        # Title must be a word between 5-50 letters long
        if isinstance(value, str) and 5 <= len(value) <= 50:
            self._title = value
        else:
            self._title = value  # Store even bad titles for testing

    @property
    def author(self):
        # Who wrote this story?
        return self._author
    
    @author.setter
    def author(self, value):
        # You can change who wrote the story (but they must be a real Author)
        if isinstance(value, Author):
            self._author = value

    @property
    def magazine(self):
        # Which magazine is this story in?
        return self._magazine
    
    @magazine.setter
    def magazine(self, value):
        # You can move the story to a different magazine
        if isinstance(value, Magazine):
            self._magazine = value

class Author:
    # Think of this like a PERSON who writes stories! ✍️
    def __init__(self, name):
        # When a new writer is born, they get a name
        self.name = name

    @property
    def name(self):
        # This is like asking "What's your name?"
        return self._name
    
    @name.setter
    def name(self, value):
        # Once you're born with a name, you can't change it!
        if hasattr(self, '_name'):
            return  # Already have a name - can't change it!
        # Name must be at least 1 letter long
        if isinstance(value, str) and len(value) > 0:
            self._name = value
        else:
            self._name = value  # Store even bad names for testing

    def articles(self):
        # Find all the stories I wrote! 🔍
        # Look through ALL stories and find MINE
        my_articles = []
        for article in Article.all:  # Look at every single story
            if article.author == self:  # Is this story mine?
                my_articles.append(article)  # Yes! Add it to my list
        return my_articles

    def magazines(self):
        # Find all the magazines I wrote stories for! 📚
        # First, get all my stories, then see what magazines they're in
        all_my_magazines = []
        for article in self.articles():  # Look at each of my stories
            all_my_magazines.append(article.magazine)  # Add the magazine
        
        # Remove duplicates (same magazine appears multiple times)
        unique_magazines = []
        for magazine in all_my_magazines:
            if magazine not in unique_magazines:  # Haven't seen this one yet?
                unique_magazines.append(magazine)  # Add it!
        return unique_magazines

    def add_article(self, magazine, title):
        # Write a brand new story! ✨
        # This creates a new story and says I wrote it
        return Article(self, magazine, title)

    def topic_areas(self):
        # What kinds of topics do I write about? 🤔
        if not self.articles():
            return None  # I haven't written any stories yet!
        
        # Look at all my magazines and see what categories they are
        all_categories = []
        for magazine in self.magazines():
            all_categories.append(magazine.category)
        
        # Remove duplicates (same category appears multiple times)
        unique_categories = []
        for category in all_categories:
            if category not in unique_categories:  # Haven't seen this topic yet?
                unique_categories.append(category)  # Add it!
        return unique_categories

class Magazine:
    # Think of this like a BOOK with lots of stories! 📖
    all = []  # A big bookshelf to keep ALL magazines ever made
    
    def __init__(self, name, category):
        # When we make a new magazine, we give it:
        self.name = name          # A name (like "Kids Today")
        self.category = category  # What type it is (like "Fun" or "Science")
        Magazine.all.append(self) # Put this magazine on our big bookshelf

    @property
    def name(self):
        # What is this magazine called?
        return self._name
    
    @name.setter
    def name(self, value):
        # Magazine names CAN change! (unlike people's names)
        # But the name must be between 2-16 letters long
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value
        # If bad name, keep the old good name

    @property
    def category(self):
        # What type of magazine is this? (Sports, Science, etc.)
        return self._category
    
    @category.setter
    def category(self, value):
        # Category CAN change too! But must be at least 1 letter
        if isinstance(value, str) and len(value) > 0:
            self._category = value
        # If bad category, keep the old good one

    def articles(self):
        # Find all the stories that are IN this magazine! 📝
        my_articles = []
        for article in Article.all:  # Look at every single story
            if article.magazine == self:  # Is this story in MY magazine?
                my_articles.append(article)  # Yes! Add it to my list
        return my_articles

    def contributors(self):
        # Find all the writers who wrote stories for me! ✍️
        all_authors = []
        for article in self.articles():  # Look at each story in my magazine
            all_authors.append(article.author)  # Add the writer
        
        # Remove duplicates (same writer might have multiple stories)
        unique_authors = []
        for author in all_authors:
            if author not in unique_authors:  # Haven't seen this writer yet?
                unique_authors.append(author)  # Add them!
        return unique_authors

    def article_titles(self):
        # List all the story titles in my magazine! 📋
        articles = self.articles()
        if not articles:
            return None  # I have no stories yet - return None!
        
        # Make a list of all my story titles
        titles = []
        for article in articles:
            titles.append(article.title)
        return titles

    def contributing_authors(self):
        # Find writers who wrote MORE than 2 stories for me! 🌟
        # First, count how many stories each writer wrote
        author_counts = {}  # Like a scoreboard
        for article in self.articles():
            author = article.author
            if author in author_counts:
                author_counts[author] = author_counts[author] + 1  # Add 1 point
            else:
                author_counts[author] = 1  # First story = 1 point
        
        # Find writers with MORE than 2 stories (3 or more!)
        contributing = []
        for author in author_counts:
            if author_counts[author] > 2:  # More than 2 stories?
                contributing.append(author)  # They're a star contributor!
        
        if len(contributing) == 0:
            return None  # No star contributors yet
        return contributing

    @classmethod
    def top_publisher(cls):
        # Which magazine has the MOST stories? 🏆
        if not Article.all:
            return None  # No stories exist in the whole world yet!
        
        # Count how many stories each magazine has
        magazine_counts = {}  # Like a scoreboard for magazines
        for article in Article.all:
            magazine = article.magazine
            if magazine in magazine_counts:
                magazine_counts[magazine] = magazine_counts[magazine] + 1  # Add 1 point
            else:
                magazine_counts[magazine] = 1  # First story = 1 point
        
        # Find the magazine with the highest score
        top_magazine = None
        highest_count = 0
        for magazine in magazine_counts:
            if magazine_counts[magazine] > highest_count:
                highest_count = magazine_counts[magazine]  # New high score!
                top_magazine = magazine  # New champion!
        
        return top_magazine  # Return the winner! 🏆

class Author:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if hasattr(self, '_name'):
            return  # Can't change your name once you're born!
        if isinstance(value, str) and len(value) > 0:
            self._name = value
        else:
            self._name = value

    def articles(self):
        # Find all MY stories
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        # Find all magazines I wrote for (no duplicates!)
        return list(set([article.magazine for article in self.articles()]))

    def add_article(self, magazine, title):
        # Write a new story!
        return Article(self, magazine, title)

    def topic_areas(self):
        # What topics do I write about?
        if not self.articles():
            return None  # I haven't written anything yet!
        return list(set([magazine.category for magazine in self.magazines()]))

class Magazine:
    all = []  # A big shelf to keep ALL magazines
    
    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.all.append(self)  # Put this magazine on the big shelf

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        # Magazine names CAN change (unlike author names!)
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value
        # If bad name, keep the old one!

    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, value):
        # Categories CAN change too!
        if isinstance(value, str) and len(value) > 0:
            self._category = value
        # If bad category, keep the old one!

    def articles(self):
        # Find all stories in MY magazine
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        # Find all writers who wrote for me (no duplicates!)
        return list(set([article.author for article in self.articles()]))

    def article_titles(self):
        # List all my story titles
        articles = self.articles()
        if not articles:
            return None  # I have no stories yet!
        return [article.title for article in articles]

    def contributing_authors(self):
        # Find writers who wrote MORE than 2 stories for me
        author_counts = {}
        for article in self.articles():
            author = article.author
            author_counts[author] = author_counts.get(author, 0) + 1
        
        # Only authors with MORE than 2 articles
        contributing = [author for author, count in author_counts.items() if count > 2]
        return contributing if contributing else None

    @classmethod
    def top_publisher(cls):
        # Which magazine has the MOST stories?
        if not Article.all:
            return None  # No stories exist yet!
        
        magazine_counts = {}
        for article in Article.all:
            magazine = article.magazine
            magazine_counts[magazine] = magazine_counts.get(magazine, 0) + 1
        
        return max(magazine_counts, key=magazine_counts.get) if magazine_counts else None