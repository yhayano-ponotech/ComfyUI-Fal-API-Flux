from .base_fal_api_flux_node import BaseFalAPIFluxNode
from PIL import Image
import torch
import io
import base64
import fal_client
import logging
import numpy as np

logger = logging.getLogger(__name__)

class FalAPIFluxDevWithLoraAndControlNetNode(BaseFalAPIFluxNode):
    def __init__(self):
        super().__init__()
        self.set_api_endpoint("fal-ai/flux-general")
        
    def set_api_endpoint(self, endpoint):
        super().set_api_endpoint(endpoint)
        
    @classmethod
    def INPUT_TYPES(cls):
        input_types = super().INPUT_TYPES()
        input_types["optional"].update({
            "lora_1": ("LORA_CONFIG",),
            "lora_2": ("LORA_CONFIG",),
            "lora_3": ("LORA_CONFIG",),
            "lora_4": ("LORA_CONFIG",),
            "lora_5": ("LORA_CONFIG",),
            "controlnet": ("CONTROLNET_CONFIG",),
            "controlnet_union": ("CONTROLNET_UNION_CONFIG",),
        })
        return input_types

    def prepare_arguments(self, lora_1=None, lora_2=None, lora_3=None, lora_4=None, lora_5=None, 
                         controlnet=None, controlnet_union=None, **kwargs):
        arguments = super().prepare_arguments(**kwargs)
        
        # Collect all provided LoRA configurations
        loras = []
        for lora in [lora_1, lora_2, lora_3, lora_4, lora_5]:
            if lora is not None:
                loras.append(lora)
        
        if loras:
            arguments["loras"] = loras
            
        if controlnet:
            arguments["controlnets"] = [{
                "path": controlnet["path"],
                "control_image_url": self.upload_image(controlnet["control_image"]),
                "conditioning_scale": controlnet["conditioning_scale"]
            }]
            if controlnet["config_url"]:
                arguments["controlnets"][0]["config_url"] = controlnet["config_url"]
            if controlnet["variant"]:
                arguments["controlnets"][0]["variant"] = controlnet["variant"]

        if controlnet_union:
            arguments["controlnet_unions"] = [{
                "path": controlnet_union["path"],
                "controls": [{
                    "control_image_url": self.upload_image(control["control_image"]),
                    "control_mode": control["control_mode"],
                    "conditioning_scale": control["conditioning_scale"]
                } for control in controlnet_union["controls"]]
            }]
            if controlnet_union["config_url"]:
                arguments["controlnet_unions"][0]["config_url"] = controlnet_union["config_url"]
            if controlnet_union["variant"]:
                arguments["controlnet_unions"][0]["variant"] = controlnet_union["variant"]

        return arguments

NODE_CLASS_MAPPINGS = {
    "FalAPIFluxDevWithLoraAndControlNetNode": FalAPIFluxDevWithLoraAndControlNetNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "FalAPIFluxDevWithLoraAndControlNetNode": "Fal API Flux with LoRA and ControlNet"
}