import os
import streamlit as st
from PIL import Image, UnidentifiedImageError

# Set the main directory
main_folder = "data"  # change this

# Allowed image filenames (lowercase only)
allowed_files = {"cropped_garment.jpg", "reference_compiler_upscaled.jpg", "output_turbo.png", "output_wan.png",
                 "output_wan_upgrade.png"}

st.title("WAN FIGHT")
st.set_page_config(layout="wide")

for folder_name in sorted(os.listdir(main_folder)):
    folder_path = os.path.join(main_folder, folder_name)

    if os.path.isdir(folder_path):
        st.subheader(folder_name)

        # Filter only specific files (case-insensitive)
        image_files = [
            f for f in sorted(os.listdir(folder_path))
            if f.lower() in {name.lower() for name in allowed_files}
        ]

        if not image_files:
            st.info("No matching images in this folder.")
            continue

        # Display in horizontal columns
        cols = st.columns(len(image_files))

        for idx, file_name in enumerate(image_files):
            img_path = os.path.join(folder_path, file_name)
            try:
                img = Image.open(img_path)
                with cols[idx]:
                    st.image(img, caption=os.path.splitext(file_name)[0], use_container_width=True)
            except UnidentifiedImageError:
                st.warning(f"Skipping invalid image: {file_name}")