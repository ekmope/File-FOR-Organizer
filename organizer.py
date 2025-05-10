import os
import shutil

def organize_files(directory="."):
    """
    自动整理指定目录下的文件（默认当前目录）
    按扩展名分类到不同文件夹，例如 .txt 文件放入 "Text" 文件夹
    """
    # 定义分类规则（可自定义添加）
    categories = {
        "Images": [".jpg", ".png", ".gif", ".webp"],
        "Documents": [".pdf", ".docx", ".txt", ".md"],
        "Archives": [".zip", ".rar", ".7z"],
        "Code": [".py", ".js", ".html", ".css"],
        "Videos": [".mp4", ".avi", ".mkv"]
    }

    # 遍历目录中的文件
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        # 跳过目录和隐藏文件
        if os.path.isdir(file_path) or filename.startswith("."):
            continue
        
        # 获取文件扩展名
        _, ext = os.path.splitext(filename)
        ext = ext.lower()  # 统一小写
        
        # 查找匹配的文件夹
        target_folder = "Others"  # 默认分类
        for folder, exts in categories.items():
            if ext in exts:
                target_folder = folder
                break
        
        # 创建目标文件夹（如果不存在）
        target_path = os.path.join(directory, target_folder)
        os.makedirs(target_path, exist_ok=True)
        
        # 移动文件
        try:
            shutil.move(file_path, os.path.join(target_path, filename))
            print(f"Moved: {filename} => {target_folder}/")
        except Exception as e:
            print(f"Error moving {filename}: {str(e)}")

if __name__ == "__main__":
    path = input("请输入要整理的目录路径（直接回车使用当前目录）: ").strip()
    if not path:
        path = os.getcwd()
    
    organize_files(path)
    print("\n整理完成！")