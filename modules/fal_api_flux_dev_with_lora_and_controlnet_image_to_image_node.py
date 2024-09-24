from .base_fal_api_flux_node import BaseFalAPIFluxNode
from .fal_api_flux_dev_with_lora_and_controlnet_node import FalAPIFluxDevWithLoraAndControlNetNode
from PIL import Image
import torch
import io
import base64
import fal_client
import logging
import numpy as np

logger = logging.getLogger(__name__)

class FalAPIFluxDevWithLoraAndControlNetImageToImageNode(FalAPIFluxDevWithLoraAndControlNetNode):
    def __init__(self):
        super().__init__()
        self.set_api_endpoint("fal-ai/flux-general/image-to-image")
        
    def set_api_endpoint(self, endpoint):
        super().set_api_endpoint(endpoint)
        
    @classmethod
    def INPUT_TYPES(cls):
        input_types = super().INPUT_TYPES()
        input_types["required"].update({
            "image": ("IMAGE",),  # This makes it accept input from another node
            "strength": ("FLOAT", {"default": 0.8, "min": 0.0, "max": 1.0}),
        })
        return input_types

    def prepare_arguments(self, image, strength, **kwargs):
        arguments = super().prepare_arguments(**kwargs)
        
        # Upload the image and get the URL
        image_url = self.upload_image(image)
        print(f"Uploaded image to {image_url}")
        
        arguments.update({
            "image_url": image_url,
            "strength": strength,
        })

        return arguments

NODE_CLASS_MAPPINGS = {
    "FalAPIFluxDevWithLoraAndControlNetImageToImageNode": FalAPIFluxDevWithLoraAndControlNetImageToImageNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "FalAPIFluxDevWithLoraAndControlNetImageToImageNode": "Fal API Flux with LoRA and ControlNet Image-to-Image"
}