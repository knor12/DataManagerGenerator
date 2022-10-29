

#include <stdio.h>
#include "DataManager.h"
void  var3_notify (uint32_t i )
{
    
    printf("var3_notify:%d\n",i); 
}

void  var4_notify (uint32_t i )
{
    
    printf("var4_hhhhhhnotify:%d\n",i); 
}

void  is_var4_notify (uint32_t i )
{
    
    printf("is_vae4_notify:%d\n",i); 
}
 void ui32_var4_notify(uint32_t i )
{
    
    printf("var4_callback:%d\n",i); 
}

void var3_callback_(uint32_t i )
{
    
    printf("var3_callback:%d\n",i); 
}

int main()
{
    
    DataManager_set_ui32_var1(10);
    DataManager_set_ui32_var2(20); 
    DataManager_set_ui32_var3_callback(var3_callback_);
    DataManager_set_ui32_var4_callback(ui32_var4_notify);
    
    
    DataManager_set_ui32_var3(10);
    DataManager_set_ui32_var3(3333);
    
    
    DataManager_set_ui32_var3(1);
    DataManager_set_ui32_var3(1);
    DataManager_set_ui32_var3(1);
    for (int i =0; i <100;i++)
    {
        DataManager_set_ui32_var3(33*i);
        DataManager_set_ui32_var4(2222*i);
    }
    
    printf("var1:%d\n", DataManager_get_ui32_var1());
    printf("var2:%d\n", DataManager_get_ui32_var2());

    return 0;
}
