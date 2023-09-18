# mục đích mô phòng file keyframes_id.json của hùng an
import os
import json


def create_shot(data_dir):
    dict_json_path = {} # chưa cần quan tâm
    #list_shot_id = [] # chứa thông tin của list_shot_id(các id nằm trong cùng 1 shot)
    #list_shot_path = [] # chứa thông tin của list_shot_path(gồm shot_id và shot_path)
    # tin cậy
    dict_info = {} # gồm thông tin về image_path, list_shot_id, list_shot_path để append vào list_shot_path
    dict_shot_path = [] # Trùm cuối


    for keyframe_dir in sorted(os.listdir(data_dir)):
        keyframe_dir_path = os.path.join(data_dir, keyframe_dir)

        for subdir in sorted(os.listdir(keyframe_dir_path)):  
            subdir_path = os.path.join(keyframe_dir_path, subdir) 
            
            
            count_level_min = 1
            count_level_max = 6
            count = 1
            for subdir1 in sorted(os.listdir(subdir_path)):
                subdir1_path = os.path.join(subdir_path, subdir1)
                
                
                # Tạo ra các temporary list, dict
                tmp_shot_id = [] # 00000, 000001, 00002, 00003, 00004, 00005
                #tmp_shot_path = []   # database/keyframes/.../..., ....,....,....,....
                tmp_dict_sub = {}  # {"shot_id": "00000", "shot_path" = "database/keyframes/.../..." }
                tmp_list = [] # [{   }, {    }, {    }, {    }, {    }, {      }]
                count_shot = 1
                
                # 
                
                for tmp_subdir1 in sorted(os.listdir(subdir_path)):
                    tmp_subdir1_path = os.path.join(subdir_path, tmp_subdir1)
                                   
                    if count_shot <= count_level_max and count_shot >= count_level_min :
                        #tmp_shot_path.append(tmp_subdir1_path)       # image_path
                        tmp_shot_id.append(tmp_subdir1)              # list_shot_id
                        tmp_dict_sub = {                             # list_shot_path
                            'shot_id': tmp_subdir1,                      
                            'shot_path':tmp_subdir1_path
                        }
                        tmp_list.append(tmp_dict_sub)


                    count_shot += 1
                    if count_shot == count_level_min + 6: # vòng hình ảnh thứ 7 phải lớn hơn hoặc bằng min
                        #count_level_min += 6
                        #count_level_max += 6
                        count += 1
                        if count == count_level_max:
                            count_level_max += 6
                            count_level_min += 6
                        break
                    
                    
                    
                #mình đang cần thêm 1 cơ chế để đánh dấu khi count_shot =7 thì sẽ áp dụng thay đổi min và max
                   
                dict_info = {
                    'image_path': subdir1_path,
                    'list_shot_id': tmp_shot_id,
                    'list_shot_path': tmp_list

                }
                dict_shot_path.append(dict_info)


                

    
    
    dict_json_path = {int(idx):info for idx, info in enumerate(dict_shot_path)}
    

    with open('/home/duy/Documents/Competition/Video-Text-Retrieval/dict/keyframes_id.json', 'w') as f:
        json.dump(dict_json_path, f)  
        
data_dir = '/home/duy/Documents/Competition/Video-Text-Retrieval/Database'  
create_shot(data_dir)