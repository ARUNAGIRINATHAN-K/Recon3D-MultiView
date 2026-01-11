import subprocess
import os
import open3d as o3d

class Reconstructor:
    def __init__(self, data_dir, output_dir):
        self.data_dir = data_dir
        self.output_dir = output_dir
        self.database_path = os.path.join(output_dir, "database.db")
        
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

    def run_colmap_pipeline(self):
        """
        Run the COLMAP pipeline: feature extractor, matcher, mapper.
        Assumes 'colmap' is in the system PATH.
        """
        # 1. Feature extraction
        print("Running Feature Extraction...")
        subprocess.check_call([
            "colmap", "feature_extractor",
            "--database_path", self.database_path,
            "--image_path", self.data_dir
        ])

        # 2. Exhaustive match
        print("Running Feature Matching...")
        subprocess.check_call([
            "colmap", "exhaustive_matcher",
            "--database_path", self.database_path
        ])

        # 3. Mapper (Sparse Reconstruction)
        print("Running Sparse Reconstruction...")
        sparse_dir = os.path.join(self.output_dir, "sparse")
        if not os.path.exists(sparse_dir):
            os.makedirs(sparse_dir)
            
        subprocess.check_call([
            "colmap", "mapper",
            "--database_path", self.database_path,
            "--image_path", self.data_dir,
            "--output_path", sparse_dir
        ])
        
        print("Sparse reconstruction complete.")
        return sparse_dir

    def visualize_point_cloud(self, ply_path):
        pcd = o3d.io.read_point_cloud(ply_path)
        o3d.visualization.draw_geometries([pcd])
