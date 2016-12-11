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
from SAF2_LS_FuzzyLogicProcess_pH import *

##
##from mpl_toolkits.mplot3d import Axes3D
##from matplotlib.collections import PolyCollection
##from matplotlib.colors import colorConverter
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D


criteria = {"depth":depth_input, "slope":slope_input, "salinity":salinity_input, "ph":ph_input, "prcp_grow":prcp_grow_input}

# Function 1: Generate base land plot for each variable
def generate_land(criteria):
    land_factors = zeros((29, 5))
    for lfidx in range(len(land_factors)):
        land_factors[lfidx] = [criteria["depth"][4], criteria["slope"][4],
                              criteria["salinity"][4], criteria["ph"][lfidx],
                              criteria["prcp_grow"][4]]
    return land_factors    

# Function 2: Generate variable change sceries
def criteria_scale(max_value, min_value, mpl_value, mpr_value):

    max_scale = max_value*scale_change_ph
    min_scale = min_value*scale_change_ph
    mpl_scale = mpl_value*scale_change_ph
    mpr_scale = mpr_value*scale_change_ph

    max_unchange = max_value*array(scale_unchange)
    min_unchange = min_value*array(scale_unchange)
    mpl_unchange = mpl_value*array(scale_unchange)
    mpr_unchange = mpr_value*array(scale_unchange)
        
        
    lmp_min_scale_mpl_unchanged = (min_scale + mpl_unchange)/2
    lmp_mpl_scale_min_unchanged = (mpl_scale + min_unchange)/2
    lmp_mpl_unchanged_min_unchanged = (mpl_unchange + min_unchange)/2
    
    rmp_mpr_unchanged_max_unchanged = (mpr_unchange + max_unchange)/2
    rmp_mpr_scale_max_unchanged = (mpr_scale + max_unchange)/2
    rmp_mpr_unchanged_max_scale = (mpr_unchange + max_scale)/2

    lmp_mpr_scale_min_scale = (mpl_scale + min_scale)/2
    rmp_mpr_scale_max_scale = (mpr_scale + max_scale)/2

    return max_scale, min_scale, max_unchange, min_unchange,\
            mpl_scale, mpr_scale, mpl_unchange, mpr_unchange,\
            lmp_min_scale_mpl_unchanged, lmp_mpl_scale_min_unchanged,\
            lmp_mpl_unchanged_min_unchanged, rmp_mpr_unchanged_max_unchanged,\
            rmp_mpr_scale_max_unchanged, rmp_mpr_unchanged_max_scale,\
            lmp_mpr_scale_min_scale, rmp_mpr_scale_max_scale
    



# Calling functions:
# Function 1: Generate base land plot for each variable
land_factors = generate_land(criteria)
print(land_factors)
#
# Function 2: Generate variable change sceries
max_scale, min_scale, max_unchange, min_unchange,\
mpl_scale, mpr_scale, mpl_unchange, mpr_unchange,\
lmp_min_scale_mpl_unchanged, lmp_mpl_scale_min_unchanged,\
lmp_mpl_unchanged_min_unchanged, rmp_mpr_unchanged_max_unchanged,\
rmp_mpr_scale_max_unchanged, rmp_mpr_unchanged_max_scale\
,lmp_mpr_scale_min_scale, rmp_mpr_scale_max_scale\
     = criteria_scale(ph_max, ph_min, ph_mpl, ph_mpr)


## Function 3: calculate defuzzified results for each combination
#
defuzzy_max = zeros((5,29))
defuzzy_min = zeros((5,29))
defuzzy_mpr = zeros((5,29))
defuzzy_mpl = zeros((5,29))
defuzzy_four = zeros((5,29))

defuzzy_min_max = zeros((5,29))
#
for pidx in range(len(max_scale)):
    for landfidx in range(len(land_factors)):
        defuzzy_max[pidx][landfidx] = fuzzylogic(land_factors[landfidx],
                 max_scale[pidx], min_unchange[pidx], 
                mpl_unchange[pidx], mpr_unchange[pidx],
                lmp_mpl_unchanged_min_unchanged[pidx],
                 rmp_mpr_unchanged_max_scale[pidx])
        defuzzy_min[pidx][landfidx] = fuzzylogic(land_factors[landfidx],
                 max_unchange[pidx], min_scale[pidx], 
                mpl_unchange[pidx], mpr_unchange[pidx],
                lmp_min_scale_mpl_unchanged[pidx],
                 rmp_mpr_unchanged_max_unchanged[pidx])
                 
        defuzzy_mpr[pidx][landfidx] = fuzzylogic(land_factors[landfidx],
                 max_unchange[pidx], min_unchange[pidx], 
                mpl_unchange[pidx], mpr_scale[pidx],
                lmp_mpl_unchanged_min_unchanged[pidx],
                 rmp_mpr_scale_max_unchanged[pidx])
        defuzzy_mpl[pidx][landfidx] = fuzzylogic(land_factors[landfidx],
                 max_unchange[pidx], min_unchange[pidx], 
                mpl_scale[pidx], mpr_unchange[pidx],
                lmp_mpl_scale_min_unchanged[pidx],
                 rmp_mpr_unchanged_max_unchanged[pidx])

        defuzzy_four[pidx][landfidx] = fuzzylogic(land_factors[landfidx],
                 max_scale[pidx], min_scale[pidx], 
                mpl_scale[pidx], mpr_scale[pidx],
                lmp_mpr_scale_min_scale[pidx],
                 rmp_mpr_scale_max_scale[pidx])


