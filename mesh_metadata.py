import sys
import json
import trimesh


def process_mesh(file_path, output_metadata="metadata.json"):
    """Load mesh, rename parts, and export metadata as JSON."""
    mesh = trimesh.load(file_path)

    renamed_parts = {}
    for i, geom_name in enumerate(mesh.geometry.keys()):
        new_name = f"part_{i}"
        renamed_parts[new_name] = {
            "original_name": geom_name,
            "vertices": len(mesh.geometry[geom_name].vertices),
            "faces": len(mesh.geometry[geom_name].faces),
        }

    with open(output_metadata, "w") as f:
        json.dump(renamed_parts, f, indent=4)

    print(
        f"Processed {len(renamed_parts)} parts. "
        f"Metadata saved to {output_metadata}."
    )


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python mesh_metadata.py <mesh_file>")
    else:
        process_mesh(sys.argv[1])
