import os
import uuid
import torch
from TTS.api import TTS
import gradio as gr

# Agree to Coqui TOS
os.environ["COQUI_TOS_AGREED"] = "1"

# Configuration
MODEL_NAME = "tts_models/multilingual/multi-dataset/xtts_v2"
LANGUAGES = ["en", "es", "fr", "de", "it", "pt", "pl", "tr", "ru", "nl", "cs", "ar", "zh-cn", "ja", "hu", "ko"]

# Load Model
print(">>> Loading TTS Model...")
device = "cuda" if torch.cuda.is_available() else "cpu"
tts = TTS(MODEL_NAME).to(device)
print(f">>> Model loaded on {device}")

def clone_voice(text, language, speaker_wav):
    if not text:
        raise gr.Error("Please enter text to speak.")
    if not speaker_wav:
        raise gr.Error("Please upload or record a reference voice.")

    output_filename = f"output_{uuid.uuid4()}.wav"
    output_path = os.path.join("output", output_filename)
    os.makedirs("output", exist_ok=True)

    try:
        tts.tts_to_file(
            text=text,
            speaker_wav=speaker_wav,
            language=language,
            file_path=output_path,
            split_sentences=False
        )
        return output_path
    except Exception as e:
        raise gr.Error(f"Generation failed: {str(e)}")

# Gradio Interface
with gr.Blocks(title="MyOwnTTS - Voice Cloning") as demo:
    gr.Markdown(
        """
        # 🎙️ MyOwnTTS: Voice Cloning Demo
        
        Upload a 60-second voice sample (or use the default one), enter text, and generate speech in multiple languages.
        
        *Powered by Coqui TTS (XTTS v2)*
        """
    )
    
    with gr.Row():
        with gr.Column():
            text_input = gr.Textbox(
                label="Text to Speak / 输入文字", 
                placeholder="Hello, this is a voice cloning test.",
                lines=3
            )
            language_input = gr.Dropdown(
                label="Language / 语言", 
                choices=LANGUAGES, 
                value="zh-cn"
            )
            # Use the local sample as default if it exists
            default_audio = "samples/my_voice_60s.wav" if os.path.exists("samples/my_voice_60s.wav") else None
            
            audio_input = gr.Audio(
                label="Reference Voice / 参考音频 (60s)", 
                type="filepath", 
                value=default_audio
            )
            
            submit_btn = gr.Button("🚀 Generate Speech / 生成语音", variant="primary")
        
        with gr.Column():
            audio_output = gr.Audio(label="Generated Audio / 生成结果")
            
    submit_btn.click(
        fn=clone_voice, 
        inputs=[text_input, language_input, audio_input], 
        outputs=audio_output
    )

    gr.Markdown(
        """
        ### ⚠️ Disclaimer
        This tool is for educational and research purposes only. Do not use it to clone voices without consent.
        """
    )

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
