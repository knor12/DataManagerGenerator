#variable properties are defined in variable definition section below#

from datetime import date


class variable:

    def __init__(self, name, variableType="uint32_t", prefix="ui32",  default=0, notification=False, onlyNotifyOnFreshValue = True, callbackFunction="" , checkRange= False, minimum=-4026531830 , maximum=4026531839):
        self.name = prefix+"_"+name
        self.variableType = variableType
        self.default = default
        self.notification=notification
        self.onlyNotifyOnFreshValue=onlyNotifyOnFreshValue
        self.callbackFunction=callbackFunction
        self.checkRange=checkRange
        self.minimum=minimum
        self.maximum=maximum
        self.accessors_prefix=""
        
    def get_header_definition( self ):
        name = self.name
        notification = self.notification
        variableType = self.variableType
        accessors_prefix = self.accessors_prefix
        default = self.default
        callback_type= f'{name}_callback_t'
        accessors_prefix = self.accessors_prefix
        
        out = ""
        if (notification):
            out += f"/*provide access to {name}, define setter and getter and notification*/\n"
            #out += f"/*define variable*/\n"
            #out += f"extern {variableType} {name};\n"
            out += f"/*setter*/\n"
            out += f"void {accessors_prefix}_set_{name}({variableType} x);\n"
            out += f"/*getter*/\n"
            out += f"{variableType} {accessors_prefix}_get_{name}();\n"
            out += f"/*define call back function type*/\n"
            out += f"typedef  void (* {callback_type})({variableType});\n"
            #out +="/*callback function pointer*/\n"
            #out += f"extern {callback_type} {name}_callback;\n" 
            out += f"/*setter of call back function*/\n"
            out += f"void {accessors_prefix}_set_{name}_callback({callback_type} i);\n"
            out += "\n\n"
        
        
        else: #not notification
            out += f"/*provide access to {name}, define setter and getter*/\n"
            #define
            out += f"extern {variableType} {name};\n"
            #setter
            out += f"#define {accessors_prefix}_set_{name}(x) {{ {name} = x ; }}\n"
            #getter
            out += f"#define {accessors_prefix}_get_{name}()({name})\n"
            out += "\n\n"
            
        return out 
            
            
    def get_source_implementation( self ):
    
        name = self.name
        notification = self.notification
        variableType = self.variableType
        accessors_prefix = self.accessors_prefix
        default = self.default
        callbackFunction=""
        onlyNotifyOnFreshValue=""
        rangecheck=""
        out = ""
        if self.callbackFunction !="":
            callbackFunction= f'{self.callbackFunction}(x);'
            out+='/*define function as external to be called on event*/\n'
            out += f"extern void {self.callbackFunction}({variableType});\n"
        
        if self.checkRange:
            rangecheck+='/*check if the assigned value within range*/\n    '
            rangecheck+=f'if ((x < {self.minimum})|| (x > {self.maximum})){{return; }}'
        if self.onlyNotifyOnFreshValue:
            onlyNotifyOnFreshValue=f'/*check if we have a fresh value*/\n    '
            onlyNotifyOnFreshValue+=f'if (x!={name})'
            
        out += f"/*define {name}*/\n"
        if (notification):
            out += f"#define {name}_default ({default}) \n"
            out += f"static {variableType} {name} = {name}_default;\n"
            out += f"/*getter*/\n"
            out += f"{variableType} {accessors_prefix}_get_{name}(){{return {name};}}\n"
            out +="/*callback function pointer*/\n"
            out += f"{name}_callback_t  {name}_callback = 0;\n" 
            
            out += f"/*setter*/\n"
            if "0" == "0":
                out += f"\
void {accessors_prefix}_set_{name}({variableType} x)\n\
{{\n\
    {rangecheck}\n\
    {onlyNotifyOnFreshValue}\n\
    {{\n\
        /*see if we need to notify callback functions*/\n\
        {callbackFunction}\n\
        if(({name}_callback != 0))\n\
        {{\n\
            (*{name}_callback)(x);\n\
        }}\n\
    }}\n\
    {name} = x;\n\
}};\n"    
            out += f"/*setter of call back function*/\n"
            out += f"\
void {accessors_prefix}_set_{name}_callback({name}_callback_t i)\n\
{{\n\
    {name}_callback = i;\n\
}}\n"
            out += f"\n\n"
        
        
        else: #not notification
            #out += f"/*define {name}*/\n"
            #define
            out += f"#define {name}_default ({default}) \n"
            out += f"{variableType} {name} = {name}_default;\n"
            out += f"\n\n"
            
        return out
   
   
   
