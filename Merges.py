#%% Importing the pandas for data manipulating
import pandas as pd

# %%  Setting the path where all the boiler datasets you want to merge are located. Load them and assign them to variables
pathB = "C:/Bansal Data/Drishti Data/Self/iCode/Projects/AI project/Merged data/Boiler/boiler_217.csv"
pathB1 = "C:/Bansal Data/Drishti Data/Self/iCode/Projects/AI project/Merged data/Boiler/boiler_226.csv"
pathB2 = "C:/Bansal Data/Drishti Data/Self/iCode/Projects/AI project/Merged data/Boiler/boiler_233.csv"

#%% Reading them 
PathB = pd.read_csv(pathB)
PathB1 = pd.read_csv(pathB1)
PathB2 = pd.read_csv(pathB2)

#%% Concatening the datasets
df = pd.concat([PathB, PathB1, PathB2], ignore_index = True)

#%% Exporting the dataset as an output
df.to_csv("C:/Bansal Data/Drishti Data/Self/iCode/Projects/AI project/Merged data/Boiler/Merged data for boilers.csv")
#===============================================================================================================================

# %%  Setting the path where all the coffee datasets you want to merge are located. Load them and assign them to variables
pathC = "C:/Bansal Data/Drishti Data/Self/iCode/Projects/AI project/Merged data/Coffee/coffee_37.csv"
pathC1 = "C:/Bansal Data/Drishti Data/Self/iCode/Projects/AI project/Merged data/Coffee/coffee_54.csv"
pathC2 = "C:/Bansal Data/Drishti Data/Self/iCode/Projects/AI project/Merged data/Coffee/coffee_97.csv"

#%% Reading them 
PathC = pd.read_csv(pathC)
PathC1 = pd.read_csv(pathC1)
PathC2 = pd.read_csv(pathC2)

#%% Concatening the datasets
df = pd.concat([PathC, PathC1, PathC2], ignore_index = True)

#%% Exporting the dataset as an output
df.to_csv("C:/Bansal Data/Drishti Data/Self/iCode/Projects/AI project/Merged data/Coffee/Merged data for coffee.csv")
#===============================================================================================================================
# %%  Setting the path where all the fridge datasets you want to merge are located. Load them and assign them to variables
pathF = "C:/Bansal Data/Drishti Data/Self/iCode/Projects/AI project/Merged data/Fridge/fridge_98.csv"
pathF1 = "C:/Bansal Data/Drishti Data/Self/iCode/Projects/AI project/Merged data/Fridge/fridge_207.csv"
pathF2 = "C:/Bansal Data/Drishti Data/Self/iCode/Projects/AI project/Merged data/Fridge/fridge_284.csv"
pathF3 = "C:/Bansal Data/Drishti Data/Self/iCode/Projects/AI project/Merged data/Fridge/fridge_317.csv"

#%% Reading them 
PathF = pd.read_csv(pathF)
PathF1 = pd.read_csv(pathF1)
PathF2 = pd.read_csv(pathF2)
PathF3 = pd.read_csv(pathF3)

#%% Concatening the datasets
df = pd.concat([PathF, PathF1, PathF2, PathF3], ignore_index = True)

#%% Exporting the dataset as an output
df.to_csv("C:/Bansal Data/Drishti Data/Self/iCode/Projects/AI project/Merged data/Fridge/Merged data for fridge.csv")
#===============================================================================================================================

# %%  Setting the path where all the washine machine datasets you want to merge are located. Load them and assign them to variables
pathW = "C:/Bansal Data/Drishti Data/Self/iCode/Projects/AI project/Merged data/Washing machine/washing_machine_32.csv"
pathW1 = "C:/Bansal Data/Drishti Data/Self/iCode/Projects/AI project/Merged data/Washing machine/washing_machine_52.csv"
pathW2 = "C:/Bansal Data/Drishti Data/Self/iCode/Projects/AI project/Merged data/Washing machine/washing_machine_135.csv"
pathW3 = "C:/Bansal Data/Drishti Data/Self/iCode/Projects/AI project/Merged data/Washing machine/washing_machine_157.csv"
pathW4 = "C:/Bansal Data/Drishti Data/Self/iCode/Projects/AI project/Merged data/Washing machine/washing_machine_218.csv"
pathW5 = "C:/Bansal Data/Drishti Data/Self/iCode/Projects/AI project/Merged data/Washing machine/washing_machine_343.csv"

#%% Reading them 
PathW = pd.read_csv(pathW)
PathW1 = pd.read_csv(pathW1)
PathW2 = pd.read_csv(pathW2)
PathW3 = pd.read_csv(pathW3)
PathW4 = pd.read_csv(pathW4)
PathW5 = pd.read_csv(pathW5)

#%% Concatening the datasets
df = pd.concat([PathW, PathW1, PathW2, PathW3,PathW4, PathW5], ignore_index = True)

#%% Exporting the dataset as an output
df.to_csv("C:/Bansal Data/Drishti Data/Self/iCode/Projects/AI project/Merged data/Washing machine/Merged data for washing_machine.csv")
#===============================================================================================================================

# %%  Setting the path where all the Internet router datasets you want to merge are located. Load them and assign them to variables
pathI = "C:/Bansal Data/Drishti Data/Self/iCode/Projects/AI project/Merged data/Internet router/internet_router_131.csv"
pathI1 = "C:/Bansal Data/Drishti Data/Self/iCode/Projects/AI project/Merged data/Internet router/internet_router_295.csv"

