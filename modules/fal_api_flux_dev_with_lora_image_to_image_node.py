from .base_fal_api_flux_node import BaseFalAPIFluxNode
from .fal_api_flux_dev_with_lora_node import FalAPIFluxDevWithLoraNode
import fal_client
import logging
import os

logger = logging.getLogger(__name__)

class FalAPIFluxDevWithLoraImageToImageNode(FalAPIFluxDevWithLoraNode):
    def __init__(self):
        super().__init__()
        self.set_api_endpoint("fal-ai/flux-lora/image-to-image")
        
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
    "FalAPIFluxDevWithLoraImageToImageNode": FalAPIFluxDevWithLoraImageToImageNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "FalAPIFluxDevWithLoraImageToImageNode": "Fal API Flux Dev with LoRA Image-to-Image"
}