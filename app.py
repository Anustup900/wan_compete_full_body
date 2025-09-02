import os
import streamlit as st
from PIL import Image, UnidentifiedImageError

# Set the main directory
main_folder = "data"  # change this

# Allowed image filenames in the exact order you want
allowed_files = [
    "cropped_garment.jpg",
    "reference_compiler_upscaled.jpg",
    "output_turbo.png",
    "output_wan_upgrade.png",
    "wan_single_image.png"
]

st.set_page_config(layout="wide")
st.title("WAN FIGHT")

for folder_name in sorted(os.listdir(main_folder)):
    folder_path = os.path.join(main_folder, folder_name)

    if os.path.isdir(folder_path):
        st.subheader(folder_name)

        # Filter files and maintain allowed_files order
        image_files = [
            f for f in allowed_files
            if f.lower() in {name.lower() for name in os.listdir(folder_path)}
        ]

        if not image_files:
            st.info("No matching images in this folder.")
            continue

        # Display in horizontal columns (order preserved)
        cols = st.columns(len(image_files))

        for idx, file_name in enumerate(image_files):
            img_path = os.path.join(folder_path, file_name)
            try:
                img = Image.open(img_path)
                with cols[idx]:
                    st.image(img, caption=os.path.splitext(file_name)[0], use_container_width=True)
            except UnidentifiedImageError:
                st.warning(f"Skipping invalid image: {file_name}")
