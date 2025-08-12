import os

imagesExtensions = ["jpg", "jpeg", "png", "gif", "bmp", "tiff", "svg", "webp", ]
videoExtensions = ["mp4", "mkv", "mov", "avi", "flv", "wmv"]
docsExtensions = ["pdf", "doc", "docx", "xls", "xlsx", "ppt", "pptx", "txt"]


def get_file_extension(file_path):
    _, ext = os.path.splitext(file_path)
    return ext.lower()
