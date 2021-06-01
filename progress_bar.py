#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This is a function to calculate the progress based on iteration.





Code by: Jian Sun
-- Jan., 2019
-- PennState
"""

import time
import math
def progress_bar(i, N, startTime, showTimeOnly=False):
    """
    Parameters:
    -----------
    i : the current loop index
    N : the total length
    startTime = time.time() before the 1st loop
    showTimeOnly: False, will printing the progess bar as moving forward.
                  True, will only print the Elapsed & Remaining Time.
    ===========
    Output:
    -----------
    Printing a progress bar, Elapsed, and approximating Remaining Time.
    """
    # 
    # 
    # s
    ic = math.modf((i+1)/N*100)
    int_ic = int(ic[1])
    dec_ic = int(ic[0]*10)
    
    time_elapsed = time.time() - startTime
    time_remain = time_elapsed / (i + 0.000001) * (N-i+1.000001)
    if showTimeOnly:
        if i+1==N: time_remain =0
        print('Time Elapsed: {:.0f}m{:.1f}s, Remaining: {:.0f}m{:.1f}s'.format(time_elapsed // 60, time_elapsed % 60 ,time_remain // 60, time_remain % 60))
    else:
        if dec_ic != 0:
            if i+1==N: time_remain =0
            print('\r[{}{}{}{}]{:.0f}%, Elapsed: {:.0f}m{:.1f}s, Remaining: {:.0f}m{:.1f}s'
                  .format('='*int_ic, '>', dec_ic, ' '*(100-int_ic-1), int_ic, time_elapsed // 60, time_elapsed % 60 ,time_remain // 60, time_remain % 60),end='')
        else:
            print('\r[{}{}{}]{:.0f}%, Elapsed: {:.0f}m{:.1f}s, Remaining: {:.0f}m{:.1f}s'
                  .format('='*int_ic, '>', ' '*(100-int_ic), int_ic, time_elapsed // 60, time_elapsed % 60, time_remain // 60, time_remain % 60),end='')
        if time_elapsed / (i + 0.001) < 0.05: 
            time.sleep(0.05)

    return