x = land_factors[:, 3]
#y = max_scale
#y = min_scale

y_min = arange(ph_min*0.9, ph_min*1.15, (ph_min*1.15 - ph_min*0.9)/5)
y_max = arange(ph_max*0.9, ph_max*1.15, (ph_max*1.15 - ph_max*0.9)/5)
y_mpr = arange(ph_mpr*0.9, ph_mpr*1.15, (ph_mpr*1.15 - ph_mpr*0.9)/5)
y_mpl = arange(ph_mpl*0.9, ph_mpl*1.15, (ph_mpl*1.15 - ph_mpl*0.9)/5)
y_four = arange(ph_min*0.9, ph_max*1.15, (ph_max*1.15 - ph_min*0.9)/5)



fig = plt.figure(figsize=(10,10))

# Add subfigure for min
ax = fig.add_subplot(3, 2, 1, projection='3d')
xs, ys = meshgrid(x, y_min)
zs = defuzzy_min
surf = ax.plot_surface(xs, ys, zs, rstride=1, cstride=1,
                       linewidth=0.1, antialiased=False,
                       alpha = 0.3,
                       cmap='summer')
ax.set_xlabel("pH as input")
ax.set_ylabel("Left lower bd")
ax.set_zlabel("Land suitability index")
ax.set_title("Left lower bound pH")
ax.tick_params(axis='x', which='both', pad=1)
ax.tick_params(axis='y', which='both', pad=1)
ax.tick_params(axis='z', which='both', pad=1)




# Add subfigure for mpl
ax = fig.add_subplot(3, 2, 2, projection='3d')
xs, ys = meshgrid(x, y_mpl)
zs = defuzzy_mpl
surf = ax.plot_surface(xs, ys, zs, rstride=1, cstride=1,
                       linewidth=0.1, antialiased=False,
                       alpha = 0.3,
                       cmap='summer')
ax.set_xlabel("pH as input")
ax.set_ylabel("Left upper bd")
ax.set_zlabel("Land suitability index")
ax.set_title("Left upper bound pH")
ax.tick_params(axis='x', which='both', pad=1)
ax.tick_params(axis='y', which='both', pad=1)
ax.tick_params(axis='z', which='both', pad=1)

# Add subfigure for mpr
ax = fig.add_subplot(3, 2, 3, projection='3d')
xs, ys = meshgrid(x, y_mpr)
zs = defuzzy_mpr
surf = ax.plot_surface(xs, ys, zs, rstride=1, cstride=1,
                       linewidth=0.1, antialiased=False,
                       alpha = 0.3,
                       cmap='summer')
ax.set_xlabel("pH as input")
ax.set_ylabel("Right upper bd")
ax.set_zlabel("Land suitability index")
ax.set_title("Right upper bound pH")
ax.tick_params(axis='x', which='both', pad=1)
ax.tick_params(axis='y', which='both', pad=1)
ax.tick_params(axis='z', which='both', pad=1)
# Add sub figure for max
ax = fig.add_subplot(3, 2, 4, projection='3d')
xs, ys = meshgrid(x, y_max)
zs = defuzzy_max
surf = ax.plot_surface(xs, ys, zs, rstride=1, cstride=1,
                       linewidth=0.1, antialiased=False,
                       alpha = 0.3,
                       cmap='summer')
ax.set_xlabel("pH as input")
ax.set_ylabel("Right lower bd")
ax.set_zlabel("Land suitability index")
ax.set_title("Right lower bound pH")
ax.tick_params(axis='x', which='both', pad=1)
ax.tick_params(axis='y', which='both', pad=1)
ax.tick_params(axis='z', which='both', pad=1)

# Add sub figure for max
#ax = fig.add_subplot(3, 3, , projection='3d', )
#xs, ys = meshgrid(x, y_four)
#zs = defuzzy_four
#surf = ax.plot_surface(xs, ys, zs, rstride=1, cstride=1,
#                       linewidth=0.1, antialiased=False,
#                       alpha = 0.3,
#                       cmap='summer')
#ax.set_xlabel("pH as input")
#ax.set_ylabel("Right lower bd")
#ax.set_zlabel("Land suitability index")
#ax.set_title("Right lower bound pH")
#ax.tick_params(axis='x', which='both', pad=1)
#ax.tick_params(axis='y', which='both', pad=1)
#ax.tick_params(axis='z', which='both', pad=1)


font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 14}

plt.rc('font', **font)


plt.tight_layout()







#fig = plt.figure(figsize=(4,4))
#ax = Axes3D(fig)
#ax.set_xlabel("pH as input")

#ax.set_ylabel("Upper Bound of Slope ")
#ax.set_ylabel("Lower Bound of Slope ")
#ax.set_ylabel("Changes of pH min")
#
#ax.set_zlabel("Land suitability index")
#ax.set_title("pH-left_bound(%) within 10% change")
#
#
#ax.plot_surface(xs, ys, zs, rstride=1, cstride=1, cmap='winter')
#plt.gca().invert_xaxis()
#plt.show()
##fig.savefig("D:/ArcGIS/04_FSLS_SensitivityAnalysis/NewCode/Depth-")