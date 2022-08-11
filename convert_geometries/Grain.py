# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 11:00:00 2022

@author: shabalin

Class to work with a grain object. Loads .log  files.
"""

import sys, os
import numpy as np
from numpy import float32
from datetime import datetime

single_separator = "--------------------------------------------------------------\n"
double_separator = "==============================================================\n"

class Grain:
    
    def __init__(self, directory=None, grain_id=None):
        self.log = []
#         self.absorbed =[]
        self.directory = None
        self.grain_id = None
        self.log_file = None
        self.gff_file = None
        self.spacegroup = None
        self.unitcell = []
        self.u = None
        self.ubi = None
        self.eps = None
        self.size = None
        self.mean_IA = None
        self.position = None
        self.pos_chisq = None
        self.r = None
        self.phi = None
        self.quaternion = None
        self.summary = None
        self.gvectors_report = []
        self.measured_gvectors = []
        self.expected_gvectors = []
        self.add_to_log('Created Grain object.', True)
        if directory: self.set_attr('directory', directory)
        if grain_id : self.set_attr('grain_id' , grain_id)
        return
 

    def add_to_log(self, str_to_add, also_print = False):
        self.log.append( str(datetime.now()) + '> ' + str_to_add )
        if also_print: print(str_to_add)
        return
    
    
    def set_attr(self, attr, value):
        old = getattr(self, attr)
        setattr(self, attr, value)
        new = getattr(self, attr)
        if attr in ['gvectors_report', 'measured_gvectors', 'expected_gvectors']:
            old, new = f'list of {len(old)}', f'list of {len(new)}'
        self.add_to_log(attr+': '+str(old)+' -> '+str(new))
        return
        
        
    def add_to_attr(self, attr, value):
        old_list = getattr(self, attr)
        setattr(self, attr, old_list+[value])
        new_list = getattr(self, attr)
        self.add_to_log(attr+': += '+str(new_list[-1]))
        return
    
    
    def print(self, also_log = False):
        print(double_separator+'Grain object:')
        print('directory:' , self.directory )
        print('grain_id:'  , self.grain_id  )
        print('log_file:'  , self.log_file  )
        print('gff_file:'  , self.gff_file  )
        print('spacegroup:', self.spacegroup)
        print('unitcell:'  , self.unitcell  )
        print('u:'         , self.u         )
        print('ubi:'       , self.ubi       )
        print('eps:'       , self.ubi       )
        print('size:'      , self.size      )
        print('mean_IA:'   , self.mean_IA   )
        print('position:'  , self.position  )
        print('pos_chisq:' , self.pos_chisq )
        print('r:'         , self.r         )
        print('phi:'       , self.phi       )
        print('quaternion:', self.quaternion)
        print('summary:'   , self.summary   )
        print('gvectors_report:'  , len(self.gvectors_report  ))
        print('measured_gvectors:', len(self.measured_gvectors))
        print('expected_gvectors:', len(self.expected_gvectors))
#         print('absorbed:', len(self.absorbed))
        if also_log:
            print(single_separator + 'Log:')
            for record in self.log: print(record)
        return
