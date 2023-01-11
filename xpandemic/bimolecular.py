import numpy as np
import random
from xpandemic.particles import *


# BIMOLEC FUNCS NOTE: ALL THEM MUST HAVE THE SAME VARIABLES (system,tipos,Ss,indices,locs)
    
def contagion(Ss,system,superp):
    for s in superp:
        if Ss[s].species == 'Susceptible':
            system.set_particles([Exposed(Ss[s].position)])
            Ss[s].kill('exposed',system,system.s1,'converted')
            



bimolec_funcs_array = {('Infectious','Susceptible'):contagion}   
############################################           
