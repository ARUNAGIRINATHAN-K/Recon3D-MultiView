from src.feature_extraction import detect_features
from src.matching import match_features
from src.reconstruction import Reconstructor
import os

class ReconstructionPipeline:
    def __init__(self, data_dir, output_dir):
        self.data_dir = data_dir
        self.output_dir = output_dir
        self.reconstructor = Reconstructor(data_dir, output_dir)

    def run(self):
        print(f"Starting pipeline for images in {self.data_dir}")
        # In a real scenario, we might use the python feature extraction 
        # for visualization or custom matching, but rely on COLMAP for the heavy lifting.
        
        # Run COLMAP pipeline
        try:
            sparse_path = self.reconstructor.run_colmap_pipeline()
            print(f"Reconstruction available at {sparse_path}")
        except FileNotFoundError:
            print("Error: COLMAP executable not found in PATH.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Example usage
    pipeline = ReconstructionPipeline("data/images", "output")
    pipeline.run()
