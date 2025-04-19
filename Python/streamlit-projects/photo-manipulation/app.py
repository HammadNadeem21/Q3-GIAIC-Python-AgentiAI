import streamlit as st
from PIL import Image, ImageOps
import io
from rembg import remove


# app title
st.title("Photo Manipulation Tool")

# upload image
upload_image = st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])


if upload_image is not None:

    img = Image.open(upload_image).convert("RGBA") # convert in RGBA format
    st.image(img, caption="Original Image")


    # 1. Remove Background
    if st.button("Remove Background"):
        # Get the uploaded image in bytes format and use the 'rembg' library to remove its background
        img_no_bg = remove(upload_image.getvalue()) 
        img_no_bg = Image.open(io.BytesIO(img_no_bg)).convert("RGBA") # Convert the bytes output to an image object in RGBA format
        st.image(img_no_bg, caption="Background Removed")
        img = img_no_bg # Update the 'img' variable with the new image without background.


    #2. Upload a new Background 
    background_image = st.file_uploader("Upload a New Background Image", type=["jpg", "jpeg", "png"])

    if background_image is not None:
        # Open the new background image and convert into RGBA format.
        new_bg = Image.open(background_image).convert("RGBA") 
        
        # Resize the new background
        new_bg = new_bg.resize(img.size) 

        # get the transparancy
        img_alpha = img.split()[-1]

        # Create a blank Image
        combined_image = Image.new("RGBA", img.size)

        # Paste the new background image
        combined_image.paste(new_bg, (0, 0))

        # Paste the original image
        combined_image.paste(img, (0, 0), img_alpha)  


        # Show the final combined image in the Streamlit app
        st.image(combined_image, caption="Image with New Background")

        # Image with new Background
        img = combined_image


    #3. Rotate the image
    rotate_angle = st.slider("Rotate Image", 0, 360, 0)

    if rotate_angle:
        rotated_img = img.rotate(rotate_angle, expand=True)
        st.image(rotated_img, caption=f"Image Rotated by {rotate_angle} degrees")
        img = rotated_img

    
    # 4. Crop the image
    if st.button("Crop Image"):
        cropped_img = ImageOps.fit(img, (200, 200))
        st.image(cropped_img, caption="Cropped Image")
        img = cropped_img


    # Download Image
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    byte = buf.getvalue()
    st.download_button(label="Download Image", data=byte, file_name="manipulated_image.png")

else:
    st.write("Please upload an image to start.")