class DataManagerGenerator:

    def __init__(self, variableList=[], moduleName="DataManager", accessors_prefix="DataManager", CFileHeadersList=[], HFileHeaderList=[] ):
        self.variableList = variableList
        self.moduleName = moduleName
        self.CFileHeadersList = CFileHeadersList
        self.HFileHeaderList = HFileHeaderList
        self.accessors_prefix = accessors_prefix
        
        self.Disclamer_Header=f'/*!\n*Generated by DataManagerGenerator, do not edit manualy\n'
        self.Disclamer_Header+=f'*@file {moduleName}.h\n'
        self.Disclamer_Header+=f'*@date {date.today()}\n'
        self.Disclamer_Header+=f'*@author n.kessa\n'
        self.Disclamer_Header+=f'*@brief Manages device global configurations and device data flow between software modules.\n'
        self.Disclamer_Header+=f'*\n'
        self.Disclamer_Header+=f'*/\n\n'
        
        self.Disclamer_Source=f''
        self.Disclamer_Source+=f'/*!\n*Generated by DataManagerGenerator, do not edit manualy\n'
        self.Disclamer_Source+=f'*@file {moduleName}.c\n'
        self.Disclamer_Source+=f'*@date {date.today()}\n'
        self.Disclamer_Source+=f'*@author n.kessa\n'
        self.Disclamer_Source+=f'*@brief Manages device global configurations and device data flow between software modules.\n'
        self.Disclamer_Source+=f'*\n'
        self.Disclamer_Source+=f'*/\n\n'
        
        
    def generateHeaderFile(self):
        out = ""
        
        out+= self.Disclamer_Header
        
        #add guard
        out+=f'#ifndef {self.moduleName.upper()}_H \n'
        out+=f'#define {self.moduleName.upper()}_H \n'
        
        
        
        #add includes
        i = 0
        while i < len(self.HFileHeaderList):
            out+=self.HFileHeaderList[i]
            i = i + 1

        #add variables related stuff
        i = 0
        while i < len(self.variableList):
            self.variableList[i].accessors_prefix = self.accessors_prefix
            out+=f'/*****************************start of {self.variableList[i].name} definitions*************************************/\n'
            out+=self.variableList[i].get_header_definition()
            out+=f'/*****************************end of {self.variableList[i].name} definitions*************************************/\n\n'
            i = i + 1
        
        #close the guard
        out+=f'#endif /* {self.moduleName.upper()}_H */ \n'
  
        print("h file cintent" + out)
        f = open(f'{self.moduleName}.h', "w")
        f.write(out)
        f.close()
        
        
    def generateSourceFile(self):
    
        out=""
        out+= self.Disclamer_Source
        #add includes
        i = 0
        while i < len(self.CFileHeadersList):
            out+=self.CFileHeadersList[i]
            i = i + 1

        #add variables related stuff
        i = 0
        while i < len(variables):
            self.variableList[i].accessors_prefix = self.accessors_prefix
            out+=f'/*****************************start of {self.variableList[i].name} definitions*************************************/\n'
            out+=variables[i].get_source_implementation()
            out+=f'/*****************************end of {self.variableList[i].name} definitions*************************************/\n\n'
            i = i + 1
  
        print(out)
        f = open(f'{self.moduleName}.c', "w")
        f.write(out)
        f.close()
        


###################################### variable definition section ###################################### 

#variables used on the project
variables= []
variables.append(variable(name="var3", variableType="uint32_t",prefix="ui32",default=123,notification=True,callbackFunction="var3_notify",checkRange= True, minimum=0 , maximum=500))
variables.append(variable(name="var1", variableType="uint32_t",prefix="ui32",default=100,notification=False))
variables.append(variable(name="var2", variableType="uint32_t",prefix="ui32",default=100,notification=False))
variables.append(variable(name="var4", variableType="uint32_t",prefix="ui32",default=123,notification=True,onlyNotifyOnFreshValue = False, callbackFunction="var4_notify"))
variables.append(variable(name="var4", variableType="bool",prefix="is",default="true",notification=True, callbackFunction="is_var4_notify"))

#headers for the DataManager.h
h_headers = []
h_headers.append("#include <stdint.h>\n")
h_headers.append("#include <stdbool.h>\n")
h_headers.append("\n\n\n")

#headers for the DataManager.c
c_headers = []
c_headers.append('#include "DataManager.h"\n')
c_headers.append("\n\n\n")

###################################### end of variable definition section ###################################### 

if __name__ == "__main__":

    genrator = DataManagerGenerator(variableList=variables, moduleName="DataManager", CFileHeadersList=c_headers, HFileHeaderList =h_headers)
    genrator.generateSourceFile()
    genrator.generateHeaderFile()

exit(0)
