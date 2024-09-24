import os
import hashlib
import folder_paths
from PIL import Image, ImageOps
import numpy as np
import torch

class FalAPIFluxImageLoaderConfigNode:
    @classmethod
    def INPUT_TYPES(s):
        input_dir = folder_paths.get_input_directory()
        files = [f for f in os.listdir(input_dir) if os.path.isfile(os.path.join(input_dir, f))]
        return {"required":
                    {"image": (sorted(files), {"image_upload": True})},
                }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "load_image"
    CATEGORY = "image"

    def load_image(self, image):
        image_path = folder_paths.get_annotated_filepath(image)
        return (image_path,)

    @classmethod
    def IS_CHANGED(s, image):
        image_path = folder_paths.get_annotated_filepath(image)
        m = hashlib.sha256()
        with open(image_path, 'rb') as f:
            m.update(f.read())
        return m.digest().hex()

    @classmethod
    def VALIDATE_INPUTS(s, image):
        if not folder_paths.exists_annotated_filepath(image):
            return "Invalid image file: {}".format(image)
        return True

NODE_CLASS_MAPPINGS = {
    "FalAPIFluxImageLoaderConfigNode": FalAPIFluxImageLoaderConfigNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "FalAPIFluxImageLoaderConfigNode": "Fal API Flux Image Loader Config"
}