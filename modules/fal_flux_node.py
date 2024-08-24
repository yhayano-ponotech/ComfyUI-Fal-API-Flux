from .base_fal_api_flux_node import BaseFalAPIFluxNode

class FalAPIFluxNode(BaseFalAPIFluxNode):
    @classmethod
    def INPUT_TYPES(cls):
        return super().INPUT_TYPES()

NODE_CLASS_MAPPINGS = {
    "FalAPIFluxNode": FalAPIFluxNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "FalAPIFluxNode": "Fal API Flux"
}