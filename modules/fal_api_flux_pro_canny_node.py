from .base_fal_api_flux_node import BaseFalAPIFluxNode
from .fal_api_flux_pro_node import FalAPIFluxProNode
import logging
import torch

logger = logging.getLogger(__name__)

class FalAPIFluxProCannyNode(FalAPIFluxProNode):
    def __init__(self):
        super().__init__()
        self.set_api_endpoint("fal-ai/flux-pro/v1/canny")

    @classmethod
    def INPUT_TYPES(cls):
        input_types = super().INPUT_TYPES()
        # Add control image input
        input_types["required"].update({
            "control_image": ("IMAGE",),  # Accept input from another node
        })
        
        return input_types

    def prepare_arguments(self, control_image, **kwargs):
        # Get base arguments from parent class
        arguments = super().prepare_arguments(**kwargs)
        
        # Upload the control image and get its URL
        control_image_url = self.upload_image(control_image)
        logger.info(f"Uploaded control image. URL: {control_image_url}")
        
        # Update arguments with Canny-specific parameters
        arguments.update({
            "control_image_url": control_image_url
        })
        
        # Remove width and height if they exist
        arguments.pop("width", None)
        arguments.pop("height", None)
        
        return arguments

NODE_CLASS_MAPPINGS = {
    "FalAPIFluxProCannyNode": FalAPIFluxProCannyNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "FalAPIFluxProCannyNode": "Fal API Flux Pro Canny"
}