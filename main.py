import os

# Enable MPS fallback for missing operators
os.environ["PYTORCH_ENABLE_MPS_FALLBACK"] = "1"

import torch
from TTS.api import TTS

# Configuration
SAMPLE_DIR = "samples"
OUTPUT_DIR = "output"
# You can change this filename to match your recorded file
REFERENCE_AUDIO_FILENAME = "my_voice_60s.wav" 
OUTPUT_FILENAME = "output_speech.wav"
TEXT_TO_SPEAK = "为什么要做回测分析？首先是验证策略有效性，看策略在历史上能否盈利；其次是评估风险，了解可能的最大亏损；第三是优化参数，找到最优的均线周期；最后是预估资金曲线，对实盘有个心理预期。一份完整的回测报告包含四大要素：收益曲线、关键指标、交易统计和交易明细。"
MODEL_NAME = "tts_models/multilingual/multi-dataset/xtts_v2"

def main():
    # Ensure directories exist
    os.makedirs(SAMPLE_DIR, exist_ok=True)
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    reference_audio_path = os.path.join(SAMPLE_DIR, REFERENCE_AUDIO_FILENAME)

    # Check if reference audio exists
    if not os.path.exists(reference_audio_path):
        print(f"错误: 未找到参考音频文件: {reference_audio_path}")
        print(f"请录制一段约60秒的你的声音 (wav格式)，命名为 '{REFERENCE_AUDIO_FILENAME}' 并放入 '{SAMPLE_DIR}' 文件夹中。")
        return

    print("正在加载模型...")
    # Get device
    # device = "cuda" if torch.cuda.is_available() else "cpu"
    # if torch.backends.mps.is_available():
    #     device = "mps" # For macOS Metal performance
    device = "cpu" # Force CPU due to MPS compatibility issues with ComplexFloat in PyTorch 2.1.2
    
    print(f"使用设备: {device}")

    # Init TTS
    tts = TTS(MODEL_NAME).to(device)

    print("正在生成语音...")
    # Run TTS
    # Note: XTTS supports multiple languages. We specify "zh-cn" for Chinese.
    tts.tts_to_file(
        text=TEXT_TO_SPEAK,
        speaker_wav=reference_audio_path,
        language="zh-cn",
        file_path=os.path.join(OUTPUT_DIR, OUTPUT_FILENAME),
        split_sentences=False
    )

    print(f"生成完成! 音频已保存至: {os.path.join(OUTPUT_DIR, OUTPUT_FILENAME)}")

if __name__ == "__main__":
    main()
