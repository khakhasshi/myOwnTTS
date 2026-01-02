import sounddevice as sd
from scipy.io.wavfile import write
import os
import numpy as np

# Configuration
SAMPLE_DIR = "samples"
FILENAME = "my_voice_60s.wav"
DURATION = 60  # seconds
FS = 44100  # Sample rate

def record_audio():
    os.makedirs(SAMPLE_DIR, exist_ok=True)
    filepath = os.path.join(SAMPLE_DIR, FILENAME)

    print(f"准备录制 {DURATION} 秒的音频...")
    print("请在倒数结束后开始朗读一段文字（可以是任何书或文章）。")
    
    for i in range(3, 0, -1):
        print(f"{i}...")
        sd.sleep(1000)
    
    print("开始录音! (请说话...)")
    
    # Record
    myrecording = sd.rec(int(DURATION * FS), samplerate=FS, channels=1)
    sd.wait()  # Wait until recording is finished
    
    print("录音结束!")
    
    # Save as WAV
    # Convert to 16-bit PCM
    data = (myrecording * 32767).astype(np.int16)
    write(filepath, FS, data)
    
    print(f"文件已保存至: {filepath}")

if __name__ == "__main__":
    try:
        record_audio()
    except Exception as e:
        print(f"录音出错: {e}")
        print("请确保已安装 sounddevice: pip install sounddevice numpy scipy")
        print("如果是在 macOS 上，可能需要授予终端麦克风权限。")
