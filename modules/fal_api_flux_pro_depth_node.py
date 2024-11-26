from .fal_api_flux_pro_canny_node import FalAPIFluxProCannyNode
import logging

logger = logging.getLogger(__name__)

class FalAPIFluxProDepthNode(FalAPIFluxProCannyNode):
    def __init__(self):
        super().__init__()
        self.set_api_endpoint("fal-ai/flux-pro/v1/depth")

NODE_CLASS_MAPPINGS = {
    "FalAPIFluxProDepthNode": FalAPIFluxProDepthNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "FalAPIFluxProDepthNode": "Fal API Flux Pro Depth"
}