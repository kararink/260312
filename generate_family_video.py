import os
import sys
import glob
from PIL import Image, ImageDraw, ImageFont
from elevenlabs.client import ElevenLabs
from moviepy.editor import ImageClip, AudioFileClip, CompositeAudioClip, concatenate_videoclips

api_key = os.environ.get("ELEVENLABS_API_KEY")
if not api_key:
    # Try reading from .env
    env_path = os.path.join(os.path.dirname(__file__), ".env")
    if os.path.exists(env_path):
        with open(env_path, "r", encoding="utf-8") as f:
            for line in f:
                if line.startswith("ELEVENLABS_API_KEY="):
                    api_key = line.strip().split("=", 1)[1].strip('"\'')
                    os.environ["ELEVENLABS_API_KEY"] = api_key

if not api_key:
    print("Error: ELEVENLABS_API_KEY environment variable not found.")
    sys.exit(1)

client = ElevenLabs(api_key=api_key)

# 1. BGM生成
bgm_path = "bgm.mp3"
if not os.path.exists(bgm_path):
    print("Generating BGM...")
    try:
        audio = client.music.compose(
            prompt="A very warm, gentle, and heartwarming acoustic guitar and soft piano background music. Sentimental, beautiful, perfect for a family memory video.",
            music_length_ms=32000
        )
        audio_chunks = []
        for chunk in audio:
            audio_chunks.append(chunk)
        if len(audio_chunks) > 0:
            with open(bgm_path, "wb") as f:
                for chunk in audio_chunks:
                    f.write(chunk)
            print("BGM generated.")
        else:
            print("BGM generation returned empty.")
    except Exception as e:
        print("BGM generation skipped/failed:", e)

# 2. TTS・テロップ生成
texts = [
    "桜の便りが届く季節。\nチャロと一緒に、穏やかな空を見上げています。",
    "さら、合格おめでとう。\n君の新しい春を、遠くからでもずっと見守っているよ。",
    "まち、今までありがとう。\n離れていても、変わらない繋がりがここにあるよ。"
]
voice_id = "JBFqnCBsd6RMkjVDRZzb" # George

image_dir = r"C:\Users\杢之助\.gemini\antigravity\brain\79abe86b-7b3a-4424-bb84-25d4eea034ee"
img_files = [
    glob.glob(os.path.join(image_dir, "scene1_dog_porch_*.png"))[0],
    glob.glob(os.path.join(image_dir, "scene2_girl_sakura_*.png"))[0],
    glob.glob(os.path.join(image_dir, "scene3_evening_table_*.png"))[0]
]

processed_imgs = []
audio_paths = []

font_path = r"C:\Windows\Fonts\meiryo.ttc"
if not os.path.exists(font_path):
    font_path = r"C:\Windows\Fonts\msgothic.ttc"
if not os.path.exists(font_path):
    font_path = "arial.ttf" # Fallback

for i, text in enumerate(texts):
    # 音声生成
    mp3_path = f"voice_{i+1}.mp3"
    audio_paths.append(mp3_path)
    if not os.path.exists(mp3_path):
        print(f"Generating TTS for scene {i+1}...")
        try:
            audio = client.text_to_speech.convert(
                text=text.replace('\n', ''),
                voice_id=voice_id,
                model_id="eleven_multilingual_v2"
            )
            audio_chunks = []
            for chunk in audio:
                audio_chunks.append(chunk)
            if len(audio_chunks) > 0:
                with open(mp3_path, "wb") as f:
                    for chunk in audio_chunks:
                        f.write(chunk)
            else:
                print("Voice generation returned empty.")
        except Exception as e:
            print("Voice generation skipped/failed:", e)

    # テロップ合成
    img = Image.open(img_files[i]).convert("RGBA")
    # Resize to 1920x1080 if not already
    img = img.resize((1920, 1080), Image.LANCZOS)
    draw = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype(font_path, 48)
    except IOError:
        font = ImageFont.load_default()
    
    # 影付きテキスト
    margin = 50
    shadow_color = "black"
    text_color = "white"
    
    # 簡単な中央寄せの概算
    draw.text((margin+5, 1080 - 150 + 5), text, font=font, fill=shadow_color)
    draw.text((margin, 1080 - 150), text, font=font, fill=text_color)
    
    out_img = f"scene{i+1}_text.png"
    img.save(out_img)
    processed_imgs.append(out_img)

# 3. 動画組み立て
print("Assembling video with MoviePy ImageSequenceClip...")
from moviepy.editor import ImageSequenceClip
final_video = ImageSequenceClip(processed_imgs, durations=[11, 11, 11])

out_file = os.path.join(image_dir, "Family_Charo_Bond.mp4")
print(f"Writing final video file to {out_file}...")
final_video.write_videofile(out_file, fps=24, codec="libx264", audio=False)
print("Video assembly complete.")
