from .modules.fal_flux_node import FalAPIFluxNode
from .modules.fal_flux_lora_config_node import FalAPIFluxLoraConfigNode

NODE_CLASS_MAPPINGS = {
    "FalAPIFluxNode": FalAPIFluxNode,
    "FalAPIFluxLoraConfigNode": FalAPIFluxLoraConfigNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "FalAPIFluxNode": "Fal API Flux",
    "FalAPIFluxLoraConfigNode": "Fal API Flux LoRA Config"
}

__all__ = ['FalAPIFluxNode', 'FalAPIFluxLoraConfigNode']