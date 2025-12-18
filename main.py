import open3d as o3d
import numpy as np
import sys
import os

def main():
    input_file = "Dusseldorf.ply"
    output_file_full = "Dusseldorf_full.ply"
    output_preview = "Dusseldorf_preview.ply"

    # 1. Load Data
    print(f"Loading {input_file}...")
    if not os.path.exists(input_file):
        print("Error: File not found. Did you rename it to 'input.ply'?")
        return

    pcd = o3d.io.read_point_cloud(input_file)
    original_count = len(pcd.points)
    print(f"Loaded {original_count:,} points.")

    # 2. Downsample
    if original_count > 1000000:
        print(f"Data is huge ({original_count:,}). Downsampling for processing...")
        pcd_proc = pcd.voxel_down_sample(voxel_size=0.05)
        print(f"Processing cloud reduced to {len(pcd_proc.points):,} points.")
    else:
        pcd_proc = pcd

    # 3. Floor detection (RANSAC)
    print("Detecting Floor")
    plane_model , inliers = pcd_proc.segment_plane(distance_threshold = 0.04, ransac_n = 3, num_iterations = 1000)
    [a, b, c, d] = plane_model
    print(f"Floor Equation: {a:.2f}x + {b:.2f}y + {c:.2f}z + {d:.2f} = 0")

    # 4. Color
    floor_cloud = pcd_proc.select_by_index(inliers)
    room_cloud = pcd_proc.select_by_index(inliers, invert=True)
    floor_cloud.paint_uniform_color([1, 0, 0])       # RED Floor
    room_cloud.paint_uniform_color([0.8, 0.8, 0.8])  # GREY Room

    # 5. Height
    all_z_values = np.asarray(pcd_proc.points)[:, 1]
    floor_z = np.percentile(all_z_values, 1)
    max_z = np.percentile(all_z_values, 99)
    height = max_z - floor_z
    print(f"Estimated Room Height: {height:.2f} meters")

    # 6. Save Preview
    print(f"Saving preview to {output_preview}...")
    combined = floor_cloud + room_cloud
    o3d.io.write_point_cloud(output_preview, combined)
    
    print("-" * 30)
    print("DONE!")

if __name__ == "__main__":
    main()