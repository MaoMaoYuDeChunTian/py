po_file = r"E:\Git_Work\avatar\editor\translations\zh_CN.po"
append_file = r"C:\Users\Administrator\Desktop\avatar-translate (3).txt"
save_file = "./merge.po"

exists_translation = {}

last_key = None
last_id = None
for line in open(po_file, encoding='utf-8'):
    if '#~' in line or '#:' in line:
        key = line.strip()
        key = key[2:]
        key = key.strip()
        if key not in exists_translation.keys():
            exists_translation[key] = {}
            last_key = key
        else: 
            last_key = key
    else:
        if 'msgid' in line:
            last_id = line.strip()
        elif 'msgstr' in line and last_key is not None:
            exists_translation[last_key][last_id] = line.strip()


exists = False
for line in open(append_file, encoding='utf-8'):
    if '#~' in line:
        key = line.strip()
        key = key[2:]
        key = key.strip()
        if key in exists_translation.keys():
            last_key = key
        else:
            exists_translation[key] = {}
            last_key = key
    else:
        if 'msgid' in line:
            last_id = line.strip()
            if last_id not in exists_translation[last_key].keys():
                exists = False
            else:
                exists = True
        elif 'msgstr' in line:
            if not exists:
                exists_translation[last_key][last_id] = line.strip()

'''
for key, value in exists_translation.items():
    print(key)
    for item_key, item_value in value.items():
        print(f'{item_key} -> {item_value}')
    print()
'''    
with open(save_file,'w',encoding='utf-8') as mf:
    for key, value in exists_translation.items():
        print(key)
        mf.write("\n\n#~ "+key+"\n")
        for item_key, item_value in value.items():
            mf.write(item_key+"\n")
            mf.write(item_value+"\n")
            mf.write("\n")

        

