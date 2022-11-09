__author__      = "Noreddine Kessa"
__copyright__   = "!"
__license__ = "MIT License"

from DataManagerGenerator import *
from variable import *
import sys
import os



if __name__ == "__main__":


    #process command line arguments for input configuration file
    file =  sys.argv[1]
    
    #check if file exists
    if not os.path.exists(file):
        print (f'Configuration file {file} not found')
        exit()
    
    
    #open and read from the file
    file1 = open(file, 'r')
    Lines = file1.readlines()
    
    #create lists to store the data parsed
    h_headers = []
    c_headers = []
    variables= []
    moduleName_=""
    

    
    #process line by line and build data structure for the code generator
    for line in Lines:
        #preprocess the lines
        line.replace("TRUE", "True")
        line.replace("FALSE", "False")
        print (f"Processing line:{line}")
        
        #look for line and headers
        words = line.split(",")
        print(f'length={words}')
        if len (words) >=2:
            temp =  words[1]
            temp = temp.replace("\"#", "#")
            temp = temp.replace("\"\"\"", "\"")
            temp = temp.replace("\"\"", "\"")
            if (words[0]=="$INCLUDE_H"):
                h_headers.append(f'{temp}\n')
            if (words[0]=="$INCLUDE_C"):
                c_headers.append(f"{temp}\n")
                #c_headers.append(f'{words[1]}\n')
                
            if (words[0]=="$NAME"):
                moduleName_=words[1]
                print(f"=========================================NAMEDETECTED={words[1]}n ")
                
                
        #look for variables data
        if len(words)>= 11:    
            if (words[0]=="$VARIABLE"):
                print(f"parsing {words}")
                name_=words[1]
                type_=words[2]
                prefix_=words[3]
                default_=words[4]
                
                notif_=False
                if (words[5]=="True"or words[5]=="TRUE"):
                    notif_=True
                
                callback_=words[6]
                
                CheckRange=False
                if (words[7]=="True" or words[7]=="TRUE" ):
                    CheckRange=True
                        
                minimum_=-4026531830
                if (words[8]!=""):
                    minimum_ = int(words[8])
                    
                maximum_=4026531839
                if (words[9]!=""):
                    maximum_ = int(words[9])
                
                notifyOnFresh=False
                if (words[10]=="True"or words[10]=="TRUE"):
                    notifyOnFresh=True
                    
                    
                var =  variable(name=name_, variableType=type_,prefix=prefix_,default=default_, notification=notif_,callbackFunction= callback_,checkRange=CheckRange,minimum=minimum_ , maximum=maximum_, onlyNotifyOnFreshValue=   notifyOnFresh )
                print(f'appending {var}\n')    
                variables.append(var)
                
    genrator = DataManagerGenerator(variableList=variables, moduleName=moduleName_, CFileHeadersList=c_headers, HFileHeaderList =h_headers)
    genrator.generateSourceFile()
    genrator.generateHeaderFile()
    
    
    print("#######################printing variables#######################\n")
    for var in variables:
        print(var)