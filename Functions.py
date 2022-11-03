import pandas as pd
from TypeChart import types
import sys

def attack(attacker,defender):
    return(types.at[defender, attacker])

def defend(defender,attacker):
    return(types.at[defender, attacker])

def convert_mons_to_types(team):
    types = []
    for mon in team:
        types.append(mon[0])
        if len(mon) > 1:
            types.append(mon[1])
    return(types)

# ------------------------------------- Returns a list of all types that receive super effective damage ----------------------
def attacks_for_super(attacker):
    vulnerable = []
    for type, row in types.iterrows():
        if "super" == types.at[type,attacker]:
            vulnerable.append(type)
    return(vulnerable)

# ------------------------------------- Returns a list of all types that hit defender for super effective damage ----------------------
def receives_super_from(defender):
    vulnerable = []
    for type, row in types.iterrows():
        if "super" == types.at[defender,type]:
            vulnerable.append(type)
    return(vulnerable)

# ------------------------------------- Returns a list of all types that resist damage from attacker ------------------------------
def attacks_for_resist(attacker):
    resists = []
    for type, row in types.iterrows():
        if "not" == types.at[type,attacker]:
            resists.append(type)
    return(resists)

# ------------------------------------- Returns a list of all types that hit defender for not very effective damage ----------------------
def receives_resist_from(defender):
    resists = []
    for type, row in types.iterrows():
        if "not"== types.at[defender,type]:
            resists.append(type)
    return(resists)

# ------------------------------------- Returns a list of all types that cannot hit defender --------------------------------------------
def receives_immune_from(defender):
    resists = []
    for type, row in types.iterrows():
        if "immune" == types.at[defender,type]:
            resists.append(type)
    return(resists)

# ------------------------------------- Returns a list of all types that attacker cannot hit --------------------------------------------
def attacks_for_immune(attacker):
    resists = []
    for type, row in types.iterrows():
        if "immune" == types.at[type,attacker]:
            resists.append(type)
    return(resists)

# -------------------------------------------------------- Lists -----------------------------------------------------------------------------------------

# ---------------------- Returns a list of all types that receive super effective damage from the list of types given -----------
def attacks_for_super_multiple_types(team):
    attackerList = convert_mons_to_types(team)
    vulnerable = []
    for type in attackerList:
        lists = attacks_for_super(type)
        for i in lists:
            vulnerable.append(i)
    return(vulnerable)

# ---------------------- Returns a list of all types that resist damage from the list of types given ------------------------
def attacks_for_resist_multiple_types(team):
    attackerList = convert_mons_to_types(team)
    vulnerable = []
    for type in attackerList:
        lists = attacks_for_resist(type)
        for i in lists:
            vulnerable.append(i)
    return(vulnerable)

# ---------------------- Returns a list of all types that are immune to damage from the list of types given ------------------------
def attacks_for_immune_multiple_types(team):
    attackerList = convert_mons_to_types(team)
    vulnerable = []
    for type in attackerList:
        lists = attacks_for_immune(type)
        for i in lists:
            vulnerable.append(i)
    return(vulnerable)

# ---------------------- Returns a list of all types from which defender list resists attacks  ---------------------------
def receives_resist_from_multiple_types(team):
    vulnerable = []
    resists = []
    final = []
    for mon in team:
        for type in mon:
            resists.extend(receives_resist_from(type))
            vulnerable.extend(receives_super_from(type))
    for i in resists:
        if i not in vulnerable:
            final.append(i)
    return(final)

# ---------------------- Returns a list of all types from which defender list is vulnerable to attacks  ---------------------------
def receives_super_from_multiple_types(team):
    vulnerable = []
    resists = []
    final = []
    for mon in team:
        for type in mon:
            vulnerable.extend(receives_super_from(type))
            resists.extend(receives_resist_from(type))
            resists.extend(receives_immune_from(type))
    for i in vulnerable:
        if i not in resists:
            final.append(i)
    return(final)

