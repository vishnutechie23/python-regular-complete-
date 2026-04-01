import streamlit as st
import pandas as pd

st.title("🎬 Streamlit Media Elements Demo")

# ============================================
# 1️⃣ Displaying an Image
st.subheader("1️⃣ Display an Image")

# You can display an image from a file path or URL
st.image("https://wallpapers.com/images/featured/4k-oaax18kaapkokaro.jpg", 
         caption="🖼️ Example Image from URL"
         )

# ============================================
# 2️⃣ Playing an Audio File
st.subheader("2️⃣ Play an Audio File")

# Example: Upload your own audio file
audio_file = st.file_uploader("Upload an audio file (MP3, WAV, etc.):", type=["mp3", "wav"])
if audio_file is not None:
    st.audio(audio_file, format='audio/mp3')

# ============================================
# 3️⃣ Playing a Video File
st.subheader("3️⃣ Play a Video File")

# Example: Upload your own video file
video_file = st.file_uploader("Upload a video file (MP4, MOV, etc.):", type=["mp4", "mov", "avi"])
if video_file is not None:
    st.video(video_file)

# ============================================
# 4️⃣ File Uploader – CSV, Images, Anything
st.subheader("4️⃣ File Uploader for CSV/Image/Any File")

uploaded_file = st.file_uploader("Upload a file (CSV, image, or anything):")
if uploaded_file is not None:
    file_type = uploaded_file.type
    
    if file_type == "text/csv":
        df = pd.read_csv(uploaded_file)
        st.write("📄 Uploaded CSV File:")
        st.dataframe(df)
    
    elif "image" in file_type:
        st.image(uploaded_file, caption="🖼️ Uploaded Image")
    
    elif "audio" in file_type:
        st.audio(uploaded_file)
    
    elif "video" in file_type:
        st.video(uploaded_file)
    
    else:
        st.write("✅ File uploaded, but preview not supported for this type.")