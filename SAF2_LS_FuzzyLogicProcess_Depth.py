"""
This code was generated by Qingyu Feng
on Dec 20, 2014

The goal of this program was to test the sensitivity of
fuzzy logic system to the variations of input criteria.

The method used for sensitivity analysis is called one at
a time. This code aimed at evaluate the global sensitivity of
each variable.

This code stores the function for calculating defuzzification
results.

"""
from SAF1_triangle_fuzzification import *
from SA2_LS_CriteriaValues import *
from SA2_RuleGeneration import *
final_rule = rule_infer(rule_list)

def fuzzylogic(landfactor, max_v, min_v, mp_v):
    """
    lfparameter = elements in land factors
    max_value, min_value, mp: the array of max, min, and mp value for specific variable.
    """
    
    depth_fhs = []
    depth_fms = []
    depth_fns = []

    salinity_fhs = []
    salinity_fms = []
    salinity_fns = []

    slope_fhs = []
    slope_fms = []
    slope_fns = []

    ph_fhs = []
    ph_fms = []
    ph_fns = []

    prcpgrows_fhs = []
    prcpgrows_fms = []
    prcpgrows_fns = []

    dictvar = {}

    fri_hs = 0
    fri_gs = 0
    fri_ms = 0
    fri_ps = 0
    fri_ns = 0
    
    depth_fhs = fuzzification_stri(landfactor[0], max_v, min_v)
    depth_fms = fuzzification_tri(landfactor[0], max_v, min_v, mp_v)
    depth_fns = fuzzification_ztri(landfactor[0], max_v, min_v)
       
    salinity_fhs = fuzzification_ztri(landfactor[1], salinity_max, salinity_min)
    salinity_fms = fuzzification_tri(landfactor[1], salinity_max, salinity_min, salinity_mp)
    salinity_fns = fuzzification_stri(landfactor[1], salinity_max, salinity_min)

    slope_fhs = fuzzification_ztri(landfactor[2], slope_max, slope_min)
    slope_fms = fuzzification_tri(landfactor[2], slope_max, slope_min, slope_mp)
    slope_fns = fuzzification_stri(landfactor[2], slope_max, slope_min)

    ph_fhs = fuzzification_htra(landfactor[3], ph_max, ph_min, ph_mpl, ph_mpr)
    ph_fms = fuzzification_mtra(landfactor[3], ph_max, ph_min, ph_mpl, ph_mpr, ph_lm, ph_rm)
    ph_fns = fuzzification_ntra(landfactor[3], ph_max, ph_min, ph_mpl, ph_mpr)

    prcpgrows_fhs = fuzzification_stri(landfactor[4], prcp_grow_max, prcp_grow_min)
    prcpgrows_fms = fuzzification_tri(landfactor[4], prcp_grow_max, prcp_grow_min, prcp_grow_mp)
    prcpgrows_fns = fuzzification_ztri(landfactor[4], prcp_grow_max, prcp_grow_min)

    dictvar = {"depth_fhs": depth_fhs,
               "depth_fms": depth_fms,
               "depth_fns": depth_fns,

               "salinity_fhs": salinity_fhs,
               "salinity_fms": salinity_fms,
               "salinity_fns": salinity_fns,
               
               "slope_fhs": slope_fhs,
               "slope_fms": slope_fms,
               "slope_fns": slope_fns,

               "ph_fhs": ph_fhs,
               "ph_fms": ph_fms,
               "ph_fns": ph_fns,

               "prcpgrows_fhs": prcpgrows_fhs,
               "prcpgrows_fms": prcpgrows_fms,
               "prcpgrows_fns": prcpgrows_fns}

    temp = [0]*len(final_rule)
    for fridx in range(len(final_rule)):
        temp[fridx] = final_rule[fridx][1:]
        for subridx in range(len(temp[fridx])):
            temp[fridx][subridx] = min(dictvar[temp[fridx][subridx][0]],
                        dictvar[temp[fridx][subridx][1]],
                        dictvar[temp[fridx][subridx][2]],
                        dictvar[temp[fridx][subridx][3]],
                        dictvar[temp[fridx][subridx][4]])
    fri_hs = max(temp[0])
    fri_gs = max(temp[1])
    fri_ms = max(temp[2])
    fri_ps = max(temp[3])
    fri_ns = max(temp[4])

    defuzzy_temp = (fri_hs * hs_com + fri_gs * gs_com + fri_ms * ms_com + fri_ps * ps_com
                            + fri_ns * ns_com)/(fri_hs + fri_gs + fri_ms + fri_ps + fri_ns)
    return defuzzy_temp

