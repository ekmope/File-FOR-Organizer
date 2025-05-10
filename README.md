<!-- markdownlint-disable first-line-h1 -->
<!-- markdownlint-disable html -->
<!-- markdownlint-disable no-duplicate-header -->

<div align="center">
  <img src="https://cdn-icons-png.flaticon.com/512/3050/3050202.png" width="20%" alt="File Organizer" />
</div>

<hr>

<div align="center" style="line-height: 1;">
  <a href="https://github.com/ekmope/File-FOR-Organizer"><img alt="GitHub Repo"
    src="https://img.shields.io/badge/📂%20GitHub-File_Organizer-536af5?logo=github&color=536af5"/></a>
  <a href="https://choosealicense.com/licenses/mit/"><img alt="License"
    src="https://img.shields.io/badge/📜%20License-MIT-f5de53?color=f5de53"/></a>
  <a href="https://pypi.org/project/pyinstaller/"><img alt="PyInstaller"
    src="https://img.shields.io/badge/📦%20Packaged_with-PyInstaller-2ba97a?color=2ba97a"/></a>
  <img src="https://img.shields.io/badge/Python-3.7%2B-blue" alt="Python">
  <img src="https://img.shields.io/github/last-commit/ekmope/File-FOR-Organizer" alt="Last Commit">
</div>

## Table of Contents

1. [Introduction](#1-introduction)
2. [Features](#2-features)
3. [Quick Start](#3-quick-start)
4. [Advanced Usage](#4-advanced-usage)
5. [Build from Source](#5-build-from-source)
6. [Roadmap](#6-roadmap)
7. [Contributing](#7-contributing)
8. [License](#8-license)
9. [Contact](#9-contact)

---

## 1. Introduction

**File Organizer** 是一个智能文件自动分类工具，支持通过命令行快速整理杂乱目录。基于文件扩展名自动归类到预设文件夹（如图片、文档、代码等），提升工作效率。支持 Windows/macOS/Linux 全平台运行。

<div align="center">
  <img src="demo.gif" width="70%">
</div>

---

## 2. Features

### Core Architecture
- **轻量化内核**：单脚本实现核心功能（<150行代码）
- **零依赖**：仅需标准库（`os`/`shutil`）
- **跨平台兼容**：原生适配主流操作系统

### Functional Highlights
- 🗂️ 支持 5 大文件类型自动分类（可扩展）
- 🔄 自动跳过隐藏文件及系统文件
- 🛡️ 错误处理与日志记录机制
- ⚙️ 自定义分类规则（修改代码即可扩展）

---

## 3. Quick Start

### Prerequisites
- Python 3.7+
- Git（可选）

### Installation
```bash
# 克隆仓库
git clone https://github.com/ekmope/File-FOR-Organizer.git
cd File-FOR-Organizer

# 运行整理工具
python organizer.py
```

### Basic Usage
| Command          | Description          | Example                  |
|------------------|----------------------|--------------------------|
| 直接运行         | 整理当前目录         | `python organizer.py`    |
| 指定路径         | 整理目标目录         | `python organizer.py /path/to/folder` |

---

## 4. Advanced Usage

### 自定义分类规则
修改 `categories` 字典扩展支持的文件类型：
```python
# 在 organizer.py 中修改
categories = {
    "Music": [".mp3", ".wav", ".flac"],
    "Spreadsheets": [".xlsx", ".csv"]
}
```

### 日志配置
```python
# 启用详细日志记录
DEBUG_MODE = True  # 设为 False 关闭调试输出
```

---

## 5. Build from Source

### 生成可执行文件
```bash
# 安装依赖
pip install pyinstaller

# 打包（Windows）
pyinstaller --onefile --name file-organizer.exe organizer.py

# 打包（macOS/Linux）
pyinstaller --onefile --name file-organizer organizer.py
```

### 输出路径
```
dist/
  ├── file-organizer.exe    # Windows可执行文件
  └── file-organizer        # Unix可执行文件
```

---

## 6. Roadmap

| 状态 | 功能                | 目标版本 |
|------|---------------------|----------|
| ✅   | 基础文件分类        | v1.0     |
| 🚧   | 重复文件检测        | v1.2     |
| ⏳   | 图形界面（Tkinter） | v2.0     |
| ⏳   | 云端备份集成        | v2.1     |

---

## 7. Contributing

欢迎通过以下方式参与贡献:cite[6]:cite[7]：
1. Fork 本仓库
2. 创建功能分支 (`git checkout -b feature/awesome`)
3. 提交修改 (`git commit -am 'Add awesome feature'`)
4. 推送分支 (`git push origin feature/awesome`)
5. 发起 Pull Request

---

## 8. License

本项目采用 [MIT License](LICENSE)，允许商业使用和修改。核心条款包括：
- 保留原始版权声明
- 免责条款

---

## 9. Contact

遇到问题或建议？欢迎通过以下方式联系：
- 📮 Email: your.email@example.com
- 🐛 [Issue Tracker](https://github.com/ekmope/File-FOR-Organizer/issues)