#%% Reading them 
PathI = pd.read_csv(pathI)
PathI1 = pd.read_csv(pathI1)

#%% Concatening the datasets
df = pd.concat([PathI, PathI1], ignore_index = True)

#%% Exporting the dataset as an output
df.to_csv("C:/Bansal Data/Drishti Data/Self/iCode/Projects/AI project/Merged data/Internet router/Merged data for internet router.csv")
#===============================================================================================================================

# %%  Setting the path where all the laptop datasets you want to merge are located. Load them and assign them to variables
pathL = "C:/Bansal Data/Drishti Data/Self/iCode/Projects/AI project/Merged data/Laptop/laptop_64.csv"
pathL1 = "C:/Bansal Data/Drishti Data/Self/iCode/Projects/AI project/Merged data/Laptop/laptop_289.csv"

#%% Reading them 
PathL = pd.read_csv(pathL)
PathL1 = pd.read_csv(pathL1)

#%% Concatening the datasets
df = pd.concat([PathL, PathL1], ignore_index = True)

#%% Exporting the dataset as an output
df.to_csv("C:/Bansal Data/Drishti Data/Self/iCode/Projects/AI project/Merged data/Laptop/Merged data for laptop.csv")
#===============================================================================================================================

# %%  Setting the path where all the screen datasets you want to merge are located. Load them and assign them to variables
pathS = "C:/Bansal Data/Drishti Data/Self/iCode/Projects/AI project/Merged data/Screen/screen_146.csv"
pathS1 = "C:/Bansal Data/Drishti Data/Self/iCode/Projects/AI project/Merged data/Screen/screen_302.csv"

#%% Reading them 
PathS = pd.read_csv(pathS)
PathS1 = pd.read_csv(pathS1)

#%% Concatening the datasets
df = pd.concat([PathS, PathS1], ignore_index = True)

#%% Exporting the dataset as an output
df.to_csv("C:/Bansal Data/Drishti Data/Self/iCode/Projects/AI project/Merged data/Screen/Merged data for screen.csv")
#===============================================================================================================================

# %%  Setting the path where all the microwave datasets you want to merge are located. Load them and assign them to variables
pathM = "C:/Bansal Data/Drishti Data/Self/iCode/Projects/AI project/Merged data/Microwave/micro_wave_oven_147.csv"
pathM1 = "C:/Bansal Data/Drishti Data/Self/iCode/Projects/AI project/Merged data/Microwave/micro_wave_oven_314.csv"

#%% Reading them 
PathM = pd.read_csv(pathM)
PathM1 = pd.read_csv(pathM1)

#%% Concatening the datasets
df = pd.concat([PathM, PathM1], ignore_index = True)

#%% Exporting the dataset as an output
df.to_csv("C:/Bansal Data/Drishti Data/Self/iCode/Projects/AI project/Merged data/Microwave/Merged data for microwave.csv")
#===============================================================================================================================

# %%  Setting the path where all the deumidifer datasets you want to merge are located. Load them and assign them to variables
pathD = "C:/Bansal Data/Drishti Data/Self/iCode/Projects/AI project/Merged data/Dehumidifier/dehumidifier_310.csv"
pathD1 = "C:/Bansal Data/Drishti Data/Self/iCode/Projects/AI project/Merged data/Dehumidifier/dehumidifier_322.csv"

#%% Reading them 
PathD = pd.read_csv(pathD)
PathD1 = pd.read_csv(pathD1)

#%% Concatening the datasets
df = pd.concat([PathD, PathD1], ignore_index = True)

#%% Exporting the dataset as an output
df.to_csv("C:/Bansal Data/Drishti Data/Self/iCode/Projects/AI project/Merged data/Dehumidifier/Merged data for dehumidifier.csv")
#===============================================================================================================================

# %%  Setting the path where all the vacuum datasets you want to merge are located. Load them and assign them to variables
pathV = "C:/Bansal Data/Drishti Data/Self/iCode/Projects/AI project/Merged data/Vacuum/vacuum_236.csv"
pathV1 = "C:/Bansal Data/Drishti Data/Self/iCode/Projects/AI project/Merged data/Vacuum/vacuum_254.csv"

#%% Reading them 
PathV = pd.read_csv(pathV)
PathV1 = pd.read_csv(pathV1)

#%% Concatening the datasets
df = pd.concat([PathV, PathV1], ignore_index = True)

#%% Exporting the dataset as an output
df.to_csv("C:/Bansal Data/Drishti Data/Self/iCode/Projects/AI project/Merged data/Vacuum/Merged data for vacuum.csv")
#===============================================================================================================================

# %% Merging the appliance for EDA for all.
# %%  Setting the path where all the vacuum datasets you want to merge are located. Load them and assign them to variables
path_0 = "C:/Bansal Data/Drishti Data/Self/iCode/Projects/AI project/Merged data/Boiler/boiler_226.csv"
path_0["Appliance"] = path_0["Boiler"]
path_0.head(3)
#pathV1 = "C:/Bansal Data/Drishti Data/Self/iCode/Projects/AI project/Merged data/Vacuum/vacuum_254.csv"

#%% Reading them 
PathV = pd.read_csv(pathV)
PathV1 = pd.read_csv(pathV1)

#%% Concatening the datasets
df = pd.concat([PathV, PathV1], ignore_index = True)

#%% Exporting the dataset as an output
df.to_csv("C:/Bansal Data/Drishti Data/Self/iCode/Projects/AI project/Merged data/Merged data for All.csv")
#===============================================================================================================================
