## Chapter · Method

### 🛠️ 需要准备什么

1. **Python环境**: Python 3.7+
2. **依赖包**: 
   ```bash
   pip install Pillow
   ```
3. **API密钥**: 需要配置GPT API密钥，`config.json`中需要配置
4. **输入文件**: Markdown 格式的论文文件
5. **图片目录**: 论文相关的图片文件夹

### 🚀 怎么跑程序

#### 第一次用
```bash
cd Method_Agent
chmod +x pipeline.py  # 给脚本执行权限
python pipeline.py your_paper.md
```

#### Quick Start
```bash
cd Method_Agent
python pipeline.py your_paper.md
```

#### 完整用法
```bash
python pipeline.py paper.md --output-base-dir ./output --images-dir ./images
```

这里举个简单的例子，have a try 😊！
```bash
python pipeline.py paper_info/ChatDev/ChatDev.md --images-dir paper_info/ChatDev/ChatDev_images --output-base-dir ChatDev_output
```

#### 参数说明
- `paper.md`: 输入的论文文件（必须）
- `--output-base-dir`: 输出目录（可选，默认./pipeline_output）
- `--images-dir`: 图片目录

### 📊 基本效果


**输出**: 
```
output/
├── 论文名_segmentation/        # AI智能分割结果
│   └── split_pages/           # 每页独立的md文件
├── 论文名_generated_code/     # 每页对应的Manim动画代码
└── 论文名_generated_speech/   # 每页对应的配音文本
```

