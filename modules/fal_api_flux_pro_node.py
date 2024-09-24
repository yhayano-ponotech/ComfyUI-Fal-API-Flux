from .base_fal_api_flux_node import BaseFalAPIFluxNode
import logging

logger = logging.getLogger(__name__)

class FalAPIFluxProNode(BaseFalAPIFluxNode):
    def __init__(self):
        super().__init__()
        self.set_api_endpoint("fal-ai/flux-pro")

    @classmethod
    def INPUT_TYPES(cls):
        input_types = super().INPUT_TYPES()
        input_types["required"]["safety_tolerance"] = (["1", "2", "3", "4", "5", "6"],)
        return input_types

    def prepare_arguments(self, prompt, image_size, num_inference_steps, guidance_scale, num_images, safety_tolerance, seed=None, **kwargs):
        arguments = super().prepare_arguments(prompt, image_size, num_inference_steps, guidance_scale, num_images, seed, **kwargs)
        arguments["safety_tolerance"] = safety_tolerance
        return arguments

NODE_CLASS_MAPPINGS = {
    "FalAPIFluxProNode": FalAPIFluxProNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "FalAPIFluxProNode": "Fal API Flux Pro"
}