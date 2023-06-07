__author__      = "Noreddine Kessa"
__copyright__   = "!"
__license__ = "MIT License"


from datetime import date

class EnumItem:

    def __init__(self, name, value, comment ):
        self.name = name
        self.value = value
        self.comment = comment
    
        
    def __str__(self):
        comment =""
        if self.comment !="":
            comment=f"comment={self.comment},"
        st = f"name={self.name}, value={self.value},{comment}\n"
        return st  

class Enumeration:

    def __init__(self, name, comment):
        self.name = name
        self.comment = comment
        self.items = []
        
        
    def addItem(self, item):
        self.items.append(item)
    
        
    def __str__(self):
        comment=""
        if self.comment !="":
            comment=f"comment={self.comment},"
        st = f"name={self.name},{comment}\n"
        for item in  self.items:
            st+=f"    {item}"
        return st    
        
    def get_definition( self ):
        
        #no need to return anything if no items are provided
        if (len(self.items)<=0): 
            return f"/*enum {self.name} has no items.\n*/"
        #see if have any comment
        comment = ""
        if self.comment != "": 
            comment = f"/*{self.comment}*/"
        
        #start generating definition
        st = f"typedef enum {comment}\n"
        st+= "{\n"
        for item in self.items:
            item_comment=""
            if item.comment != "":
                item_comment = f"    /*{item.comment}*/"
                
            item_value=""
            if item.value != "":
                item_value=f" = {item.value}"
            
            st+=f"    {item.name}{item_value},{item_comment}\n"
                
        st+= f"\n}}{self.name};\n"
        return st
        
            

   
