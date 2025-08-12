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


def organize_files(source_dir, target_dir):
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    for root, _, files in os.walk(source_dir):
        for file in files:
            file_path = os.path.join(root, file)
            category = get_category_name(file_path)
            category_dir = os.path.join(target_dir, category)

            if not os.path.exists(category_dir):
                os.makedirs(category_dir)

            target_file_path = os.path.join(category_dir, file)
            if not os.path.exists(target_file_path):
                os.rename(file_path, target_file_path)
            else:
                print(f"File {target_file_path} already exists. Skipping.")


def main():
    source_dir = input("Enter the source directory: ")
    target_dir = input("Enter the target directory: ")
    organize_files(source_dir, target_dir)


if __name__ == "__main__":
    main()
    print("Files organized successfully.")