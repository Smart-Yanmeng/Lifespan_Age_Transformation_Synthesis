import os
import subprocess
import zipfile

from flask import render_template, request, send_from_directory, send_file

from web.app import app


# 初页面
@app.route('/', methods=['GET'])
def index():
    return 'Hello World! Welcome to Face Aging!'


# 上传文件页面
@app.route('/upload')
def upload_file():
    return render_template('upload.html')


# 生成计算
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

    files_arr = []

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

            # 生成要下载的文件目录
            files_arr.append(f'Img_{str(idx)}.mp4')

    if sex == 'male':
        batch_file_path = "C:/Users/yorky/Desktop/STUDY/Python/interesting_project/Lifespan_Age_Transformation_Synthesis/web/start_scripts/males_model_starts.bat"
        video_path = "C:/Users/yorky/Desktop/STUDY/Python/interesting_project/Lifespan_Age_Transformation_Synthesis/results/males_model/test_latest/traversal/"
    else:
        batch_file_path = "C:/Users/yorky/Desktop/STUDY/Python/interesting_project/Lifespan_Age_Transformation_Synthesis/web/start_scripts/females_model_starts.bat"
        video_path = "C:/Users/yorky/Desktop/STUDY/Python/interesting_project/Lifespan_Age_Transformation_Synthesis/results/females_model/test_latest/traversal/"

    video_generate_path = 'C:/Users/yorky/Desktop/STUDY/Python/interesting_project/Lifespan_Age_Transformation_Synthesis/web/result_files.zip'

    if start(batch_file_path):
        return download_zip_files(video_path, files_arr, video_generate_path)
    else:
        return 'Error!'


# 开始运算
def start(batch_file_path):
    process = subprocess.Popen(batch_file_path, shell=True)
    process.wait()

    if process.returncode == 0:
        return True
    else:
        return False


# 初始化文件夹
def initialize(upload_folder):
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)


# 计算目录中文件夹的个数
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


# 下载文件
def download_zip_files(video_file_path, video_arr, video_generate_path):
    zip_filename = 'result_files.zip'

    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        for video in video_arr:
            zipf.write(video_file_path + video, video)

    print(video_generate_path)

    return send_file(video_generate_path, as_attachment=True)
