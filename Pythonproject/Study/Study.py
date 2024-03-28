import json

# 打开原始JSON文件
with open("C://Users/周奕兵/Desktop/motif_mix_fixed.json", 'r', encoding='utf-8') as file:
    data = json.load(file)
new_data = []
for item in data:
    # 获取id和conversations
    id = item['id']
    conversations = item['conversations']
    # 将对话分成问题和回答两个部分，并添加相应的标记
    new_conversations = []
    for i in range(len(conversations)):
        if i % 2 == 0:
             # new_conversations.append("User"+":"+'"{}"'.format(conversations[i]['value'])+"\n\n")
             new_conversations.append({"User": conversations[i]['value']+"\n\n"})
        else:
             new_conversations.append({"Assistant": conversations[i]['value'] + "\n\n"})
            # new_conversations.append('"Assistant": "{}"'.format(conversations[i]['value'])+"\n\n")

    # 构建新的数据对象
    new_item = {
        "id": id,
        "conversations": new_conversations
    }
    # 添加到新数据列表中
    new_data.append(new_item)
# 将新的JSON数据写入新的文件
with open("C://Users/周奕兵/Desktop/formatted.json", 'w') as file:
    json.dump(new_data, file, indent=4)



