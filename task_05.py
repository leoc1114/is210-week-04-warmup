#!usr/bin/env python
# _*_ coding: utf-8 _*_
"""TASK 5"""

BLOOD = int(raw_input('What is your current blood pressure:'))

if BLOOD < 89:

    BP_STATUS = 'Low'

elif 90 <= BLOOD < 119:

    BP_STATUS = 'Ideal'

elif 120 <= BLOOD < 139:

    BP_STATUS = 'Warning'

elif 140 <= BLOOD < 159:

    BP_STATUS = 'High'

elif BLOOD > 160:

    BP_STATUS = 'EMERGENCY'

RESULT = 'Your status is currenly:{}'.format(BP_STATUS)

print RESULT
