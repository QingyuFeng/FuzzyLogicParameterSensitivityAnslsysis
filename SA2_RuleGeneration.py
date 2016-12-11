# This script is written by Qingyu Feng
# on Aug 12, 2014
# The function of this script is to generate the results of fuzzy rule inference.
# There are three suitability classes (membership function) for each environmental variable.
# These suitability classes will be inter-combined and a list of combination will be
# generated. These combination will be the IF part of the fuzzy rule inference.
# These rules will be classified into 5 suitability classes, which will be the then part
# and will be conducted later.



# Input and outputs:
# Input will be 4 environmental variables, each with 3 suitability classes.
# These environmental variables and suitability variables will be input
# from raster layers.
# suit5_var represents the 5 suitability classes that will be used in defuzzification.


# Input variables
envi_var = [0]*5
suit3_var = [0]*3
suit5_var = [[0]]*5
envi_suit3 = [0]*len(envi_var)

# Assign original values to input variables
envi_var[0] = "ph"
envi_var[1] = "slope"
envi_var[2] = "salinity"
envi_var[3] = "depth"
envi_var[4] = "prcpgrows"
#envi_var[5] = "prcpann"

suit3_var[0] = "fhs"
suit3_var[1] = "fms"
suit3_var[2] = "fns"

suit5_var[0] = ["hs"]
suit5_var[1] = ["gs"]
suit5_var[2] = ["ms"]
suit5_var[3] = ["ps"]
suit5_var[4] = ["ns"]



# Functions:
# Function 1: generating the combinations of envi and suitability variables
def comb(envi_var, suit3_var, envi_suit3):
    # This function aims at creating a matrix that includes both envi and suit variables.
    for esidx in range(len(envi_suit3)):
        envi_suit3[esidx] = [envi_var[esidx]]*len(suit3_var)
        for subesidx in range(len(suit3_var)):
            envi_suit3[esidx][subesidx] = envi_suit3[esidx][subesidx] + "_" + suit3_var[subesidx]

    return envi_suit3



# Function 2: generating rule list
def rule_gen (envi_suit3):
    # This function will create a matrix includes full combinations of all envi and suit variables.
    # The results will serve as the base of IF part of the fuzzy rule inference.
    rule_list = [[]]
    for envi in envi_suit3:
        # This syntax reads each elements in the envivar.
        #print "Environment suitability combined"
        #print envi
        temp_list = []
        for suit in envi:
            # This sentence print each element
            # print "Element in each combination"
            #print suit
            for idx in rule_list:
                # first, the idx was empty
                # The first run added the 3 elements of ph.
                # The second run, 3 elements of slopes were added.
                # Then the other elements
                # At last, the rzdepth was added. 
                temp_list.append(idx + [suit])
    # The idea comes from "http://code.activestate.com/recipes/496807-list-of-all-combination-from-multiple-lists/"
        rule_list = temp_list
        #print rule_list
        
    return rule_list




# Function 3: Fuzzy Rule Inference
# This functions will convert each of the combination into one of 5 suitability classes including highly suitable,
# marginally suitable, good suitability, poor suitability, and not suitable.
# The rules for converting are:
# 1. When there is at least one not suitable, the combinations will be considered as not suitable (N). 
# 2. When there are all highly suitable variables, the combination will be considered as highly suitable (H)
# 3. When there are 1 and 2 marginally suitable variables, the combination will be considered as good suitability (G)
# 4. When there are 3 and 4 marginally suitable variables, the combination will be considered as marginal suitability (M).
# 5. When there are 5 and 6 marginally suitable, the combination will be considered as poor suitable (P), 

# The minimum values from the 6 components of each combination will be taken as the results of IF part.
# For the THEN part with same linguistic values, the maximum numeric value will be taken as its final value for suitability.
# This will be calculated in Function 4. 
def rule_infer(rule_list):
    # The function aims at converting all combinations to a smaller groups containing the results from different combinations.
    # I would like first assign one list variables for each of the linguistic variable.
    # Then do the judgement and put the results in to corresponding variables by using the function "append".
    import sys
    # These temp variables will be used to store the components in one combination in one loop. They will be used in judgement. 
    # Suit_list is an intermediate variable that are used to store the element of rules
    suit_list = []
    # suit_count is another intermediate variable that count the number of suitability classes as a criteria to determine the
    # 5-scale suitability classes.
    suit_count = {}

    for ridx in rule_list:
        # The following step will extract the suitbaility class for each component in each rule list.
        # The suitability class was assigned as the last letter.
        for sub_ridx in ridx:
            #print sub_ridx[-3:] The last three leters were the 3 suitability class for each variable
            suit_list.append(sub_ridx[-3:])
        
        # The next sentence counted the numbers of suitability class, which will be used as the criteria for
        # determine the final suitability class.
        suit_count = {suit3_var[0]: suit_list.count(suit3_var[0]),
                      suit3_var[1]: suit_list.count(suit3_var[1]),
                      suit3_var[2]: suit_list.count(suit3_var[2])}
        #print suit_count



        if suit_count[suit3_var[2]] == 0:
            if suit_count[suit3_var[0]] == 5:
                suit5_var[0].append(ridx)
##            print "Highly suitable"
##            print suit3_var[0]
##            print suit_count[suit3_var[0]]
##            print ridx
##            print "\n"
            
            if (suit_count[suit3_var[1]] == 1 or suit_count[suit3_var[1]] == 2):
                suit5_var[1].append(ridx)
##                print "Good suitable"
##                print suit_count[suit3_var[1]]
##                print ridx
##                print "\n"

                
            if (suit_count[suit3_var[1]] == 3 or suit_count[suit3_var[1]] == 4):
                suit5_var[2].append(ridx)
##                print "Marginally suitable"
##                print suit3_var[1]
##                print suit_count[suit3_var[1]]
##                print ridx
##                print "\n"

            if suit_count[suit3_var[1]] == 5:
                suit5_var[3].append(ridx)
##                print "Poor suitable"
##                print suit5_var[3]
##                print ridx
##                print "\n"


        if suit_count[suit3_var[2]] > 0:
            suit5_var[4].append(ridx)
##            #print "Not suitable"
##            print suit3_var[2]
##            print suit_count[suit3_var[2]]
##            #print ridx
##            print "\n"

        suit_list = []

    return suit5_var






# Call functions
# Calling function 1
envi_suit3 = comb(envi_var, suit3_var, envi_suit3)

# Calling function 2
rule_list = rule_gen(envi_suit3)




# Calling function 3
# This function will be called by another script to apply the rules for rasters
##suit5_var = rule_infer(rule_list)
####
##print "number of highly suitable is", len(suit5_var[0])-1
##print "number of good suitable is", len(suit5_var[1])-1
##
##print "number of moderate suitable is", len(suit5_var[2])-1
##print "number of poor suitable is", len(suit5_var[3])-1
##print "number of not suitable is", len(suit5_var[4])-1










