import logging

from .base_fal_api_flux_node import BaseFalAPIFluxNode
from .fal_api_flux_pro_v11_node import FalAPIFluxProV11Node

logger = logging.getLogger(__name__)


class FalAPIFluxProV11UltraNode(FalAPIFluxProV11Node):
    """
    See https://fal.ai/models/fal-ai/flux-pro/v1.1-ultra/api
    """

    def __init__(self):
        super().__init__()
        self.set_api_endpoint("fal-ai/flux-pro/v1.1-ultra")

    @classmethod
    def INPUT_TYPES(cls):
        # get input types from Flux Pro 1.1
        input_types = super().INPUT_TYPES()

        # remove `width` and `height` from inputs
        # the 1.1 ultra API replaces these with `aspect_ratio`
        del (input_types["required"]["width"])
        del (input_types["required"]["height"])

        # remove `num_inference_steps` and `guidance_scale`
        del (input_types["required"]["num_inference_steps"])
        del (input_types["required"]["guidance_scale"])

        # add `aspect_ratio`
        input_types["required"]["aspect_ratio"] = (["16:9", "4:3", "21:9", "1:1", "3:4", "9:16", "9:21"],)

        # add `raw`
        input_types["required"]["raw"] = ("BOOLEAN", {"default": True})

        return input_types

    def prepare_arguments(self, prompt, aspect_ratio, num_images, safety_tolerance,
                          enable_safety_checker, raw, seed=None, **kwargs):
        # override from base since we don't have width and height
        if not self.api_key:
            raise ValueError("API key is not set. Please check your config.ini file.")

        arguments = {"prompt": prompt, "raw": raw, "num_images": num_images,
                     "enable_safety_checker": enable_safety_checker,
                     "safety_tolerance": safety_tolerance, "aspect_ratio": aspect_ratio}

        if seed is not None and seed != 0:
            arguments["seed"] = seed

        return arguments


NODE_CLASS_MAPPINGS = {
    "FalAPIFluxProV11UltraNode": FalAPIFluxProV11Node
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "FalAPIFluxProV11UltraNode": "Fal API Flux Pro v1.1 Ultra"
}
