/*!
*Generated by DataManagerGenerator, do not edit manualy
*@file DataManager.c
*@date 2022-10-07
*@author n.kessa
*@brief Manages device global configurations and device data flow between software modules.
*
*/

#include "DataManager.h"



/*****************************start of ui32_var3 definitions*************************************/
/*define function as external to be called on event*/
extern void var3_notify(uint32_t);
/*define ui32_var3*/
#define ui32_var3_default (123) 
static uint32_t ui32_var3 = ui32_var3_default;
/*getter*/
uint32_t DataManager_get_ui32_var3(){return ui32_var3;}
/*callback function pointer*/
ui32_var3_callback_t  ui32_var3_callback = 0;
/*setter*/
void DataManager_set_ui32_var3(uint32_t x)
{
    /*check if the assigned value within range*/
    if ((x < 0)|| (x > 500)){return; }
    /*check if we have a fresh value*/
    if (x!=ui32_var3)
    {
        /*see if we need to notify callback functions*/
        var3_notify(x);
        if((ui32_var3_callback != 0))
        {
            (*ui32_var3_callback)(x);
        }
    }
    ui32_var3 = x;
};
/*setter of call back function*/
void DataManager_set_ui32_var3_callback(ui32_var3_callback_t i)
{
    ui32_var3_callback = i;
}


/*****************************end of ui32_var3 definitions*************************************/

/*****************************start of ui32_var1 definitions*************************************/
/*define ui32_var1*/
#define ui32_var1_default (100) 
uint32_t ui32_var1 = ui32_var1_default;


/*****************************end of ui32_var1 definitions*************************************/

/*****************************start of ui32_var2 definitions*************************************/
/*define ui32_var2*/
#define ui32_var2_default (100) 
uint32_t ui32_var2 = ui32_var2_default;


/*****************************end of ui32_var2 definitions*************************************/

/*****************************start of ui32_var4 definitions*************************************/
/*define function as external to be called on event*/
extern void var4_notify(uint32_t);
/*define ui32_var4*/
#define ui32_var4_default (123) 
static uint32_t ui32_var4 = ui32_var4_default;
/*getter*/
uint32_t DataManager_get_ui32_var4(){return ui32_var4;}
/*callback function pointer*/
ui32_var4_callback_t  ui32_var4_callback = 0;
/*setter*/
void DataManager_set_ui32_var4(uint32_t x)
{
    
    
    {
        /*see if we need to notify callback functions*/
        var4_notify(x);
        if((ui32_var4_callback != 0))
        {
            (*ui32_var4_callback)(x);
        }
    }
    ui32_var4 = x;
};
/*setter of call back function*/
void DataManager_set_ui32_var4_callback(ui32_var4_callback_t i)
{
    ui32_var4_callback = i;
}


/*****************************end of ui32_var4 definitions*************************************/

/*****************************start of is_var4 definitions*************************************/
/*define function as external to be called on event*/
extern void is_var4_notify(bool);
/*define is_var4*/
#define is_var4_default (true) 
static bool is_var4 = is_var4_default;
/*getter*/
bool DataManager_get_is_var4(){return is_var4;}
/*callback function pointer*/
is_var4_callback_t  is_var4_callback = 0;
/*setter*/
void DataManager_set_is_var4(bool x)
{
    
    /*check if we have a fresh value*/
    if (x!=is_var4)
    {
        /*see if we need to notify callback functions*/
        is_var4_notify(x);
        if((is_var4_callback != 0))
        {
            (*is_var4_callback)(x);
        }
    }
    is_var4 = x;
};
/*setter of call back function*/
void DataManager_set_is_var4_callback(is_var4_callback_t i)
{
    is_var4_callback = i;
}


/*****************************end of is_var4 definitions*************************************/

