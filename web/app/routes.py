import os
import subprocess

from flask import render_template, request

from web.app import app


@app.route('/', methods=['GET'])
def index():
    return 'Hello World! Welcome to Face Aging!'


@app.route('/upload')
def upload_file():
    return render_template('upload.html')


@app.route('/generate', methods=['POST'])
def generate():
    upload_folder = 'C:/Users/yorky/Desktop/STUDY/Python/interesting_project/Lifespan_Age_Transformation_Synthesis/datasets'
    image_list_dir = 'C:/Users/yorky/Desktop/STUDY/Python/interesting_project/Lifespan_Age_Transformation_Synthesis'

    fList = request.files.getlist('files')
    sex = request.form.get('sex')

    folder_path = upload_folder + f'/{sex}'
    image_list_path = image_list_dir + f'/{sex}_image_list.txt'

    initialize(folder_path)
    test_order = dir_sum(folder_path) + 1

    folder_path = folder_path + f'/test_{test_order}'
    os.makedirs(folder_path)

    with open(image_list_path, 'w') as image_list_file:
        for idx, file in enumerate(fList):
            # 获取文件拓展名
            file_extension = os.path.splitext(file.filename)[1]

            # 生成文件路径
            image_saving_path = folder_path + f'/Img_{str(idx)}{file_extension}'
            image_path = f'datasets/{sex}/test_{test_order}/Img_{str(idx)}{file_extension}'

            # 写入 image_list_file 中
            image_list_file.write(image_path + '\n')
            # 保存图片
            file.save(image_saving_path)
            print(idx)

    return 'done'


def start():
    batch_file_path = 'C:/Users/yorky/Desktop/STUDY/Python/interesting_project/Lifespan_Age_Transformation_Synthesis/run_scripts/in_the_wild.bat'

    process = subprocess.Popen(batch_file_path, shell=True)
    process.wait()

    if process.returncode == 0:
        return 'Done!'
    else:
        return 'Error!'


def initialize(upload_folder):
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)


def dir_sum(folder_path):
    try:
        item_list = os.listdir(folder_path)
        folder_count = 0

        for item in item_list:
            item_path = os.path.join(folder_path, item)
            if os.path.isdir(item_path):
                folder_count += 1

        return folder_count

    except Exception as e:
        print("An error occurred:", e)
        return None
