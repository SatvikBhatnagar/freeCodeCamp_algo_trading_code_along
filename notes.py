#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 10:47:56 2023

@author: stoner69
"""

#freeCodeCamp - https://www.youtube.com/watch?v=xfzGZB4HhEE

#Algorithmic Trading with Python by Nick McCullum

###############################################
#Section 1 -- Algorithmic Trading Basics
###############################################

#Algorithmic Trading Overview
"""Algorithmic trading means using computers to make investment decisions.
There are many different types of algorithmic trading. The main difference 
is their speed of execution."""

#The Algorithmic Trading Landscape
"""Here are some of the main players in the algorithmic trading landscape:
    - Renaissance Technologies
    - AQR Capital Management
    - Citadel Securities """
    
#Algorithmic Trading & Python
"""Python is the most popular programming language for algorithmic trading.
However, Python is slow. This means that it is often used as a "glue language"
to trigger code that runs in other languages. One example of this is the NumPy
library for Python, which we'll be using in this course.
NumPy is the most popular Python library for performing numerical computing.

Although it's written for use in Python, the core underlying functionality is
writtern in C, which is a much faster language."""

#The Algorithmic Trading Process
"""The process of running a quantitaive investing strategy can be broken down
into the following steps:
    1. Collect data
    2. Develop a hypothesis for a strategy
    3. Backtest that strategy"""



###############################################
#Section 2 - API Basics
###############################################

#What is an API?
"""An API is an Application Programming Interface.
APIs allow you to interact with someone else's software using your own code."""

#API Functionality
"""GET: Retreive data from a server at the specified resource.
   POST: Adds data to the database exposed by the API. (Create only)
   PUT: Adds and overwrites data in the database exposed by the API. (Create or replace)
   DELETE: Deletes data from the API's database"""