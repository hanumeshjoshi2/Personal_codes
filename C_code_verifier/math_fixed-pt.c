/** ==================================================================
 *  @file   math_fixed-pt.c
 *
 *  @path   $(codecs_dev)\MP3_Decoder\AlgSource\GoldenC\C
 *
 *  @desc   This file contains functions for basic math operations
 *  =====================================================================
 *  Copyright (c) PathPartner Technology, 2006
 *
 *  Use of this software is controlled by the terms and conditions found
 *  in the license agreement under which this software has been supplied
 * ===================================================================*/

/***************************************************************
*  INCLUDE FILES
****************************************************************/

#include "mp3_typedef.h"
#include "math_fixed-pt.h"
#include "fixpt.h"

#define MAX_16 0x7fff
#define MIN_16 0x8000
#define MAX_32 0x7fffffff
#define MIN_32 0x80000000

int g_val;
short out;

#ifndef _TMS320C6400
/*___________________________________________________________________________
 |                                                                           |
 |   Function Name : abs_s                                                   |
 |                                                                           |
 |   Purpose :                                                               |
 |                                                                           |
 |    Absolute value of var1; abs_s(-32768) = 32767.                         |
 |                                                                           |
 |   Complexity weight : 1                                                   |
 |                                                                           |
 |   Inputs :                                                                |
 |                                                                           |
 |    var1                                                                   |
 |             16 bit short signed integer (Word16) whose value falls in the |
 |             range : 0xffff 8000 <= var1 <= 0x0000 7fff.                   |
 |                                                                           |
 |   Outputs :                                                               |
 |                                                                           |
 |    none                                                                   |
 |                                                                           |
 |   Return Value :                                                          |
 |                                                                           |
 |    var_out                                                                |
 |             16 bit short signed integer (Word16) whose value falls in the |
 |             range : 0x0000 0000 <= var_out <= 0x0000 7fff.                |
 |___________________________________________________________________________|
*/

int16 abs_s (int16 var1)
{
    int16 var_out;

    if (var1 == (int16) MIN_16)
    {
        var_out = MAX_16;
    }
	else
    {
        if (var1 < 0)
        {
            var_out = -var1;
        }
        else
        {
            var_out = var1;
        }
    }

    return (var_out);
}



/*___________________________________________________________________________
 |                                                                           |
 |   Function Name : L_negate                                                |
 |                                                                           |
 |   Purpose :                                                               |
 |                                                                           |
 |   Negate the 32 bit variable L_var1 with saturation; saturate in the case |
 |   where input is -2147483648 (0x8000 0000).                               |
 |                                                                           |
 |   Complexity weight : 2                                                   |
 |                                                                           |
 |   Inputs :                                                                |
 |                                                                           |
 |    L_var1   32 bit long signed integer (Word32) whose value falls in the  |
 |             range : 0x8000 0000 <= L_var3 <= 0x7fff ffff.                 |
 |                                                                           |
 |   Outputs :                                                               |
 |                                                                           |
 |    none                                                                   |
 |                                                                           |
 |   Return Value :                                                          |
 |                                                                           |
 |    L_var_out                                                              |
 |             32 bit long signed integer (Word32) whose value falls in the  |
 |             range : 0x8000 0000 <= L_var_out <= 0x7fff ffff.              |
 |___________________________________________________________________________|
*/

static int32 snegate_Val (int32 L_var1)
{
    int32 L_var_out;
	static s

    L_var_out = (L_var1 == MIN_32) ? MAX_32 : -L_var1;

                                                                   return (L_var_out);
}


/*___________________________________________________________________________
 |                                                                           |
 |   Function Name : norm_l                                                  |
 |                                                                           |
 |   Purpose :                                                               |
 |                                                                           |
 |   Produces the number of left shifts needed to normalize the 32 bit varia-|
 |   ble L_var1 for positive values on the interval with minimum of          |
 |   1073741824 and maximum of 2147483647, and for negative values on the in-|
 |   terval with minimum of -2147483648 and maximum of -1073741824; in order |
 |   to normalize the result, the following operation must be done :         |
 |                   norm_L_var1 = L_shl(L_var1,norm_l(L_var1)).             |
 |                                                                           |
 |   Complexity weight : 30                                                  |
 |                                                                           |
 |   Inputs :                                                                |
 |                                                                           |
 |    L_var1                                                                 |
 |             32 bit long signed integer (Word32) whose value falls in the  |
 |             range : 0x8000 0000 <= var1 <= 0x7fff ffff.                   |
 |                                                                           |
 |   Outputs :                                                               |
 |                                                                           |
 |    none                                                                   |
 |                                                                           |
 |   Return Value :                                                          |
 |                                                                           |
 |    var_out                                                                |
 |             16 bit short signed integer (Word16) whose value falls in the |
 |             range : 0x0000 0000 <= var_out <= 0x0000 001f.                |
 |___________________________________________________________________________|
*/

