'''
    Đoạn này nhằm mục đích tạo ra một từ điển (dictionary) chứa thông tin về đường dẫn của các hình ảnh trong thư mục dữ liệu. từ điển này
    sẽ có cấu trúc phù hợp....
    Giải thích:
     1. Import: glob (để tìm tất cả các tệp hình ảnh trong thư mục), 'os'(để thao tác với hệ thống tệp) và json(để sử lý file json)
     2. create_dict_image_path(data_dir): Đây là hàm chính trực tiếp thực hiện việc tạo từ điển chứa thông rtin về đuòng dẫn của các hình ảnh
     3. dict_json_path: đây là từ điển chính mà chúng ta sẽ xây dựng để lưu thông tin về đường dẫn hình ảnh
     4. lặp qua các thư mục và hình ảnh:
        - đầu tiên vòng lập for key keyframe_dir in sorted(os.listdir(data_dir)) được sử dụng để duyệt qua từng thư mục chứa keyframe(C00_V00, C01_V00,..)
        - trong vòng lặp này chúng ta tạo một khóa cho từ điển theo định dạng C00_V00 và tạo ra một từ điển con trong keyframe(C00_V0000, C00_V0001,..)
        - Tiếp theo chúng ta lặp qua các thư mục con bên trong keyframe và lặp qua danh sách các hình ảnh
        - Mỗi hình ảnh được thêm vào từ điển con với khóa là một số nguyên thẻ hiện chỉ số của hình ảnh trong danh sách. chú ý rằng bạn cũng có thể sử dụng tên hình ảnh làm khóa
        nếu muốn(bạn có thể chọn cách này bằng cách bỏ dấu commment trước dòng tương ứng và bỏ cặp dấu comment ở dòng cuối cùng
        - cuối cùng một khóa total_image được thêm vào từ điển con để lưu tổng số lượng hình ảnh trong thư mục con
    5. Lưu dữ liệu vào file JSON
        - Sau khi tạo từ diển hoàn chỉnh chúng ta sử dụng hàm json.dump() để lưu vào file JSON có tên......
'''


from glob import glob
import os 
import json 


def create_dict_image_path(data_dir):
    dict_json_path = {}
    for keyframe_dir in sorted(os.listdir(data_dir)):
        keyframe_dir_path = os.path.join(data_dir, keyframe_dir)
        dict_json_path[keyframe_dir[-3:]] = {}

        for subdir in sorted(os.listdir(keyframe_dir_path)):
            if subdir not in dict_json_path:
                dict_json_path[keyframe_dir[-3:]][subdir] = {}

            subdir_path = os.path.join(keyframe_dir_path, subdir)
            list_image_path = glob(os.path.join(subdir_path, "*.jpg"))
            list_image_path.sort()
            # print(list_image_path)

            for index, image_path in enumerate(list_image_path):
                image_name = image_path.split("/")[-1]
                #dict_json_path[keyframe_dir[-7:]][subdir][int(index)] = image_name # id2img
                dict_json_path[keyframe_dir[-7:]][subdir][image_name] = index # img2id 
            
            dict_json_path[keyframe_dir[-3:]][subdir]["total_image"] = len(list_image_path)



    with open('/home/duy/Documents/Competition/Video-Text-Retrieval/dict/dict_img2id_path.json', 'w') as f:
        json.dump(dict_json_path, f)

    # with open('dict_image_path_img2id.json', 'w') as f:
    #     json.dump(dict_json_path, f)

    # Gọi hàm create_dict_image_path với đường dẫn thư mục dữ liệu


data_dir = '/home/duy/Documents/Competition/Video-Text-Retrieval/Database'
create_dict_image_path(data_dir)

