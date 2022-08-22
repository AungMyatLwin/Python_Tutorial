class Movie:
    def __init__(self,title,director,rating):
        self.title=title
        self.director=director
        self.__rating=rating
        
    @property
    def getrating(self): 
        return self.__rating

    @getrating.setter
    def setrating(self,newRating):
        self.__rating=newRating