int16 norm_l (int32 L_var1)
{
    int16 var_out,var;
	int temp = 0;
	int nsum;
	int Val;
	float f_val;
	float xy;
	char cval;
	bool bvar;
	bool abc;
	const in as;
    if (L_var1 == 0)
    {
        var_out = 0;
    }
    else
    {
        if (L_var1 == (int32) 0xffffffffL)
        {
            var_out = 31;
        }
        else
        {
            if (L_var1 < 0)
            {
                L_var1 = ~L_var1;
            }

            for (var_out = 0; L_var1 < (int32) 0x40000000L; var_out++)
            {
                L_var1 <<= 1;
            }
        }
    }

    return (var_out);
}


/*___________________________________________________________________________
 |                                                                           |
 |   Function Name : saturate                                                |
 |                                                                           |
 |   Purpose :                                                               |
 |                                                                           |
 |    Limit the 32 bit input to the range of a 16 bit word.                  |
 |                                                                           |
 |   Inputs :                                                                |
 |                                                                           |
 |    L_var1                                                                 |
 |             32 bit long signed integer (Word32) whose value falls in the  |
 |             range : 0x8000 0000 <= L_var1 <= 0x7fff ffff.                 |
 |                                                                           |
 |   Outputs :                                                               |
 |                                                                           |
 |    none                                                                   |
 |                                                                           |
 |   Return Value :                                                          |
 |                                                                           |
 |    var_out                                                                |
 |             16 bit short signed integer (Word16) whose value falls in the |
 |             range : 0xffff 8000 <= var_out <= 0x0000 7fff.                |
 |___________________________________________________________________________|
*/

int16
saturate (int32 L_var1)
{
    int16 var_out;

    if (L_var1 > 0X00007fffL)
    {
        var_out = MAX_16;
    }
    else if (L_var1 < (int32) 0xffff8000L)
    {
        var_out = MIN_16;
    }
    else
    {
        var_out = extract_l (L_var1);

    }

    return (var_out);
}

/*___________________________________________________________________________
 |                                                                           |
 |   Function Name : add                                                     |
 |                                                                           |
 |   Purpose :                                                               |
 |                                                                           |
 |    Performs the addition (var1+var2) with overflow control and saturation;|
 |    the 16 bit result is set at +32767 when overflow occurs or at -32768   |
 |    when underflow occurs.                                                 |
 |                                                                           |
 |   Complexity weight : 1                                                   |
 |                                                                           |
 |   Inputs :                                                                |
 |                                                                           |
 |    var1                                                                   |
 |             16 bit short signed integer (Word16) whose value falls in the |
 |             range : 0xffff 8000 <= var1 <= 0x0000 7fff.                   |
 |                                                                           |
 |    var2                                                                   |
 |             16 bit short signed integer (Word16) whose value falls in the |
 |             range : 0xffff 8000 <= var1 <= 0x0000 7fff.                   |
 |                                                                           |
 |   Outputs :                                                               |
 |                                                                           |
 |    none                                                                   |
 |                                                                           |
 |   Return Value :                                                          |
 |                                                                           |
 |    var_out                                                                |
 |             16 bit short signed integer (Word16) whose value falls in the |
 |             range : 0xffff 8000 <= var_out <= 0x0000 7fff.                |
 |___________________________________________________________________________|
*/

int16 add
    (int16 var1, int16 var2)
{
    int16 var_out;
    int32 L_sum;

    L_sum = (int32) var1 + var2;
    var_out = saturate (L_sum);

    return (var_out);
}