# ---------------------- Returns a list of all types from which defender list is immune to attacks  ---------------------------
def receives_immune_from_multiple_types(team):
    vulnerable = []
    for mon in team:
        for type in mon:
            lists = receives_immune_from(type)
            for i in lists:
                vulnerable.append(i)
    return(vulnerable)

# ----------------------------------------------------------------------------------------------------------------------------------------------------

def count_duplicates_and_remove_them(list):
    unique = {}
    count_duplicates = 0
    for i in list:
        if i not in unique:
            count_duplicates = list.count(i)
            unique[i] = count_duplicates
    return(unique)

def remove_duplicates(list):
    unique = []
    for i in list:
        if i not in unique:
            unique.append(i)
    return(unique)

def count_types(list):
    unique = []
    for i in list:
        if i not in unique:
            unique.append(i)
    return(len(unique))

def missing_types(typeslist):
    all_types = types.index.values
    missing_types = []
    for i in all_types:
        if i not in typeslist:
            missing_types.append(i)
    return(missing_types)

def types_comparisson(typeslist1,typeslist2):
    missing_types = []
    for i in typeslist1:
        if i not in typeslist2:
            missing_types.append(i)
    return(missing_types)

# ----------------------------------------------------------------------------------------------------------------------------------------------------

# ---------------------- Returns a dictionnary of types hitting for super : the amount of times  ---------------------------
def amount_types_attack_for_super(typeslist):
    list = attacks_for_super_multiple_types(typeslist)
    uniques = count_duplicates_and_remove_them(list)
    return(uniques)

# ---------------------- Returns a list of all types not covered by supereffectives  ---------------------------
def types_not_covered(typeslist):
    list = attacks_for_super_multiple_types(typeslist)
    return(missing_types(list))

# ---------------------- Returns a dictionnary of types hitting for resist : the amount of times  ---------------------------
def amount_types_attack_for_resist(typeslist):
    list = attacks_for_resist_multiple_types(typeslist)
    uniques = count_duplicates_and_remove_them(list)
    return(uniques)

# ---------------------- Returns a dictionnary of types hitting for immune : the amount of times  ---------------------------
def amount_types_attack_for_immune(typeslist):
    list = attacks_for_immune_multiple_types(typeslist)
    uniques = count_duplicates_and_remove_them(list)
    return(uniques)

# ---------------------- Returns a dictionnary of types from which receiving super : the amount of times  ---------------------------
def amount_types_receive_super_from(typeslist):
    list = receives_super_from_multiple_types(typeslist)
    uniques = count_duplicates_and_remove_them(list)
    return(uniques)

# ---------------------- Returns a dictionnary of types frpm which receiving resist : the amount of times  ---------------------------
def amount_types_receive_resist_from(typeslist):
    list = receives_resist_from_multiple_types(typeslist)
    uniques = count_duplicates_and_remove_them(list)
    return(uniques)

# ---------------------- Returns a dictionnary of types from which receiving immune : the amount of times  ---------------------------
def amount_types_receive_immune_from(typeslist):
    list = receives_immune_from_multiple_types(typeslist)
    uniques = count_duplicates_and_remove_them(list)
    return(uniques)

# ----------------------- Returns a list of types that are not covered by resistances ---------------------------
def types_not_covered_resist(typeslist):
    list = receives_resist_from_multiple_types(typeslist)
    return(missing_types(list))

# ------------------------------- Returns a list of vulnerable types that are not covered by supers ---------------------------
def blind_spots(typeslist):
    vulnerablelist = receives_super_from_multiple_types(typeslist)
    superagainstlist = attacks_for_super_multiple_types(typeslist)
    return(count_duplicates_and_remove_them(types_comparisson(vulnerablelist,superagainstlist)))

# ------------------------------- Returns a list of types not immune against ---------------------------------
def types_not_covered_immune(typeslist):
    list = receives_immune_from_multiple_types(typeslist)
    return(missing_types(list))

def str_to_class(classname):
    return getattr(sys.modules[__name__], classname)