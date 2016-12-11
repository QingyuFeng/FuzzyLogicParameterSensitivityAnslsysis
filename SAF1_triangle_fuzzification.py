# Function f1: Fuzzification function for high 
def fuzzification_stri(var_value, var_max, var_min):
    if var_value < var_min:
        var_value = 0
    elif (var_value <= var_max) and (var_value >= var_min):
        var_value = (var_value - var_min)/(var_max - var_min)
    elif var_value > var_max:
        var_value = 1
    return var_value

# Function f2: Fuzzification function for medium
def fuzzification_tri(var_value, var_max, var_min, var_mp):
    if (var_value < var_min) or (var_value > var_max):
        var_value = 0
    elif (var_value < var_mp) and (var_value >= var_min):
        var_value = (var_value - var_min)/(var_mp - var_min)
    elif (var_value <= var_max) and (var_value > var_mp):
        var_value = (var_max - var_value)/(var_max - var_mp)
    elif var_value == var_mp:
        var_value = 1
        
    return var_value

# Function f3: Fuzzification function for not suitable
def fuzzification_ztri(var_value, var_max, var_min):
    if var_value < var_min:
        var_value = 1
    elif (var_value < var_max) and (var_value > var_min):
        var_value = (var_max - var_value)/(var_max - var_min)
    elif var_value > var_max:
        var_value = 1
    return var_value


# Function f4: Fuzzification function for high trapezium
def fuzzification_htra(var_value, var_max, var_min, var_mpl, var_mpr):
    if (var_value < var_min) or (var_value > var_max):
        var_value = 0
    elif (var_value <= var_mpl) and (var_value >= var_min):
        var_value = (var_value - var_min)/(var_mpl - var_min)
    elif (var_value <= var_max) and (var_value >= var_mpr):
        var_value = (var_max - var_value)/(var_max - var_mpr)
    elif (var_value < var_mpr) and (var_value > var_mpl):
        var_value = 1
        
    return var_value

# Function f5: Fuzzification function for not suitabile for trapezium
def fuzzification_ntra(var_value, var_max, var_min, var_mpl, var_mpr):
    if (var_value < var_min) or (var_value > var_max):
        var_value = 1
    elif (var_value <= var_mpl) and (var_value >= var_min):
        var_value = (var_mpl - var_value)/(var_mpl - var_min)
    elif (var_value <= var_max) and (var_value >= var_mpr):
        var_value = (var_value - var_mpr)/(var_max - var_mpr)
    elif (var_value < var_mpr) and (var_value > var_mpl):
        var_value = 0
        
    return var_value

# Function f6: Fuzzification function for moderate suitabile for trapezium
def fuzzification_mtra(var_value, var_max, var_min, var_mpl, var_mpr, var_lm, var_rm):
    if (var_value < var_min) or (var_value > var_max) or ((var_value < var_mpr) and (var_value > var_mpl)):
        var_value = 0
    elif (var_value < var_lm) and (var_value >= var_min):
        var_value = (var_value - var_min)/(var_lm - var_min)
    elif (var_value > var_lm) and (var_value <= var_mpl):
        var_value = (var_mpl - var_value)/(var_mpl - var_lm)
    elif (var_value < var_rm) and (var_value >= var_mpr):
        var_value = (var_value - var_rm)/(var_rm - var_mpr)
    elif (var_value > var_rm) and (var_value <= var_max):
        var_value = (var_max - var_value)/(var_max - var_rm)
    elif (var_value == var_lm) or (var_value == var_rm):
        var_value = 1
    return var_value