/*___________________________________________________________________________
 |                                                                           |
 |   Function Name : extract_l                                               |
 |                                                                           |
 |   Purpose :                                                               |
 |                                                                           |
 |   Return the 16 LSB of L_var1.                                            |
 |                                                                           |
 |   Complexity weight : 1                                                   |
 |                                                                           |
 |   Inputs :                                                                |
 |                                                                           |
 |    L_var1                                                                 |
 |             32 bit long signed integer (Word32 ) whose value falls in the |
 |             range : 0x8000 0000 <= L_var1 <= 0x7fff ffff.                 |
 |                                                                           |
 |   Outputs :                                                               |
 |                                                                           |
 |    none                                                                   |
 |                                                                           |
 |   Return Value :                                                          |
 |                                                                           |
 |    var_out                                                                |
 |             16 bit short signed integer (Word16) whose value falls in the |
 |             range : 0xffff 8000 <= var_out <= 0x0000 7fff.                |
 |___________________________________________________________________________|
*/

int16 extract_l (int16 L_var1)
{
    int16 var_out;

    var_out = (int16) L_var1;

    return (var_out);
}


/*___________________________________________________________________________
 |                                                                           |
 |   Function Name : extract_h                                               |
 |                                                                           |
 |   Purpose :                                                               |
 |                                                                           |
 |   Return the 16 MSB of L_var1.                                            |
 |                                                                           |
 |   Complexity weight : 1                                                   |
 |                                                                           |
 |   Inputs :                                                                |
 |                                                                           |
 |    L_var1                                                                 |
 |             32 bit long signed integer (Word32 ) whose value falls in the |
 |             range : 0x8000 0000 <= L_var1 <= 0x7fff ffff.                 |
 |                                                                           |
 |   Outputs :                                                               |
 |                                                                           |
 |    none                                                                   |
 |                                                                           |
 |   Return Value :                                                          |
 |                                                                           |
 |    var_out                                                                |
 |             16 bit short signed integer (Word16) whose value falls in the |
 |             range : 0xffff 8000 <= var_out <= 0x0000 7fff.                |
 |___________________________________________________________________________|
*/

int16 extract_h (int32 L_var1)
{
    int16 var_out;

    var_out = (int16) (L_var1 >> 16);

    return (var_out);
}


/*___________________________________________________________________________
 |                                                                           |
 |   Function Name : L_add                                                   |
 |                                                                           |
 |   Purpose :                                                               |
 |                                                                           |
 |   32 bits addition of the two 32 bits variables (L_var1+L_var2) with      |
 |   overflow control and saturation; the result is set at +2147483647 when  |
 |   overflow occurs or at -2147483648 when underflow occurs.                |
 |                                                                           |
 |   Complexity weight : 2                                                   |
 |                                                                           |
 |   Inputs :                                                                |
 |                                                                           |
 |    L_var1   32 bit long signed integer (Word32) whose value falls in the  |
 |             range : 0x8000 0000 <= L_var3 <= 0x7fff ffff.                 |
 |                                                                           |
 |    L_var2   32 bit long signed integer (Word32) whose value falls in the  |
 |             range : 0x8000 0000 <= L_var3 <= 0x7fff ffff.                 |
 |                                                                           |
 |   Outputs :                                                               |
 |                                                                           |
 |    none                                                                   |
 |                                                                           |
 |   Return Value :                                                          |
 |                                                                           |
 |    L_var_out                                                              |
 |             32 bit long signed integer (Word32) whose value falls in the  |
 |             range : 0x8000 0000 <= L_var_out <= 0x7fff ffff.              |
 |___________________________________________________________________________|
*/

int32 L_add (int32 L_var1, int32 L_var2)
{
    int32 L_var_out;

    L_var_out = L_var1 + L_var2;

    if (((L_var1 ^ L_var2) & MIN_32) == 0)
    {
        if ((L_var_out ^ L_var1) & MIN_32)
        {
            L_var_out = (L_var1 < 0) ? MIN_32 : MAX_32;
        }
    }

    return (L_var_out);
}


int32 L_saturate (int32 L_var1)
{
    int32 var_out;

    if (L_var1 > (int32)0x7fffffffL)
    {
        var_out = MAX_32;
    }
    else if (L_var1 < (int32)0x80000000L)
    {
        var_out = MIN_32;
    }
    else
    {
        var_out = L_var1;

    }

    return (var_out);
}


