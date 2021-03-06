#!/usr/bin/env python
"""
Example file generation for a real condensation system
"""
from starpolymers import MoleculeFactory, System, ConfigFile
import pytest
import json
import os.path as path

ROOT = '/'.join(path.abspath(__file__).split('/')[:-1])

def _compare(*args):
    return True

def _parse_molecules(fname):
    with open(fname, 'r') as f:
        data = json.load(f, encoding='utf-8')['molecules']
    return data

def _generate(fout):
    f_mol = '{}/molecules.json'.format(ROOT)
    box = 50
    molecules = MoleculeFactory(_parse_molecules(f_mol), box=box).molecules
    system = System(box, molecules=molecules)
    config = ConfigFile(system, comment='Real condensation system')
    config.write(fout)

def test_07():
    fout = '{}/test_config.dat'.format(ROOT)
    _generate(fout)
    assert ConfigFile.validate(fout)
    assert ConfigFile.compare('{}/config.dat'.format(ROOT), fout)

if __name__ == '__main__':
    test_07()