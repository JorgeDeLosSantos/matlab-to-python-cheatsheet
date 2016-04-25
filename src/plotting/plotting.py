# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import inspect
import sys

def plot_line():
    x = np.linspace(0,2*np.pi)
    y = np.cos(x)
    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    
    ax.plot(x, y)
    fig.savefig('line_01.png')
    plt.close()
    
def plot_line_02():
    x = np.linspace(0,2*np.pi)
    y = np.sin(x)
    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    
    ax.plot(x, y, color="#00ffff", ls='--', lw=3)
    fig.savefig('line_02.png')
    plt.close()


def plot_bar():
    print 12

if __name__=='__main__':
    __all__ = inspect.getmembers(sys.modules[__name__], inspect.isfunction)
    for name,function in __all__:
        function() #...
    
    
