from .fal_api_flux_pro_node import FalAPIFluxProNode
import logging
import torch

logger = logging.getLogger(__name__)

class FalAPIFluxProFillNode(FalAPIFluxProNode):
    def __init__(self):
        super().__init__()
        self.set_api_endpoint("fal-ai/flux-pro/v1/fill")

    @classmethod
    def INPUT_TYPES(cls):
        input_types = super().INPUT_TYPES()
        # Add control image input
        input_types["required"].update({
            "image": ("IMAGE",), 
            "mask_image": ("IMAGE",),
        })
        
        return input_types

    def prepare_arguments(self, image, mask_image, **kwargs):
        # Get base arguments from parent class
        arguments = super().prepare_arguments(**kwargs)
        
        # Upload the image and mask and get its URL
        image_url = self.upload_image(image)
        mask_image_url = self.upload_image(mask_image)
        logger.info(f"Uploaded target image. URL: {control_image_url}")
        logger.info(f"Uploaded mask image. URL: {control_image_url}")
        
        # Update arguments with Fill-specific parameters
        arguments.update({
            "image_url": control_image_url,
            "mask_url": mask_image_url
        })
        
        return arguments

NODE_CLASS_MAPPINGS = {
    "FalAPIFluxProFillNode": FalAPIFluxProFillNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "FalAPIFluxProFillNode": "Fal API Flux Pro Fill"
}