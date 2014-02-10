#!/usr/bin/env python
# emacs: -*- mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vi: set ft=python sts=4 ts=4 sw=4 et:
"""Script to auto-generate our API docs.
"""
# stdlib imports
import os
import argparse
import sys
import inspect
from nipype.interfaces.base import Interface


def listClasses(module=None):
    if module:
        __import__(module)
        pkg = sys.modules[module]
        print "Available Interfaces:"
        for k,v in pkg.__dict__.items():
            if inspect.isclass(v) and issubclass(v, Interface):
                print "\t%s"%k

def add_options(parser=None, module=None, function=None):
    interface = None
    if parser and module and function:
        __import__(module)
        interface = getattr(sys.modules[module],function)()

        for k,v in interface.inputs.items():
            if hasattr(v, "mandatory") and v.mandatory:
                parser.add_argument(k, help=v.desc)
            else:
                parser.add_argument("--%s"%k, dest=k,
                                help=v.desc)
    return parser, interface

def run_instance(interface, options):
    if interface:
        print "setting function inputs"
        for k,_ in interface.inputs.items():
            if getattr(options, k) != None:
                setattr(interface.inputs, k,
                        getattr(options, k))
        print interface.inputs
        res = interface.run()
        print res.outputs    


def parse_args():
    
    if len(sys.argv) == 2:
        listClasses(sys.argv[1])
        return
    
    parser = argparse.ArgumentParser(description='Nipype interface runner')
    parser.add_argument("module", type=str, help="Module name")
    parser.add_argument("interface", type=str, help="Interface name")
    parsed = parser.parse_args(args=sys.argv[1:3])
    
    _, prog = os.path.split(sys.argv[0])
    interface_parser = argparse.ArgumentParser(description="Run %s"%parsed.interface, prog=" ".join([prog] + sys.argv[1:3]))
    interface_parser, interface  = add_options(interface_parser, parsed.module, parsed.interface)
    args = interface_parser.parse_args(args=sys.argv[3:])
    run_instance(interface, args)


#*****************************************************************************
if __name__ == '__main__':
    parse_args()
