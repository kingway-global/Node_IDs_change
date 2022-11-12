# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 12:24:40 2022

@author: kakdemi
"""

import pandas as pd
import numpy as np

#Defining the interconnection number (1 for WEST, 2 for EAST, 3 for ERCOT)
Interconnection_ID = 2

#Defining number of nodes
NODE_NUMBER = [115, 125, 150, 175, 200, 225, 250, 275, 300, 400, 500, 750, 1000]
#NODE_NUMBER_2 = [75,100,125,150,175,200,225,250,275,300]

#Changing node IDs in selected, excluded nodes as well as outputs in ASU network reduction algorithm
for NN in NODE_NUMBER:
    
    #Changing selected and excluded node IDs
    selected = pd.read_csv('selected_nodes_{}.csv'.format(NN))
    excluded = pd.read_csv('excluded_nodes_{}.csv'.format(NN))
    
    selected_new = selected.copy()
    excluded_new = excluded.copy()
    
    for i in range(len(selected)):
        selected_new.loc[i,'SelectedNodes'] = int(str(selected_new.loc[i,'SelectedNodes']) + str(Interconnection_ID))
        
    for i in range(len(excluded)):
        excluded_new.loc[i,'ExcludedNodes'] = int(str(excluded_new.loc[i,'ExcludedNodes']) + str(Interconnection_ID))
        
    selected_new.to_csv('New_files_new_IDs/selected_nodes_{}.csv'.format(NN),index=False)
    excluded_new.to_csv('New_files_new_IDs/excluded_nodes_{}.csv'.format(NN),index=False)

#Since there are no reduction files for 50 nodes, I started another for loop    
#for NN in NODE_NUMBER_2:
    
    #Changing node IDs in outputs of ASU network reduction algorithm
#    Summary_df = pd.read_excel('Results_Excluded_Nodes_{}.xlsx'.format(NN),header=0,sheet_name='Summary')
#    Bus_df = pd.read_excel('Results_Excluded_Nodes_{}.xlsx'.format(NN),header=0,sheet_name='Bus')
#    Gen_df = pd.read_excel('Results_Excluded_Nodes_{}.xlsx'.format(NN),header=0,sheet_name='Gen')
#    Branch_df = pd.read_excel('Results_Excluded_Nodes_{}.xlsx'.format(NN),header=0,sheet_name='Branch')
    
#    Summary_df_new = Summary_df.copy()
#    Bus_df_new = Bus_df.copy()
#    Gen_df_new = Gen_df.copy()
#    Branch_df_new = Branch_df.copy()
    
#    for i in range(len(Branch_df)):
        
#        Branch_df_new.loc[i,'fbus'] = int(str(Branch_df_new.loc[i,'fbus']) + str(Interconnection_ID))
#        Branch_df_new.loc[i,'tbus'] = int(str(Branch_df_new.loc[i,'tbus']) + str(Interconnection_ID))
        
#    for i in range(len(Gen_df)):
        
#        Gen_df_new.loc[i,'Bus'] = int(str(Gen_df_new.loc[i,'Bus']) + str(Interconnection_ID))
        
#    for i in range(len(Bus_df)):
        
#        Bus_df_new.loc[i,'bus_i'] = int(str(Bus_df_new.loc[i,'bus_i']) + str(Interconnection_ID))
        
#    for i in range(5,len(Summary_df)):
        
#        selected_sentence = Summary_df_new.loc[i,'**********Reduction Summary****************']
#        splitted_sentence = selected_sentence.split()
        
#        splitted_sentence[4] = splitted_sentence[4] + str(Interconnection_ID)
#        splitted_sentence[8] = splitted_sentence[8] + str(Interconnection_ID)
        
#        joined_sentence = ' '.join(splitted_sentence)
        
#        Summary_df_new.loc[i,'**********Reduction Summary****************'] = joined_sentence
        
#    with pd.ExcelWriter('New_files_new_IDs/Results_Excluded_Nodes_{}.xlsx'.format(NN), engine='openpyxl') as writer:  
#        Summary_df_new.to_excel(writer, sheet_name='Summary',index=False)
#        Bus_df_new.to_excel(writer, sheet_name='Bus',index=False)
#        Gen_df_new.to_excel(writer, sheet_name='Gen',index=False)
#        Branch_df_new.to_excel(writer, sheet_name='Branch',index=False)
        
#Changing nodes_to_BA_state
nodes_to_BA = pd.read_csv('nodes_to_BA_state.csv',header=0)
del nodes_to_BA['Unnamed: 0']
nodes_to_BA_new = nodes_to_BA.copy()

for i in range(len(nodes_to_BA)):
    nodes_to_BA_new.loc[i,'Number'] = int(str(nodes_to_BA_new.loc[i,'Number']) + str(Interconnection_ID))
    
nodes_to_BA_new.to_csv('New_files_new_IDs/nodes_to_BA_state.csv')

nodes_to_BA = pd.read_csv('nodes_to_BA_state_original.csv',header=0)
del nodes_to_BA['Unnamed: 0']
nodes_to_BA_new = nodes_to_BA.copy()

for i in range(len(nodes_to_BA)):
    nodes_to_BA_new.loc[i,'Number'] = int(str(nodes_to_BA_new.loc[i,'Number']) + str(Interconnection_ID))
    
nodes_to_BA_new.to_csv('New_files_new_IDs/nodes_to_BA_state_original.csv')

#Changing Heat_rates_EIA
heat_rates = pd.read_csv('Heat_rates_EIA.csv',header=0)
heat_rates_new = heat_rates.copy()

for i in range(len(heat_rates)):
    heat_rates_new.loc[i,'BusNum'] = int(str(heat_rates_new.loc[i,'BusNum']) + str(Interconnection_ID))
    
heat_rates_new.to_csv('New_files_new_IDs/Heat_rates_EIA.csv',index=False)   

#Changing Generators_EIA
gen = pd.read_csv('Generators_EIA.csv',header=0)
gen_new = gen.copy()

for i in range(len(gen)):
    gen_new.loc[i,'BusNum'] = int(str(gen_new.loc[i,'BusNum']) + str(Interconnection_ID))
    
gen_new.to_csv('New_files_new_IDs/Generators_EIA.csv',index=False)

#Changing data_genparams
genparams = pd.read_csv('data_genparams.csv',header=0)
genparams_new = genparams.copy()

for i in range(len(genparams)):
    genparams_new.loc[i,'node'] = str(genparams_new.loc[i,'node'] + str(Interconnection_ID))
    
genparams_new.to_csv('New_files_new_IDs/data_genparams.csv',index=False)

genparams = pd.read_csv('data_genparams_full.csv',header=0)
genparams_new = genparams.copy()

for i in range(len(genparams)):
    genparams_new.loc[i,'node'] = str(genparams_new.loc[i,'node'] + str(Interconnection_ID))
    
genparams_new.to_csv('New_files_new_IDs/data_genparams_full.csv',index=False)

#Changing thermal_gens
thermal_gen = pd.read_csv('thermal_gens.csv',header=0)
thermal_gen_new = thermal_gen.copy()

for i in range(len(thermal_gen)):
    thermal_gen_new.loc[i,'Bus'] = int(str(thermal_gen_new.loc[i,'Bus']) + str(Interconnection_ID))
    
thermal_gen_new.to_csv('New_files_new_IDs/thermal_gens.csv',index=False)

#Changing Load_EIA
load = pd.read_csv('Load_EIA.csv',header=0)
load_new = load.copy()

for i in range(len(load)):
    load_new.loc[i,'Number'] = int(str(load_new.loc[i,'Number']) + str(Interconnection_ID))
    
load_new.to_csv('New_files_new_IDs/Load_EIA.csv',index=False)   

#Changing Buses_EIA
buses_EIA = pd.read_csv('Buses_EIA.csv',header=0)
buses_EIA_new = buses_EIA.copy()

for i in range(len(buses_EIA)):
    buses_EIA_new.loc[i,'Number'] = int(str(buses_EIA_new.loc[i,'Number']) + str(Interconnection_ID))
    
buses_EIA_new.to_csv('New_files_new_IDs/Buses_EIA.csv',index=False)   

#Changing EIA
EIA = pd.read_csv('EIA.csv',header=0)
EIA_new = EIA.copy()

for i in range(len(EIA)):
    EIA_new.loc[i,'Number'] = int(str(EIA_new.loc[i,'Number']) + str(Interconnection_ID))
    
EIA_new.to_csv('New_files_new_IDs/EIA.csv',index=False)

#Changing oil_nodes
oil_nodes = pd.read_csv('oil_nodes.csv',header=0)
oil_nodes_new = oil_nodes.copy()

for i in range(len(oil_nodes)):
    oil_nodes_new.loc[i,'Bus'] = str(oil_nodes_new.loc[i,'Bus'] + str(Interconnection_ID))
    
oil_nodes_new.to_csv('New_files_new_IDs/oil_nodes.csv',index=False)  

#Changing test
test = pd.read_csv('test.csv',header=0)
test_new = test.copy()

for i in range(len(test)):
    test_new.loc[i,'Number'] = int(str(test_new.loc[i,'Number']) + str(Interconnection_ID))
    
test_new.to_csv('New_files_new_IDs/test.csv',index=False)

#Changing gen_mat
gen_mat = pd.read_csv('gen_mat.csv', header=0)
gen_mat_new = gen_mat.copy()
buses = pd.DataFrame(gen_mat_new.columns)

for i in range(1, len(buses)):
    buses.iloc[i,0] = str(buses.iloc[i,0]) + str(Interconnection_ID)
gen_mat_new.columns = buses[0]

gen_mat_new.to_csv('New_files_new_IDs/gen_mat.csv',index=False)

gen_mat = pd.read_csv('gen_mat_full.csv', header=0)
gen_mat_new = gen_mat.copy()
buses = pd.DataFrame(gen_mat_new.columns)

for i in range(1, len(buses)):
    buses.iloc[i,0] = str(buses.iloc[i,0]) + str(Interconnection_ID)
gen_mat_new.columns = buses[0]

gen_mat_new.to_csv('New_files_new_IDs/gen_mat_full.csv',index=False)

#Changing line_to_bus
line_to_bus = pd.read_csv('line_to_bus.csv', header=0)
line_to_bus_new = line_to_bus.copy()
buses = pd.DataFrame(line_to_bus_new.columns)

for i in range(1, len(buses)):
    buses.iloc[i,0] = str(buses.iloc[i,0]) + str(Interconnection_ID)
line_to_bus_new.columns = buses[0]

line_to_bus_new.to_csv('New_files_new_IDs/line_to_bus.csv',index=False)

#Changing must_run
must_run = pd.read_csv('must_run.csv', header=0)
must_run_new = must_run.copy()
buses = pd.DataFrame(must_run_new.columns)

for i in range(len(buses)):
    buses.iloc[i,0] = str(buses.iloc[i,0]) + str(Interconnection_ID)
must_run_new.columns = buses[0]

must_run_new.to_csv('New_files_new_IDs/must_run.csv',index=False)

#Changing nodal_hydro
hydro = pd.read_csv('nodal_hydro.csv', header=0)
hydro_new = hydro.copy()
buses = pd.DataFrame(hydro_new.columns)

for i in range(len(buses)):
    buses.iloc[i,0] = str(buses.iloc[i,0]) + str(Interconnection_ID)
hydro_new.columns = buses[0]

hydro_new.to_csv('New_files_new_IDs/nodal_hydro.csv',index=False)

#Changing nodal_load
nodal_load = pd.read_csv('nodal_load.csv', header=0)
nodal_load_new = nodal_load.copy()
buses = pd.DataFrame(nodal_load_new.columns)

for i in range(len(buses)):
    buses.iloc[i,0] = str(buses.iloc[i,0]) + str(Interconnection_ID)
nodal_load_new.columns = buses[0]

nodal_load_new.to_csv('New_files_new_IDs/nodal_load.csv',index=False)

#Changing nodal_solar
nodal_solar = pd.read_csv('nodal_solar.csv', header=0)
nodal_solar_new = nodal_solar.copy()
buses = pd.DataFrame(nodal_solar_new.columns)

for i in range(len(buses)):
    buses.iloc[i,0] = str(buses.iloc[i,0]) + str(Interconnection_ID)
nodal_solar_new.columns = buses[0]

nodal_solar_new.to_csv('New_files_new_IDs/nodal_solar.csv',index=False)

nodal_solar = pd.read_csv('nodal_solar2.csv', header=0)
nodal_solar_new = nodal_solar.copy()
buses = pd.DataFrame(nodal_solar_new.columns)

for i in range(len(buses)):
    buses.iloc[i,0] = str(buses.iloc[i,0]) + str(Interconnection_ID)
nodal_solar_new.columns = buses[0]

nodal_solar_new.to_csv('New_files_new_IDs/nodal_solar2.csv',index=False)

#Changing nodal_wind
nodal_wind = pd.read_csv('nodal_wind.csv', header=0)
nodal_wind_new = nodal_wind.copy()
buses = pd.DataFrame(nodal_wind_new.columns)

for i in range(len(buses)):
    buses.iloc[i,0] = str(buses.iloc[i,0]) + str(Interconnection_ID)
nodal_wind_new.columns = buses[0]

nodal_wind_new.to_csv('New_files_new_IDs/nodal_wind.csv',index=False)

nodal_wind = pd.read_csv('nodal_wind2.csv', header=0)
nodal_wind_new = nodal_wind.copy()
buses = pd.DataFrame(nodal_wind_new.columns)

for i in range(len(buses)):
    buses.iloc[i,0] = str(buses.iloc[i,0]) + str(Interconnection_ID)
nodal_wind_new.columns = buses[0]

nodal_wind_new.to_csv('New_files_new_IDs/nodal_wind2.csv',index=False)

