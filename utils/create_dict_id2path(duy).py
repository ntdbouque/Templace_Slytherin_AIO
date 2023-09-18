from glob import glob
import os 
import json 



data_dir = '/home/duy/Documents/Competition/Video-Text-Retrieval/Database'

def create_dict_image_path(data_dir):
    dict_json_path = {}
    list_image_path = []

    for keyframe_dir in sorted(os.listdir(data_dir)):
        keyframe_dir_path = os.path.join(data_dir, keyframe_dir)
        
        for subdir in sorted(os.listdir(keyframe_dir_path)):            
            subdir_path = os.path.join(keyframe_dir_path, subdir)
            #list_image_path = glob(os.path.join(subdir_path, "*.jpg"))
            #list_image_path.sort()
            
            for subdir1 in sorted(os.listdir(subdir_path)):
                subdir1_path = os.path.join(subdir_path, subdir1)
                list_image_path.append(subdir1_path)
    
    #dict_json_path = {idx: path for idx, path in enumerate(list_image_path)}
    dict_json_path = {path: idx for idx, path in enumerate(list_image_path)}
    with open('/home/duy/Documents/Competition/Video-Text-Retrieval/dictDuy/keyframe_path2id.json', 'w') as f:
        json.dump(dict_json_path, f)  
                
create_dict_image_path(data_dir)