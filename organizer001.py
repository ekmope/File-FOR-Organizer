import os
import shutil
import argparse
import logging
import json
from pathlib import Path

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("organizer.log"),
        logging.StreamHandler()
    ]
)

def load_config(config_path="categories.json"):
    """从JSON文件加载分类配置"""
    default_categories = {
        "Images": [".jpg", ".png", ".gif"],
        "Documents": [".pdf", ".docx", ".txt"],
        # ...其他默认分类
    }
    try:
        with open(config_path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return default_categories

def organize_files(directory=".", recursive=False):
    """整理目录（可选递归子目录）"""
    categories = load_config()
    
    for item in Path(directory).iterdir():
        # 递归处理子目录
        if recursive and item.is_dir() and not item.name.startswith("."):
            organize_files(item, recursive)
            continue
            
        # 跳过目录和隐藏文件
        if item.is_dir() or item.name.startswith("."):
            continue
            
        # 获取扩展名
        ext = item.suffix.lower()
        
        # 匹配分类
        target_folder = "Others"
        for folder, exts in categories.items():
            if ext in exts:
                target_folder = folder
                break
        
        # 创建目标目录
        target_path = Path(directory) / target_folder
        target_path.mkdir(exist_ok=True)
        
        # 移动文件
        try:
            shutil.move(str(item), str(target_path / item.name))
            logging.info(f"Moved: {item.name} => {target_folder}/")
        except shutil.Error as e:
            logging.error(f"Failed to move {item.name}: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="文件整理工具")
    parser.add_argument("path", nargs="?", default=".", help="目标目录路径")
    parser.add_argument("-r", "--recursive", action="store_true", help="递归处理子目录")
    parser.add_argument("-c", "--config", help="自定义配置文件路径")
    args = parser.parse_args()
    
    if args.config:
        global categories
        categories = load_config(args.config)
    
    organize_files(args.path, args.recursive)
    logging.info("\n整理完成！")