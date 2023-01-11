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
identifier         = 'forster_singlet' #output identifier
time_limit         = np.inf# in PS
animation_mode     = True
save_animation     = False # if you want to save the animation
animation_exten    = 'gif' # possible options ('gif' and 'mp4')
rotate             = False             # True = animation rotates, False = remains fixed
marker_type        = 1     # marker type used at the animation processs ( 0 = balls, 1 = symbols) 
pause              = False # if you want that the annimation stops in the first frame (debug purposes)
rounds             = 5000     # Number of rounds
n_proc             = 10     # Number of cores to be used
frozen             = True              # if you want for the lattice to remain the same for all rounds
periodic           = True             # if you want periodic boundary conditions
bimolec            = True  # Turn on annihilation
#########################################################################################

###SINGLET EXCITONS######################################################################

##FORSTER RADII (Å)
r00   = 25   #distance per day    
radii = {0:r00, 10:r00}


##EXCITION TRANSFER RATES
walk   = Walk(Rf=radii)

incub = Incubation(time=3)

ifr = 0.1
tau_inf = 7

death = Death(time=tau_inf,ifr=ifr)
cure  = Cure(time=tau_inf,ifr=ifr)

###PROCESSES#############################################################################

processes = {'Susceptible':[walk], 'Infectious':[walk], 'Exposed':[walk]}
monomolecular = {'Susceptible':[],'Infectious':[death,cure],'Exposed':[incub]}
#########################################################################################

###MORPHOLOGY############################################################################

##Morphology functions

#Reading a file name that contains your lattice
#file = 'lattice.example'
#lattice_func = morphology.ReadLattice(file)


# Creating a new lattice at each new round
num_sites         = 100           #number of sites of the lattice
displacement      = [5, 5, 0]       #vector of the unit cell
disorder          = [0.,0.,0.]   #std deviation from avg position
composition       = [1,0]       #popuation probility Ex.: distribu_vect[0] is the prob of mat 0 appear in the lattice
lattice_func      = morphology.Lattice(num_sites,displacement,disorder,composition)

#ENERGIES
#Gaussian distribuitions
t1s   = {0:(3.7,0.0), 1:(3.7,0.0), 'level':'t1'} #(Peak emission energy (eV), disperison (eV)
s1s   = {0:(6.1,0.0), 1:(6.1,0.0), 'level':'s1'} # triplet energy, disperison (eV)

a1 = morphology.Gaussian_energy(s1s)
a2 = morphology.Gaussian_energy(t1s) 
#########################################################################################


##GENERATE PARTICLES#####################################################################
method    = morphology.randomized
exciton   = morphology.Create_Particles('Susceptible', 4, method, mat=[0])
exciton2  = morphology.Create_Particles('Infectious', 1, method, mat=[0])
#########################################################################################

