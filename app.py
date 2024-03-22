import streamlit as st
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import ImageFormatter
from io import BytesIO
from PIL import Image 

def code_to_image(code, language, font_size=14, line_numbers=True, image_format="PNG"):
    lexer = get_lexer_by_name(language, stripall=True)
    formatter = ImageFormatter(font_size=font_size, line_numbers=line_numbers, format_name=image_format)
    image_data = BytesIO()
    highlight(code, lexer, formatter, image_data)
    return image_data.getvalue(), image_format.lower()

def main():
    st.title("Code to Image Converter")
    code = st.text_area("Paste your code here:", height=200)
    language = st.selectbox("Select programming language:", ["Python", "Java", "C", "C++", "JavaScript"])
    font_size = st.slider("Font Size:", min_value=8, max_value=24, value=14)
    line_numbers = st.checkbox("Show Line Numbers", value=True)
    image_format = st.selectbox("Select Image Format:", ["PNG", "JPEG", "GIF", "BMP", "TIFF"])
    
    if st.button("Convert to Image"):
        if code:
            st.write("Converting...")
            image_bytes, image_format = code_to_image(code, language.lower(), font_size, line_numbers, image_format)
            try:
                image = Image.open(BytesIO(image_bytes))
                st.image(image, caption="Code Image", use_column_width=True)
            except Exception as e:
                st.error("Error creating image:", e)
        else:
            st.write("Please paste some code.")

if __name__ == "__main__":
    main()
