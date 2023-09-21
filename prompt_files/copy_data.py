#Copy all succeed data (100-249,300-355)
#9.18 
import json
import shutil
import os
class filter_succeed():
     def __init__(self) -> None:
        failed=[]
        with open('/shared/liushuai/OmniGibson/prompt_files/finished_task.json',"r")as f:
            data=json.load(f)
        path='/shared/liushuai/OmniGibson/prompt_files/data'
        tar_basepath='/shared/liushuai/OmniGibson/prompt_files/failed'
        doublecheck=[]
        for ele in data.keys():
            if data[ele]=="failed":
                succeed_data=os.path.join(path,ele)
                tar_path=os.path.join(tar_basepath,ele)
                doublecheck.append(ele)
                shutil.copytree(succeed_data,tar_path)

        with open('/shared/liushuai/OmniGibson/prompt_files/finished_task100-249,300-355.json',"r")as f:
            data2=json.load(f)
        path100_149='/shared/liushuai/OmniGibson/prompt_files/data100-149'
        tar_basepath='/shared/liushuai/OmniGibson/prompt_files/failed'
        for ele in data2.keys():
            try:
                if data2[ele]=="failed":
                        succeed_data=os.path.join(path100_149,ele)
                        tar_path=os.path.join(tar_basepath,ele)
                        shutil.copytree(succeed_data,tar_path)
                        doublecheck.append(ele)
            except:
                failed.append(ele)
                pass
errordict={}
failedlist=[]
def filter_error():
    with open("/shared/liushuai/OmniGibson/prompt_files/finished_task.json",'r')as f:
        file=json.load(f)
        for ele in file.keys():
            if file[ele]=="error":
                errordict.update({ele:"error"})

    with open("/shared/liushuai/OmniGibson/prompt_files/finished_task100-249,300-355.json",'r')as f:
        file2=json.load(f)
        for ele in file2.keys():
            if file2[ele]=="error":
                if ele in errordict.keys():
                    failedlist.append(ele)
                errordict.update({ele:"error"})

    with open("/shared/liushuai/OmniGibson/prompt_files/error_choiszt.json","w")as f:
        f.write(json.dumps(errordict))

errordict={}
failedlist=[]
def filter_failed():
    with open("/shared/liushuai/OmniGibson/prompt_files/finished_task.json",'r')as f:
        file=json.load(f)
        for ele in file.keys():
            if file[ele]=="failed":
                errordict.update({ele:"failed"})

    with open("/shared/liushuai/OmniGibson/prompt_files/finished_task100-249,300-355.json",'r')as f:
        file2=json.load(f)
        for ele in file2.keys():
            if file2[ele]=="failed":
                if ele in errordict.keys():
                    failedlist.append(ele)
                errordict.update({ele:"failed"})


dyh_error={
    "put_keg_and_credit_card_on_checkout_desk": "error",
    "put_box_of_chocolates_and_money_on_checkout_desk": "error",
    "put_bag_of_cocoa_and_money_on_checkout_desk": "error",
    "put_a_water_bottle_on_the_floor": "error",
    "put_a_plate_into_dishwasher": "error",
    "put_a_tablefork_into_dishwasher": "error",
    "turn_off_coffee_machine_and_put_mug_into_diswasher": "error",
    "collecting_nuts_with_bucket": "error",
    "put_a_clove_in_the_pan_and_cook_it": "error",
    "cook_a_crab_and_put_it_in_the_steamer": "error",
    "cook_a_pumpkin": "error",
    "cook_chips": "error",
    "put_a_prawn_in_the_pan_and_cook_it": "error",
    "cook_spinach": "error",
    "cooking_bread_slice": "error",
    "put_a_tissue_into_bin": "error",
    "put_a_water_bottle_into_bin": "error",
    "put_water_glass_in_the_bin": "error",
    "fold_a_bath_towel": "error",
    "fold_a_bath_towel_and_put_it_into_hamper": "error",
    "fold_a_rag_and_put_it_into_hamper": "error",
    "fold_a_towl_and_put_it_in_the_basket": "error",
    "fold_tortillas": "error",
    "put_an_apple_in_the_bowl": "error",
    "put_bar_soap_on_the_sink": "error",
    "put_basket_on_the_floor": "error",
    "put_bok_choy_in_the_frying_pan": "error",
    "put_bottle_of_aspirin_in_plastic_bag": "error",
    "put_carton_of_milk_in_plastic_bag": "error",
    "put_chinese_anise_in_the_wok": "error",
    "put_fertilizer_atomizer_on_checkout_desk": "error",
    "put_firewood_on_fireplace": "error",
    "put_first-aid_kit_on_checkout_desk": "error",
    "put_ice_cube_into_mug": "error",
    "put_ice_cube_into_water_glass": "error",
    "put_lettuce_in_plastic_bag": "error"
}
dyh_failed={
    "put_kabob_in_the_tupperware_and_put_it_in_the_fridge": "failed",  
    "put_candlestick_and_money_on_checkout_desk": "failed",
    "put_money_and_air_conditioner_on_checkout_desk": "failed",
    "put_pack_of_pasta_and_money_on_cash_register": "failed",
    "put_pencil_and_money_on_checkout_desk": "failed",
    "cook_a_carrot": "failed",
    "cook_a_dumpling": "failed",
    "heat_a_pie_after_unfreeze_it": "failed",
    "cook_a_prawn_and_place_on_plate_with_butter": "failed",
    "cook_asparagus": "failed",
    "cook_bacon": "failed",
    "cook_bell_pepper": "failed",
    "cook_brussels_sprouts_and_a_broccoli": "failed",
    "cook_clove_and_place_on_plate_with_butter": "failed",
    "cook_fruitcake": "failed",
    "put_ham_hocks_in_stockpot_and_cook_it": "failed",
    "cook_kale": "failed",
    "cook_kielbasa": "failed",
    "thaw_and_heat_lasagna": "failed",
    "cook_lasagne": "failed",
    "cook_mustard": "failed",
    "put_huitre_on_stockpot_and_cook_it": "failed",
    "cook_quail": "failed",
    "put_a_pan_and_a_can_of_soda_in_the_ashcan": "failed",
    "fold_a_rag": "failed",
    "fold_a_tortilla_and_put_it_on_plate": "failed",
    "put_a_wire_into_vehicle": "failed",
    "put_bottle__of__apple_juice_in_plastic_bag": "failed",
    "put_bratwurst_in_the_tupperware_and_put_it_in_carton": "failed"
}
for ele in dyh_error.keys():
    if ele not in errordict:
        errordict.update({ele:dyh_error[ele]})
        
for ele in dyh_failed.keys():
    if ele not in errordict:
        errordict.update({ele:dyh_failed[ele]})

    with open("/shared/liushuai/OmniGibson/prompt_files/failed_merged.json","w")as f:
        f.write(json.dumps(errordict))

result={}    
with open("/shared/liushuai/OmniGibson/EVLM_Task/all_400.json","r")as f:
    data=json.load(f)
with open("/shared/liushuai/OmniGibson/prompt_files/919TODO/all_failed.json","r")as f:
    cho=json.load(f)
with open("/shared/liushuai/OmniGibson/prompt_files/919TODO/failed_todo.json","a+")as f:
    for ele in data.keys():
        if data[ele]['detailed_name'] in cho.keys():
            result.update({ele:data[ele]})

    f.write(json.dumps(result))