from .base_fal_api_flux_node import BaseFalAPIFluxNode
from .fal_api_flux_pro_node import FalAPIFluxProNode
import logging

logger = logging.getLogger(__name__)

class FalAPIFluxProV11Node(FalAPIFluxProNode):
    def __init__(self):
        super().__init__()
        self.set_api_endpoint("fal-ai/flux-pro/v1.1")

    @classmethod
    def INPUT_TYPES(cls):
        input_types = super().INPUT_TYPES()
        return input_types

    def prepare_arguments(self, **kwargs):
        arguments = super().prepare_arguments(**kwargs)
        return arguments

NODE_CLASS_MAPPINGS = {
    "FalAPIFluxProV11Node": FalAPIFluxProV11Node
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "FalAPIFluxProV11Node": "Fal API Flux Pro v1.1"
}