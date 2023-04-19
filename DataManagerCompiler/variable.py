__author__      = "Noreddine Kessa"
__copyright__   = "!"
__license__ = "MIT License"


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
        
    def __str__(self):
        st = f'name={self.name}, type={self.variableType}, default={self.default}, notification={self.notification}, onFresh={self.onlyNotifyOnFreshValue}, callback={self.callbackFunction}, min={self.minimum}, max={self.maximum}'
        return st    
        
    def get_header_definition( self ):
        name = self.name
        notification = self.notification
        variableType = self.variableType
        accessors_prefix = self.accessors_prefix
        default = self.default
        callback_type= f'{name}_callback_t'
        accessors_prefix = self.accessors_prefix
        checkRange = self.checkRange
        
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
            if self.checkRange:
                out += f"#define {accessors_prefix}_set_{name}(x) {{ if ((x>= {self.minimum} )&&( x<= {self.maximum})){{ {name} = x ; }} }}\n"
            else:
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
        if self.callbackFunction !="" and self.notification:
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
            out += f"#define {name.upper()}_DEFAULT ({default}) \n"
            out += f"{variableType} {name} = {name.upper()}_DEFAULT;\n"
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
            out += f"#define {name.upper()}_DEFAULT ({default}) \n"
            out += f"{variableType} {name} = {name.upper()}_DEFAULT;\n"
            out += f"\n\n"
            
        return out
   
