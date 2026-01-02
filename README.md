# Voice Cloning TTS Project / 声音克隆 TTS 项目

![Python](https://img.shields.io/badge/python-3.11-blue.svg)
![License](https://img.shields.io/badge/license-AGPL--3.0-red.svg)
![Docker](https://img.shields.io/badge/docker-supported-2496ED.svg?logo=docker&logoColor=white)
![Platform](https://img.shields.io/badge/platform-macOS%20%7C%20Linux-lightgrey)
[![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/JIANGJINGZHE/Mac_Lightweight_Voice_Clone)

**Author / 作者:** 江景哲 JIANG JINGZHE  
**Contact / 联系方式:** contact@jiangjingzhe.com

---

## 🔊 Audio Demo / 效果试听

> **[▶️ Click here to listen to the demo / 点击此处播放试听样本](assets/audio/demo_voice.wav)**

---

## 🇬🇧 English Version

### Introduction
This is a simple Python project that uses Coqui TTS (XTTS v2) to clone your voice and perform text-to-speech generation. It is optimized for macOS (Apple Silicon) environments.

### Prerequisites

1. **Environment Setup**:
   The project uses a virtual environment.
   
   Activate the virtual environment:
   ```bash
   source venv/bin/activate
   ```
   
   Install dependencies (if not already installed):
   ```bash
   pip install -r requirements.txt
   ```

2. **Recording Voice**:
   You can use the included script to record directly:
   ```bash
   python record_audio.py
   ```
   Or record manually:
   - Record about 60 seconds of your voice.
   - Speak clearly in a quiet environment.
   - Save as WAV format.
   - Rename the file to `my_voice_60s.wav`.
   - Place the file in the `samples` folder.

### Usage

#### Option 1: Single Generation (`main.py`)
If you only want to generate one sentence:
```bash
python main.py
```
Modify the `TEXT_TO_SPEAK` variable in `main.py` to change the text.

#### Option 2: Interactive Fast Generation (Recommended)
If you want to generate multiple sentences continuously without reloading the model every time:
```bash
python interactive_tts.py
```
1. The model loads once at startup.
2. Type a sentence and press Enter; it will generate and play automatically.
3. Type `q` to exit.

### 🐳 Docker Usage

1. **Build the Image**:
   ```bash
   docker build -t my-tts .
   ```

2. **Run the Container**:
   You need to mount the `samples` (input) and `output` (results) directories.
   ```bash
   docker run -it --rm \
     -v "$(pwd)/samples:/app/samples" \
     -v "$(pwd)/output:/app/output" \
     my-tts
   ```
   *Note: Audio playback will not work inside the container. Please check the `output` folder for generated files.*

---

## ⚠️ Security & Ethical Use Disclaimer / 安全与道德使用声明

**English:**
This project is intended for **educational and research purposes only**. 
- Do not use this software to clone voices without the explicit consent of the speaker.
- Do not use this software to generate content that is illegal, harmful, defamatory, or intended to deceive (e.g., deepfakes for fraud).
- The authors assume no responsibility for any misuse of this software. By using this software, you agree to take full responsibility for your actions.

**中文:**
本项目仅供**教育和研究目的**使用。
- 请勿在未获得说话者明确同意的情况下克隆其声音。
- 请勿使用本软件生成非法、有害、诽谤或旨在欺骗的内容（例如用于诈骗的深度伪造）。
- 作者不对本软件的任何滥用行为承担责任。使用本软件即表示您同意为您的一切行为承担全部责任。

## 📄 License / 许可证

This project is licensed under the **GNU Affero General Public License v3.0 (AGPL-3.0)**.
本项目采用 **GNU Affero General Public License v3.0 (AGPL-3.0)** 许可证。

See the [LICENSE](LICENSE) file for details.


## 🇨🇳 中文版本

### 简介
这是一个简单的 Python 项目，使用 Coqui TTS (XTTS v2) 来克隆你的声音并进行文字转语音。针对 macOS (Apple Silicon) 环境进行了优化。

### 准备工作

1. **环境配置**:
   项目已配置好虚拟环境。
   
   激活虚拟环境:
   ```bash
   source venv/bin/activate
   ```
   
   安装依赖 (如果尚未安装):
   ```bash
   pip install -r requirements.txt
   ```

2. **录制声音**:
   你可以使用自带的录音脚本直接录制：
   ```bash
   python record_audio.py
   ```
   或者手动录制：
   - 录制一段大约 60 秒的你的声音。
   - 说话清晰，背景安静。
   - 保存为 WAV 格式。
   - 将文件重命名为 `my_voice_60s.wav`。
   - 将文件放入 `samples` 文件夹中。

### 运行

#### 方式一：单次生成 (`main.py`)
如果你只想生成一句话：
```bash
python main.py
```
修改 `main.py` 中的 `TEXT_TO_SPEAK` 变量来改变文字。

#### 方式二：交互式快速生成 (推荐)
如果你想连续生成多句话，不需要每次都等待模型加载：
```bash
python interactive_tts.py
```
1. 程序启动后会加载一次模型。
2. 然后你可以像聊天一样，输入一句话，回车，它就会立刻生成并自动播放。
3. 输入 `q` 退出。

### 🐳 Docker 使用方法

1. **构建镜像**:
   ```bash
   docker build -t my-tts .
   ```

2. **运行容器**:
   你需要挂载 `samples` (输入) 和 `output` (输出) 目录。
   ```bash
   docker run -it --rm \
     -v "$(pwd)/samples:/app/samples" \
     -v "$(pwd)/output:/app/output" \
     my-tts
   ```
   *注意: 容器内无法直接播放音频。请在 `output` 文件夹中查看生成的文件。*

