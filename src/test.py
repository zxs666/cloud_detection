import numpy as np

######## Search function example ###########

test_dic = {"date0": np.matrix([[0,0],[np.nan, np.nan]]), "date1": np.full((3, 3), 1, int),
            "date2":  np.full((3, 3), np.nan), "date3": np.full((3,3), 3, int), "date4": np.matrix([[np.nan,2],[3,4]])}

key_result = [key for key, value in test_dic.items() if key not in "date3"]
value_result = [value for key, value in test_dic.items() if key not in "date3"]
# extract all keys and values except the given one

pixel_values = [value[0,0] for value in value_result]
# extract a given row and column from the list

NA_values = np.isnan(pixel_values).tolist() # boolean list with True where np.nan
notNA_values = [not i for i in NA_values] # boolean list with True where different to np.nan

indices_notNA_values = [index for index, value in enumerate(notNA_values) if value == True]
# list of indices of the given list where the value is different from NA

index_reference_value = indices_notNA_values[-1]
# extracts the last value of the list, this will be the most recent not NA value we were looking for

reference_value= pixel_values[index_reference_value]
reference_date = key_result[index_reference_value]

###################################################################

np.savetxt("cloud_mask.csv", cloud_mask_array, delimiter=",")
