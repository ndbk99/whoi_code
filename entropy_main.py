# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 16:37:23 2021

@author: ndbke

"""


import xarray as xr
from utils.entropy import entropy_all




#%%


# read in volumetric T-S files
dat_grn = xr.open_dataset('NetCDFs/tsv_grn.nc', decode_times=False, autoclose=True)
dat_arc = xr.open_dataset('NetCDFs/tsv_arc.nc', decode_times=False, autoclose=True)

# entropy calcs for entirety of Greenland Sea and Arctic Ocean
print("grn")
entropy_all(dat_grn.volume,True)
print("arc")
entropy_all(dat_arc.volume,True)

# condition to get Greenland deep water vs. upper water
cond = (dat_grn.temperature >= -1.5) & (dat_grn.temperature < 0) & (dat_grn.salinity >= 34.85) & (dat_grn.salinity < 34.95)
deep = dat_grn.where(cond)
upper = dat_grn.where(~cond)

# entropy calcs for Greenland deep vs upper
print("grn - deep")
deep_H_T, deep_H_S, deep_H_TS = entropy_all(deep.volume)
print("grn - upper")
upper_H_T, upper_H_S, upper_H_TS = entropy_all(upper.volume)


# close NC files
dat_grn.close()
dat_arc.close()






#%%


# print("\t\t\t\tH(T)/H(S)\t\t J(T,S)\n\t\t\t\t--------\t\t-------")
# print("upper water:\t", np.round(upper_H_T / upper_H_S,3), "\t\t\t", upper_H_TS)
# print("deep water:  \t",np.round(deep_H_T / deep_H_S,3), "\t\t\t", deep_H_TS)