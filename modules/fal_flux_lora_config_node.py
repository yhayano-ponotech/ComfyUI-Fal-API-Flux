class FalAPIFluxLoraConfigNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "lora_url": ("STRING", {
                    "multiline": False,
                    "default": "https://example.com/path/to/lora.safetensors"
                }),
                "scale": ("FLOAT", {
                    "default": 1.0,
                    "min": 0.1,
                    "max": 2.0,
                    "step": 0.1
                }),
            }
        }

    RETURN_TYPES = ("LORA_CONFIG",)
    FUNCTION = "configure_lora"
    CATEGORY = "image generation"

    def configure_lora(self, lora_url, scale):
        if not lora_url.startswith(('http://', 'https://')):
            raise ValueError("Invalid LoRA URL. Please enter a valid HTTP or HTTPS URL.")

        return ({"path": lora_url, "scale": float(scale)},)

NODE_CLASS_MAPPINGS = {
    "FalAPIFluxLoraConfigNode": FalAPIFluxLoraConfigNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "FalAPIFluxLoraConfigNode": "Fal API Flux LoRA Config"
}