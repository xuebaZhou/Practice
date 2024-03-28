# import json
#
# # 读取 JSON 文件
# with open("C://Users/周奕兵/Desktop/generic_qa copy.json", 'r', encoding='utf-8') as f:
#     data = json.load(f)
#
# # 遍历数据列表
# for item in data:
#     # 根据video_name的值进行修改
#     if "video_name" in item:
#         item["User"] = item["Q"] #将"Q"键的值赋给新键"User"
#         item["Assistant"] = item["A"]
#         del item["Q"]#移除原始的"Q"键
#         del item["A"]
#         del item["video_name"]
# # 将修改后的 JSON 数据存入新的文件中
# with open("C://Users/周奕兵/Desktop/formatted - 副本.json", 'w') as f:
#     json.dump(data, f, indent=4)
#

import json

# 读取原始JSON文件
with open("C://Users/周奕兵/Desktop/motif_mix_fixed.json", 'r', encoding='utf-8') as f:
    data = json.load(f)

# 转换数据格式
transformed_data = []
for item in data:
    user_key = "User"
    assistant_key = "Assistant"
    user_value = ""
    assistant_value = ""
    for conv in item["conversations"]:
        if conv["from"] == "human":
            user_value = conv["value"]
        elif conv["from"] == "gpt":
            assistant_value = conv["value"]
    transformed_data.append({user_key: user_value, assistant_key: assistant_value})
# 写入新的JSON文件
with open("C://Users/周奕兵/Desktop/formatted1.json", 'w') as f:
    json.dump(transformed_data, f, indent=4)
