# Simple demo to test configuration of PSI4 in Batch Shipyard
# Per PSiAPI example from http://www.psicode.org/psi4manual/1.1/psiapi.html
#! Sample HF/cc-pVDZ H2O Computation
import os, sys
import psi4

psi4.core.set_output_file('output-python.dat', False)

#! Sample HF/cc-pVDZ H2O Computation

psi4.set_memory('500 MB')

h2o = psi4.geometry("""
O
H 1 0.96
H 1 0.96 2 104.5
""")

psi4.energy('scf/cc-pvdz')