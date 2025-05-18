import Get
import TransToPDF

def buttun():
    folder_path = "articles"
    n = Get.getNum(folder_path)
    for i in range(n):
        TransToPDF.TransToPDF(Get.getName(folder_path, i))
