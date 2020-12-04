# author: join
# time: 12/3/2020

import os
import shutil
from shutil import copyfile

import_path = ""
material_path_list = []
import_search_names = []


# 去除.jpg.import文件中的path路径
def change_import_file_content(import_file_path, target_file_path):
    if not os.path.isfile(import_file_path):
        return False

    material_path_list.append(target_file_path)
    with open(import_file_path, 'r+', encoding='utf-8') as source_f, open(target_file_path, 'w+',
                                                                          encoding='utf-8') as target_f:
        for line in source_f.readlines():
            # text = line.strip()
            if line.find('path.s3tc') != -1:
                line = 'path=""\n'

            if line.find('path.etc2') != -1:
                line = '\n'

            target_f.write(line)

    return True


# 拷贝资源文件下的.jpg.import文件
def copy_import_file(source_dir, target_dir):
    files = os.listdir(source_dir)
    for name in files:
        file_path = os.path.join(source_dir, name)
        jpg_import = file_path.find('.jpg.import') != -1
        jpg_import_up = file_path.find('.JPG.import') != -1
        png_import = file_path.find('.png.import') != -1
        png_import_up = file_path.find('.PNG.import') != -1
        if not jpg_import and not png_import and not jpg_import_up and not png_import_up:
            continue

        new_file_name = ""
        if jpg_import:
            new_file_name = name.replace('.jpg.import', '.stex.import')
        if png_import:
            new_file_name = name.replace('.png.import', '.stex.import')
        if jpg_import_up:
            new_file_name = name.replace('.JPG.import', '.stex.import')
        if png_import_up:
            new_file_name = name.replace('.PNG.import', '.stex.import')

        if not change_import_file_content(file_path, os.path.join(target_dir, new_file_name)):
            print('copy' + file_path + 'fail')


# 文件拷贝操作
def copy_file(source_path, target_path):
    try:
        copyfile(source_path, target_path)
    except IOError as e:
        print("Unable to copy file. %s" % e)
        exit(1)


# 创建文件夹并拷贝需要的文件
def create_dir(source_path, target_name):
    if os.path.exists(target_name):
        shutil.rmtree(target_name)

    if not os.path.isdir(source_path):
        print("data to express is not find!")
        return False

    material_path_list.clear()  # 用于存储需要寻找的.stex文件路径

    files = os.listdir(source_path)
    for file in files:
        source_type_path = os.path.join(source_path, file)
        target_type_path = os.path.join(target_name, file)
        # 玻璃等需要提前创建文件夹
        if not os.path.isdir(target_type_path):
            os.makedirs(target_type_path)

        files1 = os.listdir(source_type_path)
        for file1 in files1:
            source_material_path = os.path.join(source_type_path, file1)
            target_material_file_path = os.path.join(target_type_path, file1)
            target_material_path = os.path.join(target_type_path, 'texture')
            target_material_path = os.path.join(target_material_path, file1)

            if os.path.isdir(source_material_path):
                os.makedirs(target_material_path)
                copy_import_file(source_material_path, target_material_path)
            elif file1.find('.material') and file1.find('.import') == -1:
                copy_file(source_material_path, target_material_file_path)


# 根据名称获取.import中的对应的.s3tc.stex
def get_source_name(target_name):
    for name in import_search_names:
        if name.find('.s3tc.stex') != -1:
            if name.find(target_name) != -1:
                return name

    return ""


# 查找并拷贝对应.stex文件到指定文件夹
def search_stex_from_import():
    for path in material_path_list:
        base_name = os.path.basename(path)
        base_name = base_name.replace('.stex.import', '')
        target_path = os.path.dirname(path)
        target_name = base_name + '.stex'

        find_name = get_source_name(base_name)
        if find_name:
            copy_file(os.path.join(import_path, find_name), os.path.join(target_path, target_name))


# 获取import_path所有的文件名称
def find_import_names():
    global import_search_names
    import_search_names.clear()
    if not os.path.isdir(import_path):
        print(import_path + 'not find')
    import_search_names = os.listdir(import_path)


def main():
    global import_path
    import_path = input('origin data path:')
    if not import_path:
        import_path = 'E:/material_train/demo/.import'
    
    create_dir('E:/material_train/demo/材质库', '材质库')
    find_import_names()
    search_stex_from_import()


if __name__ == '__main__':
    main()
