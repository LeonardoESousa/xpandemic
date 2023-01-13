############################################################
# forster_singlet.py.                                        
# This example illustrates the simulation of singlet excitons.
# 3 singlet excitons.
# 2 Materials.
############################################################

import xpandemic.morphology as morphology
from xpandemic.rates import *
from xpandemic.particles import *

###BASIC PARAMETERS######################################################################
identifier         = 'SEIR' # output identifier
time_limit         = 7      # in days
animation_mode     = True
save_animation     = False  # if you want to save the animation
animation_exten    = 'gif'  # possible options ('gif' and 'mp4')
rotate             = False  # True = animation rotates, False = remains fixed
marker_type        = 1      # marker type used at the animation processs ( 0 = balls, 1 = symbols) 
pause              = False  # if you want that the annimation stops in the first frame (debug purposes)
rounds             = 50     # Number of rounds
n_proc             = 1      # Number of cores to be used
frozen             = True   # if you want for the lattice to remain the same for all rounds
periodic           = False  # if you want periodic boundary conditions
bimolec            = True   # Turn on annihilation
#########################################################################################

###SINGLET EXCITONS######################################################################

ages = {0:1,10:2,20:3,30:3,40:2,50:1}

##FORSTER RADII (m or km)
r00   = 1  #distance per day    
radii = {0:r00,10:1.1*r00,20:1.2*r00,30:1.3*r00,40:1.2*r00,50:1*r00}

## TRANSFER RATES
walk   = Walk(Rf=radii)

incub = Incubation(time=3)

ifr = {0:0.1,10:0.2,20:0.6,30:0.5,40:0.1,50:0.1}
tau_inf = 2

death = Death(time=tau_inf,ifr=ifr)
cure  = Cure(time=tau_inf,ifr=ifr)

###PROCESSES#############################################################################

processes = {'Susceptible':[walk], 'Exposed':[walk], 'Infectious':[walk], 'Recovered':[walk]}
monomolecular = {'Susceptible':[], 'Exposed':[incub],'Infectious':[death,cure], 'Recovered':[ExpireImmunity(time=tau_inf)]}
#########################################################################################
r00 = 5
radii = {0:r00,10:1.1*r00,20:1.2*r00,30:1.3*r00,40:1.2*r00,50:1*r00}
## TRANSFER RATES
walk2   = Walk(Rf=radii)
death2  = Death(time=2,ifr={0:1,10:1,20:1,30:1,40:1,50:1})
policy = {1:[{'Susceptible':[walk2], 'Exposed':[walk2], 'Infectious':[walk2]},{'Susceptible':[], 'Exposed':[incub],'Infectious':[death,cure]}]}
#intervention = morphology.Intervention(policy)


###MORPHOLOGY############################################################################

##Morphology functions

#Reading a file name that contains your lattice
#file = 'lattice.example'
#lattice_func = morphology.ReadLattice(file)


# Creating a new lattice at each new round
displacement      = [10, 10, 0]       #vector of the unit cell
lattice_func      = morphology.Map('mapa.txt',displacement)

#########################################################################################


##GENERATE PARTICLES#####################################################################
method    = morphology.randomized
#exciton   = morphology.Create_Particles('Susceptible', 4, method, ages, mat=[1])
exciton2  = morphology.Create_Particles('Infectious', 4, method, ages, mat=[1])
#########################################################################################

