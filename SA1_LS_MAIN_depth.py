"""
This code was generated by Qingyu Feng
on Dec 20, 2014

The goal of this program was to test the sensitivity of
fuzzy logic system to the variations of input criteria.

The method used for sensitivity analysis is called one at
a time. This code aimed at evaluate the global sensitivity of
each variable.

"""

# Input Criteria variables
from SA2_LS_CriteriaValues import *
from numpy import *
from SAF2_LS_FuzzyLogicProcess_Depth import *

##
##from mpl_toolkits.mplot3d import Axes3D
##from matplotlib.collections import PolyCollection
##from matplotlib.colors import colorConverter
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D


criteria = {"depth":depth_input, "slope":slope_input, "salinity":salinity_input, "ph":ph_input, "prcp_grow":prcp_grow_input}

# Function 1: Generate base land plot for each variable
def generate_land(criteria):
    land_factors = zeros((10, 5))
    for lfidx in range(len(land_factors)):
        land_factors[lfidx] = [criteria["depth"][lfidx], criteria["slope"][4],
                              criteria["salinity"][4], criteria["ph"][4],
                              criteria["prcp_grow"][4]]
    return land_factors    

# Function 2: Generate variable change sceries
def criteria_scale(max_value, min_value):

    max_scale = max_value*scale_change
    min_scale = min_value*scale_change

    max_unchange = max_value*array(scale_unchange)
    min_unchange = min_value*array(scale_unchange)
    
    mp_max_scale_min_unchange = (max_scale + min_unchange)/2
    mp_min_scale_max_unchange = (min_scale + max_unchange)/2
    mp_max_scale_min_scale = (min_scale + max_scale)/2
    mp_min_unchange_max_unchange = (min_unchange + max_unchange)/2
    
    return max_scale, min_scale, max_unchange, min_unchange,\
            mp_max_scale_min_unchange, mp_min_scale_max_unchange, \
            mp_max_scale_min_scale, mp_min_unchange_max_unchange
    
    



# Calling functions:
# Function 1: Generate base land plot for each variable
land_factors = generate_land(criteria)
print(land_factors)

# Function 2: Generate variable change sceries
max_scale, min_scale, max_unchange, min_unchange, mp_max_scale_min_unchange, \
mp_min_scale_max_unchange, mp_max_scale_min_scale, mp_min_unchange_max_unchange \
= criteria_scale(depth_max, depth_min)

#
# Function 3: calculate defuzzified results for each combination

defuzzy_max = zeros((5,10))
defuzzy_min = zeros((5,10))
defuzzy_min_max = zeros((5,10))

for pidx in range(len(max_scale)):
    for landfidx in range(len(land_factors)):
        defuzzy_max[pidx][landfidx] = fuzzylogic(land_factors[landfidx], max_scale[pidx], min_unchange[pidx], mp_max_scale_min_unchange[pidx])
        defuzzy_min[pidx][landfidx] = fuzzylogic(land_factors[landfidx], max_unchange[pidx], min_scale[pidx], mp_min_scale_max_unchange[pidx])
        defuzzy_min_max[pidx][landfidx] = fuzzylogic(land_factors[landfidx], max_scale[pidx], min_scale[pidx], mp_max_scale_min_scale[pidx])

x = land_factors[:, 0]
y_max = max_scale
y_min = min_scale
#y_maxim = arange(slope_min*0.6, slope_max*1.6, (slope_max*1.6 - slope_min*0.6)/5)




fig = plt.figure(figsize=(10,5))

# Add subfigure for min
ax = fig.add_subplot(1, 2, 1, projection='3d')
xs, ys = meshgrid(x, y_min)
zs = defuzzy_min
surf = ax.plot_surface(xs, ys, zs, rstride=1, cstride=1,
                       linewidth=0.1, antialiased=False,
                       alpha = 0.3,
                       cmap='summer')
ax.set_xlabel("Depth as input")
ax.set_ylabel("Lower bd")
ax.set_zlabel("Land suitability index")
ax.set_title("Lower bound depth")
ax.tick_params(axis='x', which='both', pad=1)
ax.tick_params(axis='y', which='both', pad=1)
ax.tick_params(axis='z', which='both', pad=1)




# Add subfigure for mpl
ax = fig.add_subplot(1, 2, 2, projection='3d')
xs, ys = meshgrid(x, y_max)
zs = defuzzy_max
surf = ax.plot_surface(xs, ys, zs, rstride=1, cstride=1,
                       linewidth=0.1, antialiased=False,
                       alpha = 0.3,
                       cmap='summer')
ax.set_xlabel("Depth as input")
ax.set_ylabel("Upper bd")
ax.set_zlabel("Land suitability index")
ax.set_title("Upper bound depth")
ax.tick_params(axis='x', which='both', pad=1)
ax.tick_params(axis='y', which='both', pad=1)
ax.tick_params(axis='z', which='both', pad=1)

font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 14}

plt.rc('font', **font)


plt.tight_layout()








#
#fig = plt.figure()
#ax = Axes3D(fig)
#ax.set_xlabel("Slope as input")
#
##ax.set_ylabel("Upper Bound of Slope ")
##ax.set_ylabel("Lower Bound of Slope ")
#ax.set_ylabel("Whole range of Slope ")
#
#ax.set_zlabel("Land suitability index")
#ax.set_title("Slope-Min-Max(%) within 20% change")
#
#
#ax.plot_surface(xs, ys, zs, rstride=1, cstride=1, cmap='winter')
#plt.show()
#fig.savefig("D:/ArcGIS/04_FSLS_SensitivityAnalysis/NewCode/Depth-")
