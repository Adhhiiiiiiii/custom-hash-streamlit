import streamlit as st
import hashlib

# Custom hash function
def custom_hash(text, size=32):
    if not text:
        text = " "  # handle empty string
    
    # Step 1: Convert to ASCII and manipulate
    values = [ord(c) for c in text]
    
    # Step 2: Mix ASCII values with modular arithmetic
    mixed = []
    for i, v in enumerate(values):
        val = (v * (i + 3)**2 + (i * 7)) % 257
        mixed.append(val)
    
    # Step 3: Compress to fixed length (e.g., 32)
    hash_arr = [0] * size
    for i, val in enumerate(mixed):
        hash_arr[i % size] = (hash_arr[i % size] + val) % 256
    
    # Step 4: Convert to hexadecimal
    hash_hex = ''.join(f'{v:02x}' for v in hash_arr)
    return hash_hex[:size]  # ensure fixed size

# Set up Streamlit page
st.set_page_config(page_title="Custom Hash Function vs SHA-256", layout="wide")

# Title and description
st.title("🔒 Custom Hash Function vs SHA-256")
st.subheader("A web app to compare a custom hash function with SHA-256.")

# Sidebar with instructions
with st.sidebar:
    st.header("📚 Instructions")
    st.markdown("""
        1. **Enter** a string in the text box below.
        2. Click **Generate Hash** to see the custom hash and compare it with SHA-256.
        3. **Small input changes** lead to **drastic differences** in the hash.
    """)

# Input validation and text box
input_text = st.text_area("🔑 Enter the string to hash:", height=150, value="hello")

# Custom styling for the button
st.markdown("""
    <style>
    .stButton>button {
        background-color: #4CAF50; /* Green */
        color: white;
        padding: 10px 24px;
        border: none;
        border-radius: 8px;
        cursor: pointer;
        font-size: 16px;
    }
    .stTextArea textarea {
        font-family: 'Courier New', Courier, monospace;
    }
    </style>
""", unsafe_allow_html=True)

# Input validation: Check if the user input is empty
if input_text.strip() == "":
    st.warning("⚠️ Please enter a string to hash.")
else:
    # Button to trigger the hash generation
    if st.button("Generate Hash"):
        # Generate the custom hash
        custom_hashed = custom_hash(input_text)
        
        # Generate the SHA-256 hash using hashlib
        sha256_hashed = hashlib.sha256(input_text.encode()).hexdigest()[:32]
        
        # Display the results
        st.write(f"### Custom Hash for '{input_text}':")
        st.code(custom_hashed, language='text')
        
        st.write(f"### SHA-256 Hash for '{input_text}':")
        st.code(sha256_hashed, language='text')

        # Show a comparison
        if custom_hashed == sha256_hashed:
            st.success("✔️ The hashes match!")
        else:
            st.warning("❌ The hashes do not match!")

        # Visual separator
        st.markdown("---")

# Footer section with GitHub link
st.markdown("""
    ### By Adhiyaman Babu
    GitHub: [ Repository Link](https://github.com/Adhhiiiiiiii/custom-hash-streamlit)
""")
