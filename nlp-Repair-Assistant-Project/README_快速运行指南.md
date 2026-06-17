# nlp-Repair-Assistant 快速运行指南



## 1. 环境准备 (Environment Setup)
本项目基于 Python 3.10+ 开发，建议使用虚拟环境以避免依赖冲突。

### Windows 系统一键配置：
我们已经提供了一个 PowerShell 脚本来自动创建虚拟环境并下载所需依赖。
1. 将压缩包解压到你想要的目录下。
2. 在该目录下，右键点击空白处，选择“在终端中打开” (Open in Terminal) 或者打开 PowerShell 并 `cd` 到该目录。
3. 运行环境配置脚本：
   ```powershell
   .\setup.ps1
   ```
   *(注：这会自动创建 `venv` 文件夹，安装 `requirements.txt` 中的库，并提前下载所需的模型缓存到本地。如果提示权限不足，请先运行 `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`)*

### Mac/Linux 或手动配置：
如果你不使用 Windows 或者想手动配置，请执行以下命令：
```bash
# 1. 创建并激活虚拟环境
python3 -m venv venv
source venv/bin/activate  # Windows 下用 venv\Scripts\activate

# 2. 安装依赖
pip install -r requirements.txt

# 3. 预下载模型（必须执行，防止答辩时断网）
python -c "from sentence_transformers import SentenceTransformer; SentenceTransformer('all-MiniLM-L6-v2')"
```

---

## 2. 如何运行项目 (Running the Project)

确保你的虚拟环境已经激活（命令行开头会有 `(venv)` 字样）。

### 运行终端测试版 (Terminal Test)
如果你想快速在命令行里测试检索逻辑和模块是否正常：
```bash
python test_run.py
```

### 运行完整图形界面 (Streamlit UI)
我们的主交互界面由 Streamlit 构建。运行以下命令启动网页端 UI：
```bash
streamlit run app.py
```
运行后，浏览器会自动弹出一个网页，你可以像正常用户一样在里面输入故障现象（比如：“咖啡机出水好慢”），测试系统的检索和生成效果。

---

## 3. 文档阅读指引
为了配合接下来的冲刺与分工，请大家阅读对应的文档：
- **如果是组员 A**：请立刻查看 `Task_组员A_语料库扩充指南.md` 并开始扩充数据。
- **如果是组员 B**：请立刻查看 `Task_组员B_测试验证与图表产出指南.md` 并开始写评测代码。
- **如果要写报告或了解原理**：请仔细阅读 `维修助手_技术构建与运行原理解析.md` 和 `维修助手_总方案与执行手册.md`。

---

## 常见问题 (FAQ)
- **第一次启动很慢？**：因为系统在后台把 JSON 语料库实时编码成高维向量 (Embeddings) 并存入 `cache` 文件夹。只要第一次成功了，之后都是秒开。
- **找不到模块报错？**：请检查你是否激活了虚拟环境 (`venv`)。
- **代码中有乱码？**：请确保你的代码编辑器使用 UTF-8 编码打开文件。
