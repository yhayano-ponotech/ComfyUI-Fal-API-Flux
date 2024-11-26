from .base_fal_api_flux_node import BaseFalAPIFluxNode
from .fal_api_flux_pro_node import FalAPIFluxProNode
import logging
import torch

logger = logging.getLogger(__name__)

class FalAPIFluxProReduxNode(FalAPIFluxProNode):
    def __init__(self):
        super().__init__()
        self.set_api_endpoint("fal-ai/flux-pro/v1/redux")

    @classmethod
    def INPUT_TYPES(cls):
        input_types = super().INPUT_TYPES()
        # Add control image input
        input_types["required"].update({
            "image": ("IMAGE",),  # Accept input from another node
        })
        
        return input_types

    def prepare_arguments(self, image, **kwargs):
        # Get base arguments from parent class
        arguments = super().prepare_arguments(**kwargs)
        
        # Upload the control image and get its URL
        image_url = self.upload_image(image)
        logger.info(f"Uploaded target image. URL: {image_url}")
        
        # Update arguments with Canny-specific parameters
        arguments.update({
            "image_url": image_url
        })
        
        return arguments

NODE_CLASS_MAPPINGS = {
    "FalAPIFluxProReduxNode": FalAPIFluxProReduxNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "FalAPIFluxProReduxNode": "Fal API Flux Pro Redux"
}