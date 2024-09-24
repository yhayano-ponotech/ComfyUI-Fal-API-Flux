from .modules.fal_api_flux_dev_node import FalAPIFluxDevNode
from .modules.fal_api_flux_dev_image_to_image_node import FalAPIFluxDevImageToImageNode
from .modules.fal_api_flux_dev_with_lora_node import FalAPIFluxDevWithLoraNode
from .modules.fal_api_flux_dev_with_lora_image_to_image_node import FalAPIFluxDevWithLoraImageToImageNode
from .modules.fal_api_flux_dev_with_lora_and_controlnet_node import FalAPIFluxDevWithLoraAndControlNetNode
from .modules.fal_api_flux_dev_with_lora_and_controlnet_image_to_image_node import FalAPIFluxDevWithLoraAndControlNetImageToImageNode
from .modules.fal_api_flux_pro_node import FalAPIFluxProNode
from .modules.fal_api_flux_lora_config_node import FalAPIFluxLoraConfigNode
from .modules.fal_api_flux_controlnet_config_node import FalAPIFluxControlNetConfigNode
from .modules.fal_api_flux_controlnet_union_config_node import FalAPIFluxControlNetUnionConfigNode
from .modules.fal_api_flux_image_loader_config_node import FalAPIFluxImageLoaderConfigNode

NODE_CLASS_MAPPINGS = {
    "FalAPIFluxDevNode": FalAPIFluxDevNode,
    "FalAPIFluxDevImageToImageNode": FalAPIFluxDevImageToImageNode,
    "FalAPIFluxDevWithLoraNode": FalAPIFluxDevWithLoraNode,
    "FalAPIFluxDevWithLoraImageToImageNode": FalAPIFluxDevWithLoraImageToImageNode,
    "FalAPIFluxDevWithLoraAndControlNetNode": FalAPIFluxDevWithLoraAndControlNetNode,
    "FalAPIFluxDevWithLoraAndControlNetImageToImageNode": FalAPIFluxDevWithLoraAndControlNetImageToImageNode,
    "FalAPIFluxProNode": FalAPIFluxProNode,
    "FalAPIFluxLoraConfigNode": FalAPIFluxLoraConfigNode,
    "FalAPIFluxControlNetConfigNode": FalAPIFluxControlNetConfigNode,
    "FalAPIFluxControlNetUnionConfigNode": FalAPIFluxControlNetUnionConfigNode,
    "FalAPIFluxImageLoaderConfigNode": FalAPIFluxImageLoaderConfigNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "FalAPIFluxDevNode": "Fal API Flux Dev",
    "FalAPIFluxDevImageToImageNode": "Fal API Flux Dev Image-to-Image",
    "FalAPIFluxDevWithLoraNode": "Fal API Flux Dev with LoRA",
    "FalAPIFluxDevWithLoraImageToImageNode": "Fal API Flux Dev with LoRA Image-to-Image",
    "FalAPIFluxDevWithLoraAndControlNetNode": "Fal API Flux with LoRA and ControlNet",
    "FalAPIFluxDevWithLoraAndControlNetImageToImageNode": "Fal API Flux with LoRA and ControlNet Image-to-Image",
    "FalAPIFluxProNode": "Fal API Flux Pro",
    "FalAPIFluxLoraConfigNode": "Fal API Flux LoRA Config",
    "FalAPIFluxControlNetConfigNode": "Fal API Flux ControlNet Config",
    "FalAPIFluxControlNetUnionConfigNode": "Fal API Flux ControlNet Union Config",
    "FalAPIFluxDevImageToImageNode": "Fal API Flux Dev Image-to-Image",
    "FalAPIFluxImageLoaderConfigNode": "Fal API Flux Image Loader Config"
}

__all__ = [
    'FalAPIFluxDevNode', 
    'FalAPIFluxDevImageToImageNode', 
    'FalAPIFluxNodeWithControlNet', 
    'FalAPIFluxDevWithLoraImageToImageNode', 
    'FalAPIFluxDevWithLoraAndControlNetNode', 
    'FalAPIFluxDevWithLoraAndControlNetImageToImageNode', 
    'FalAPIFluxProNode', 
    'FalAPIFluxLoraConfigNode', 
    'FalAPIFluxControlNetConfigNode', 
    'FalAPIFluxControlNetUnionConfigNode', 
    'FalAPIFluxImageLoaderConfigNode'
]