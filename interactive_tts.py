import os
import time
import sys
import torch
from TTS.api import TTS

# Enable MPS fallback for missing operators (macOS specific fix)
os.environ["PYTORCH_ENABLE_MPS_FALLBACK"] = "1"

# Configuration
SAMPLE_DIR = "samples"
OUTPUT_DIR = "output"
REFERENCE_AUDIO_FILENAME = "my_voice_60s.wav"
MODEL_NAME = "tts_models/multilingual/multi-dataset/xtts_v2"

def main():
    # Ensure directories exist
    os.makedirs(SAMPLE_DIR, exist_ok=True)
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    reference_audio_path = os.path.join(SAMPLE_DIR, REFERENCE_AUDIO_FILENAME)

    if not os.path.exists(reference_audio_path):
        print(f"错误: 未找到参考音频文件: {reference_audio_path}")
        return

    print(">>> 正在初始化模型 (这可能需要几秒钟，但只需要加载一次)...")
    
    # Force CPU as per previous stability fix
    device = "cpu" 
    
    try:
        # Load model once
        tts = TTS(MODEL_NAME).to(device)
        print(f">>> 模型加载完成! 使用设备: {device}")
    except Exception as e:
        print(f"模型加载失败: {e}")
        return

    print("\n" + "="*40)
    print("   交互式语音生成器 (快速模式)")
    print("   输入文字后回车，即可立即生成语音")
    print("   输入 'q' 或 'exit' 退出程序")
    print("="*40 + "\n")

    count = 1
    while True:
        try:
            text = input(f"\n[{count}] 请输入文字: ").strip()
        except KeyboardInterrupt:
            print("\n退出程序。")
            break

        if text.lower() in ('q', 'quit', 'exit'):
            print("退出程序。")
            break
        
        if not text:
            continue

        # Generate unique filename with timestamp or counter
        timestamp = int(time.time())
        output_filename = f"speech_{count}_{timestamp}.wav"
        output_path = os.path.join(OUTPUT_DIR, output_filename)
        
        print("   正在生成...", end="", flush=True)
        start_time = time.time()
        
        try:
            # Generate audio
            tts.tts_to_file(
                text=text,
                speaker_wav=reference_audio_path,
                language="zh-cn",
                file_path=output_path,
                split_sentences=False
            )
            
            duration = time.time() - start_time
            print(f" 完成! (耗时 {duration:.2f}s)")
            print(f"   已保存: {output_path}")
            
            # Auto-play on macOS
            if sys.platform == "darwin":
                print("   正在播放...")
                os.system(f"afplay '{output_path}'")
                
            count += 1
            
        except Exception as e:
            print(f"\n   生成失败: {e}")

if __name__ == "__main__":
    main()