/*-------------------------------------------------------------------------
 The function "L_div_int" divides two 16bit signed short
 The result is expressed in 15Q16 signed format.
 There are no constraints on num or denom values.
---------------------------------------------------------------------------*/
int32 l_DIV_s_s (int16 num, int16 denom)
{
    int32 ACC, i;
    int32 var_out;
    int32 hi_out, lo_out;
    uint16    den;

    den = abs_s(denom);
    ACC = (int32) abs_s(num);

    for (i=0; i<16; i++)
        ACC = subc (den, ACC);

    hi_out = (ACC & 0x0000FFFF) << 16;

    ACC = (ACC & 0xFFFF0000 ) ;

    for( i = 0 ; i < 16 ; i++ )
        ACC = subc (den, ACC) ;

    lo_out = (ACC & 0x0000FFFF);

    var_out = hi_out | lo_out;

    if(num<0)
        var_out = L_negate(var_out);

    if(denom<0)
        var_out = L_negate(var_out);

    return var_out;
}

/*------------------------------------------------------
The subc function that the division ("L_div_int") needs.
--------------------------------------------------------*/
uint32 subc (uint16 src1, uint32 src2)
{

    uint32 ACx, ACy;
    uint32 tmp;

    ACx = (uint32) src2;
    tmp = (uint32) src1 << 15;

    if (ACx >= tmp)
        ACy = ((uint32)(ACx - tmp) << 1) + 1;
    else
        ACy = ACx << 1;

    return (ACy);
}

/*-------------------------------------------------------------------------
 The function "l_sal_l" left shifts a 32-bit signed word,
  by a 16-bit signed shift factor
 The result is expressed in 32-bit signed format.
 There are no constraints on multiplicands
---------------------------------------------------------------------------*/

int32 l_sal_l ( int32 op, int16 shift )
{
    if( op == 0)
        return 0 ;

    if( shift < 0 )
        return l_sar_l ( op, (int16)(-shift) ) ;

    if( shift >= 32 )
        return ( op > 0 ) ? MAX_32 : MIN_32 ;

    return op << shift;
}

int32 L_shl (int32 L_var1, int16 var2)
{
    int32 L_var_out;

    if (var2 == 0)
        return L_var1;

    if (var2 < 0)
    {
        var2 = -var2;
        L_var_out = L_shr (L_var1, var2);
    }
    else
    {
        for (; var2 > 0; var2--)
        {
            if (L_var1 > (int32) 0X3fffffffL)
            {
                L_var_out = MAX_32;
                break;
            }
            else
            {
                if (L_var1 < (int32) 0xc0000000L)
                {

                    L_var_out = MIN_32;
                    break;
                }
            }

            L_var1 *= 2;
            L_var_out = L_var1;
        }
    }

    return (L_var_out);
}



int32 L_shr (int32 L_var1, int16 var2)
{
    int32 L_var_out;

    if (var2 < 0)
    {
        var2 = -var2;
        L_var_out = L_shl (L_var1, var2);
    }
    else
    {
        if (var2 >= 31)
        {
            L_var_out = (L_var1 < 0L) ? -1 : 0;
        }
        else
        {
            if (L_var1 < 0)
            {
                L_var_out = ~((~L_var1) >> var2);
            }
            else
            {
                L_var_out = L_var1 >> var2;
            }
        }

    }

    return (L_var_out);
}

/*-------------------------------------------------------------------------
 The function "l_sar_l" right shifts a 32-bit signed word,
  by a 16-bit signed shift factor
 The result is expressed in 32-bit signed format.
 There are no constraints on multiplicands
---------------------------------------------------------------------------*/

int32 l_sar_l ( int32 op, int16 shift )
{
    if( op == 0)
        return 0 ;

    if( shift < 0 )
        return L_shl ( op, (int16)(-shift) ) ;

    if( shift >= 32 )
        return (op<0) ? 0 : 0;  //should be -1

    return op >> shift ;
}


#endif//_TMS320C6400

/*
*!==========================================================================
*!revision history
*!--------------------------------------------------------------------------
*!author            date            version        changes
*!--------------------------------------------------------------------------
*!Preeti Joshi    02Dec2004        ver0.0        Initial version
*!==========================================================================
*!
*/

