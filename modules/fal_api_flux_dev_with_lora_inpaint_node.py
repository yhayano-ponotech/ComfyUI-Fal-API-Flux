from .base_fal_api_flux_node import BaseFalAPIFluxNode
from .fal_api_flux_dev_with_lora_image_to_image_node import FalAPIFluxDevWithLoraImageToImageNode
import fal_client
import logging
import os

logger = logging.getLogger(__name__)

class FalAPIFluxDevWithLoraInpaintNode(FalAPIFluxDevWithLoraImageToImageNode):
    def __init__(self):
        super().__init__()
        self.set_api_endpoint("fal-ai/flux-lora/inpainting")
        
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
    "FalAPIFluxDevWithLoraInpaintNode": FalAPIFluxDevWithLoraInpaintNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "FalAPIFluxDevWithLoraInpaintNode": "Fal API Flux Dev with LoRA Inpaint"
}