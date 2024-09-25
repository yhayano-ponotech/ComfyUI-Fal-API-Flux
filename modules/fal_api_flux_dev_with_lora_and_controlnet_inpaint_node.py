from .base_fal_api_flux_node import BaseFalAPIFluxNode
from .fal_api_flux_dev_with_lora_and_controlnet_image_to_image_node import FalAPIFluxDevWithLoraAndControlNetImageToImageNode
from PIL import Image
import torch
import io
import base64
import fal_client
import logging
import numpy as np

logger = logging.getLogger(__name__)

class FalAPIFluxDevWithLoraAndControlNetInpaintNode(FalAPIFluxDevWithLoraAndControlNetImageToImageNode):
    def __init__(self):
        super().__init__()
        self.set_api_endpoint("fal-ai/flux-general/inpainting")
        
    def set_api_endpoint(self, endpoint):
        super().set_api_endpoint(endpoint)
        
    @classmethod
    def INPUT_TYPES(cls):
        input_types = super().INPUT_TYPES()
        input_types["required"].update({
            "mask_image": ("IMAGE",),  # This makes it accept input from another node
        })
        return input_types

    def prepare_arguments(self, mask_image, **kwargs):
        arguments = super().prepare_arguments(**kwargs)
        
        # Upload the image and get the URL
        mask_url = self.upload_image(mask_image)
        print(f"Uploaded image to {mask_url}")
        
        arguments.update({
            "mask_url": mask_url,
        })

        return arguments

NODE_CLASS_MAPPINGS = {
    "FalAPIFluxDevWithLoraAndControlNetInpaintNode": FalAPIFluxDevWithLoraAndControlNetInpaintNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "FalAPIFluxDevWithLoraAndControlNetInpaintNode": "Fal API Flux with LoRA and ControlNet Inpaint"
}