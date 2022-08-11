# -*- coding: utf-8 -*-
"""
Created on Tue Aug 09 19:14:49 2022
@author: shabalin
This utility converts geometry parameters between conventions of HEXRD, ImageD11, PolyXSim, and pyFAI.
"""

import sys, os
import numpy as np
#from . import Geometry
#from Grain import Grain
#from PolySim import PolySim

single_separator = "--------------------------------------------------------------\n"
double_separator = "==============================================================\n"


if __name__=="__main__":
    print(single_separator)
    print('This utility convertes geometry configuration between definitions of:')
    print('- pyFAI    (.poni files)')
    print('- ImageD11 (.par  files)')
    print('- HEXRD    (.yml  files)')
    print('- PolyXSim (.inp  files)')
    print('If multiple input files provided, it takes an average of these geometries.')
    print('Usage syntax: pyhton convert_geometries.py input1.par input2.par output.par')
    print(single_separator)
    
    if len(sys.argv) < 3:
        raise ValueError('Provide at least 2 arguments: input_geometry_file, output_geometry_file!')
    inp_files = sys.argv[1:-1]
    
    list_of_geometries = []
    for input_geometry_file in inp_files:
        if   input_geometry_file[0] == '/':
            pass
        elif input_geometry_file[0:2] == './':
            input_geometry_file  = os.getcwd() +  input_geometry_file[1:]
        else:
            input_geometry_file  = os.getcwd() + '/' + input_geometry_file

        inp_filename = input_geometry_file.split('/')[-1]
        inp_directory = input_geometry_file.replace(inp_filename, '')
        print('Input  directory:',inp_directory)
        print('Input  filename:' ,inp_filename)
        
        PS = PolySim()
        PS.geometry = Geometry()
        if   inp_filename.split('.')[1] == 'inp':
            PS.load_inp(directory = inp_directory, inp_file = inp_filename)
        elif inp_filename.split('.')[1] == 'par':
            PS.geometry.load_par( directory = inp_directory, par_file  = inp_filename)
        elif inp_filename.split('.')[1] == 'yml':
            PS.geometry.load_yml( directory = inp_directory, yml_file  = inp_filename)
        elif inp_filename.split('.')[1] == 'poni':
            PS.geometry.load_poni(directory = inp_directory, poni_file = inp_filename)
        
        list_of_geometries.append(PS.geometry)
        
    PS.set_attr('geometry', Geometry.average_geometries(list_of_geometries) )
        
    out_file  = sys.argv[-1]
    if   out_file[0] == '/':
        output_geometry_file = out_file
    elif out_file[0:2] == './':
        output_geometry_file = os.getcwd() + out_file[1:]
    else:
        output_geometry_file = os.getcwd() + '/' + out_file

    out_filename = output_geometry_file.split('/')[-1]
    out_directory = output_geometry_file.replace(out_filename, '')        
    print('Output  directory:',out_directory)
    print('Output  filename:' ,out_filename)
    print('Output geometry file:', output_geometry_file)
        
    if   out_filename.split('.')[1] == 'inp':
        PS.save_inp(directory = out_directory, inp_file = out_filename)
    elif out_filename.split('.')[1] == 'par':
        PS.geometry.save_par( directory = out_directory, par_file  = out_filename)
    elif out_filename.split('.')[1] == 'yml':
        PS.geometry.save_yml( directory = out_directory, yml_file  = out_filename)
    elif out_filename.split('.')[1] == 'poni':
        PS.geometry.save_poni(directory = out_directory, poni_file = out_filename)
