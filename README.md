# 声音克隆 TTS 项目

这是一个简单的 Python 项目，使用 Coqui TTS (XTTS v2) 来克隆你的声音并进行文字转语音。

## 准备工作

1. **环境配置**:
   项目已配置好虚拟环境。
   
   激活虚拟环境:
   ```bash
   source venv/bin/activate
   ```
   
   (如果尚未安装依赖) 安装依赖:
   ```bash
   pip install -r requirements.txt
   ```
   *注意: 如果你在安装 `TTS` 时遇到问题，可能需要先安装系统级的依赖 (如 `libsndfile`).*

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

## 运行

### 方式一：单次生成 (main.py)
如果你只想生成一句话：
```bash
python main.py
```
修改 `main.py` 中的 `TEXT_TO_SPEAK` 变量来改变文字。

### 方式二：交互式快速生成 (推荐)
如果你想连续生成多句话，不需要每次都等待模型加载：
```bash
python interactive_tts.py
```
1. 程序启动后会加载一次模型。
2. 然后你可以像聊天一样，输入一句话，回车，它就会立刻生成并自动播放。
3. 输入 `q` 退出。

## 修改文字

你可以编辑 `main.py` 文件中的 `TEXT_TO_SPEAK` 变量来修改想要生成的文字内容。
