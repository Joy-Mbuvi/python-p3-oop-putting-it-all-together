#!/usr/bin/env python3

class Book:
    def __init__(self, title ="And Then There Were None",page_count= 272):
        self.title= title
        self.page_count= page_count

    @property
    def page_count (self):
        return self._page_count
    
    @page_count.setter
    def page_count (self,value):
        if type(value) in (int,):
            self._page_count = value

        else:print("page_count must be an integer")
    def get_title(self):
        return self._title
    def set_title(self, value):
        self._title = value
        

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

    title = property(get_title, set_title)