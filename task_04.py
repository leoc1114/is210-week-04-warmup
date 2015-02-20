#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A single if statement."""

MYINPUT = raw_input('Tell me a story!')
MAX_LENGTH = 80
LONGSTR = 'short'

A = len(MYINPUT)

if A > MAX_LENGTH:

    LONGSTR = 'long'

else:
    print LONGSTR

OUTPUT = 'That certainly was a {} story!'.format(LONGSTR)

print OUTPUT
