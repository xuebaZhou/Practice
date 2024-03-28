#
# import json
# import jsonlines
# # 假设您的原始JSON数据存储在名为'data.json'的文件中
# with open("C:/Users/周奕兵/Desktop/formatted - 副本.json", 'r',encoding='utf-8') as file:
#     data = json.load(file)
# # 创建一个新的JSONL文件用于存储转换后的数据
# with jsonlines.open("C:/Users/周奕兵/Desktop/sample.jsonl", mode='w') as writer:
#     for item in data:
#         # 根据要求进行修改
#         if "User" in item and "Assistant" in item:
#             text = f'User: {item["User"]}\n\nAssistant: {item["Assistant"]}'
#             modified_item = {"text": text}
#             writer.write(modified_item)


import json
import jsonlines

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

# 创建一个新的JSONL文件用于存储转换后的数据
with jsonlines.open("C:/Users/周奕兵/Desktop/sample.jsonl", mode='w') as writer:
    for item in transformed_data:
        # 根据要求进行修改
        if "User" in item and "Assistant" in item:
            text = f'User: {item["User"]}\n\nAssistant: {item["Assistant"]}'
            modified_item = {"text": text}
            writer.write(modified_item)
