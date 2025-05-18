import os
import glob
from docx import Document
from openai import OpenAI


def getName(folder_path,n):
    # 获取文件夹中所有文件的列表
    files = os.listdir(folder_path)

    # 确保 n 是有效的索引
    if n < 0 or n >= len(files):
        return "索引超出文件列表范围"

    # 获取第 n 个文件的文件名（去除路径）
    file_name = files[n]

    # 去除文件名的后缀
    name, _ = os.path.splitext(file_name)

    return name

def getArticle(folder_path, n):
    # 定义支持的文件类型
    supported_extensions = ['mp3', 'mp4', 'mpeg', 'mpga', 'm4a', 'wav', 'webm']
    files = []

    # 遍历所有支持的文件扩展名，收集文件
    for ext in supported_extensions:
        files.extend(glob.glob(os.path.join(folder_path, f'*.{ext}')))

    # 检查索引n是否在文件列表的范围内
    if n < 0 or n >= len(files):
        print("索引超出范围")
        return None

    # 获取第n个文件的完整路径
    file_path = files[n]

    # 打开文件
    audio_file = open(file_path, "rb")

    # 创建OpenAI客户端实例
    client = OpenAI()

    # 进行转录任务
    transcript = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file,
        response_format="text",
        language="en"
    )

    # 关闭文件
    audio_file.close()
    if transcript == "":
        return None
    # 返回转录的文本
    return transcript

# print(getArticle("audio",1))

def getNum(folder_path):
    # 定义所有需要统计的文件扩展名
    extensions = ['mp3', 'mp4', 'mpeg', 'mpga', 'm4a', 'wav', 'webm']

    # 初始化文件数量计数器
    num = 0

    # 遍历所有扩展名，统计每种类型的文件数量
    for ext in extensions:
        pattern = os.path.join(folder_path, f'*.{ext}')
        files = glob.glob(pattern)
        num += len(files)  # 累加文件数量

    return num
