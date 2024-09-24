from .modules.fal_flux_node import FalAPIFluxNode
from .modules.fal_api_flux_node_with_controlnet import FalAPIFluxNodeWithControlNet
from .modules.fal_flux_lora_config_node import FalAPIFluxLoraConfigNode
from .modules.fal_flux_controlnet_config_node import FalAPIFluxControlNetConfigNode
from .modules.fal_flux_controlnet_union_config_node import FalAPIFluxControlNetUnionConfigNode
from .modules.fal_flux_pro_node import FalAPIFluxProNode

NODE_CLASS_MAPPINGS = {
    "FalAPIFluxNode": FalAPIFluxNode,
    "FalAPIFluxNodeWithControlNet": FalAPIFluxNodeWithControlNet,
    "FalAPIFluxLoraConfigNode": FalAPIFluxLoraConfigNode,
    "FalAPIFluxControlNetConfigNode": FalAPIFluxControlNetConfigNode,
    "FalAPIFluxControlNetUnionConfigNode": FalAPIFluxControlNetUnionConfigNode,
    "FalAPIFluxProNode": FalAPIFluxProNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "FalAPIFluxNode": "Fal API Flux",
    "FalAPIFluxNodeWithControlNet": "Fal API Flux with ControlNet",
    "FalAPIFluxLoraConfigNode": "Fal API Flux LoRA Config",
    "FalAPIFluxControlNetConfigNode": "Fal API Flux ControlNet Config",
    "FalAPIFluxControlNetUnionConfigNode": "Fal API Flux ControlNet Union Config",
    "FalAPIFluxProNode": "Fal API Flux Pro"
}

__all__ = ['FalAPIFluxNode', 'FalAPIFluxNodeWithControlNet', 'FalAPIFluxLoraConfigNode', 'FalAPIFluxControlNetConfigNode', 'FalAPIFluxControlNetUnionConfigNode', 'FalAPIFluxProNode']