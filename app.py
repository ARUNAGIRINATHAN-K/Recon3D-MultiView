import streamlit as st
import os
import tempfile
from src.pipeline import ReconstructionPipeline

st.title("3D Object Reconstruction from 2D Images")

st.sidebar.header("Settings")
method = st.sidebar.selectbox("Feature Detection Method", ["SIFT", "ORB"])

uploaded_files = st.file_uploader("Upload Images", accept_multiple_files=True, type=['jpg', 'png', 'jpeg'])

if uploaded_files:
    st.write(f"Uploaded {len(uploaded_files)} images.")
    
    if st.button("Run Reconstruction"):
        with st.spinner("Processing..."):
            # Create a temporary directory to store uploaded images
            with tempfile.TemporaryDirectory() as temp_dir:
                data_dir = os.path.join(temp_dir, "images")
                os.makedirs(data_dir)
                
                # Save uploaded images
                for uploaded_file in uploaded_files:
                    file_path = os.path.join(data_dir, uploaded_file.name)
                    with open(file_path, "wb") as f:
                        f.write(uploaded_file.getbuffer())
                
                # Setup output directory
                # In a real app, this should be persistent or handled carefully
                # For demo, we use another temp dir or local folder
                output_dir = "output_streamlit"
                
                pipeline = ReconstructionPipeline(data_dir, output_dir)
                
                # Note: This requires COLMAP installed on the server/machine
                try:
                    pipeline.run()
                    st.success("Reconstruction complete!")
                    st.write(f"Results saved to {output_dir}")
                except Exception as e:
                    st.error(f"Reconstruction failed: {str(e)}")
                    st.warning("Ensure COLMAP is installed and added to system PATH.")

else:
    st.info("Please upload images to start.")
