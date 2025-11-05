# app.py
import streamlit as st
import hashlib

# -----------------------------
# Custom Hash Function
# -----------------------------
def custom_hash(input_string, hash_size=32):
    hash_value = 0
    for char in input_string:
        char_value = ord(char)
        hash_value = (hash_value << 5) + hash_value + char_value  # mixing step
        hash_value = hash_value % (10 ** hash_size)  # modular compression
    return hex(hash_value)[2:].zfill(hash_size)  # hex + zero-fill


# -----------------------------
# SHA-256 Hash Function
# -----------------------------
def sha256_hash(input_string):
    return hashlib.sha256(input_string.encode()).hexdigest()


# -----------------------------
# Streamlit App UI
# -----------------------------
st.set_page_config(page_title="Custom Hash vs SHA-256", page_icon="🔒", layout="centered")

st.title("🔐 Custom Hash Algorithm vs SHA-256")
st.write("**By: Priyanksha Das**")
st.markdown("---")

# Input text box
input_text = st.text_area("Enter text to hash:", value="hello", height=150)

# Compute hashes
custom_output = custom_hash(input_text)
sha256_output = sha256_hash(input_text)

# Display outputs
st.subheader("🧮 Hash Results")
col1, col2 = st.columns(2)
with col1:
    st.write("### Custom Hash Output:")
    st.code(custom_output, language="text")
with col2:
    st.write("### SHA-256 Output:")
    st.code(sha256_output, language="text")

# Demonstrate difference for small input change
st.markdown("---")
st.subheader("🔍 Small Change Demonstration")

# Input with slight change
slight_change = input_text + "!"
custom_changed = custom_hash(slight_change)
sha256_changed = sha256_hash(slight_change)

st.write(f"Original Input: `{input_text}`")
st.write(f"Modified Input: `{slight_change}`")

st.write("### Custom Hash Comparison")
st.code(f"Original: {custom_output}\nChanged : {custom_changed}")

st.write("### SHA-256 Comparison")
st.code(f"Original: {sha256_output}\nChanged : {sha256_changed}")

st.markdown("---")
st.success("✅ Same input → same hash; Small change → drastically different hash!")
st.info("Compare how both custom and SHA-256 behave with input changes.")

# Footer
st.markdown("""
---
**Project Summary**
- Implements a custom hash function using ASCII manipulation, shifts, and modular arithmetic.
- Compares it with SHA-256 using Python’s hashlib.
- Demonstrates hashing fundamentals visually.

**Developed by:** Adhiyaman B
""")
