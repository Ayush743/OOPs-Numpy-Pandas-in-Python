
import numpy as np
from random import randint as rd
# customer_name=np.array([
#     "Optimus Prime",
#     "Alpha Trion",
#     "Vector Prime",
#     "Solus Prime",
#     "Onyx Prime",
#     "Megatronus (The Fallen)",
#     "Micronus Prime"
#     "Megatron",
#     "Bumblebee",
#     "Arcee",
#     "Ratchet",
#     "Bulkhead",
#     "Wheeljack",
#     "Starscream",
#     "Soundwave",
#     "Knock Out",
#     "Shockwave",
#     "Grimlock",
#     "Blackarachnia",
#     "Ultra Magnus",
#     " Arcadius Prime",
#     np.nan,
#     np.nan,
#     np.nan,
#     np.nan
# ])
r_list=np.array([2,4,5,6,3,53,43,43,np.nan,np.nan,np.nan])
missing_values=np.isnan(r_list)
print(sum(missing_values))
print(np.nan_to_num(r_list))
print(np.nanmean(r_list))
print(np.nanmedian(r_list))

np_mean_data=np.where(np.isnan(r_list),np.nanmean(r_list),r_list)
print(np_mean_data)

data_without_nan=r_list[~np.isnan(r_list)]
print(data_without_nan)

#_____----------Roll function------->
test_data=np.array([1,2,3,4,np.nan,6,7])
mask=np.isnan(test_data)
test_data[mask]=np.roll(test_data,shift=1)[mask]
print(test_data)