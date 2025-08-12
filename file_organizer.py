import os

imagesExtensions = ["jpg", "jpeg", "png", "gif", "bmp", "tiff", "svg", "webp", ]
videoExtensions = ["mp4", "mkv", "mov", "avi", "flv", "wmv"]
docsExtensions = ["pdf", "doc", "docx", "xls", "xlsx", "ppt", "pptx", "txt"]


def get_file_extension(file_path):
    _, ext = os.path.splitext(file_path)
    return ext.lower()


def get_category_name(file_path):
    ext = get_file_extension(file_path)
    if ext in imagesExtensions:
        return "images"
    elif ext in videoExtensions:
        return "videos"
    elif ext in docsExtensions:
        return "documents"
    else:
        return "others"
