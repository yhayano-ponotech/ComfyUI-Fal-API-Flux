from .base_fal_api_flux_node import BaseFalAPIFluxNode
from PIL import Image
import torch
import io
import base64
import fal_client
import logging
import numpy as np

logger = logging.getLogger(__name__)

class FalAPIFluxNodeWithControlNet(BaseFalAPIFluxNode):
    @classmethod
    def INPUT_TYPES(cls):
        input_types = super().INPUT_TYPES()
        input_types["optional"].update({
            "controlnet": ("CONTROLNET_CONFIG",),
            "controlnet_union": ("CONTROLNET_UNION_CONFIG",),
        })
        return input_types

    def prepare_arguments(self, prompt, image_size, num_inference_steps, guidance_scale, num_images, controlnet=None, controlnet_union=None, **kwargs):
        arguments = super().prepare_arguments(prompt, image_size, num_inference_steps, guidance_scale, num_images, **kwargs)
        
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
                    "control_image_url": self.upload_image(control["control_image_url"]),
                    "control_mode": control["control_mode"],
                    "conditioning_scale": control["conditioning_scale"]
                } for control in controlnet_union["controls"]]
            }]
            if controlnet_union["config_url"]:
                arguments["controlnet_unions"][0]["config_url"] = controlnet_union["config_url"]
            if controlnet_union["variant"]:
                arguments["controlnet_unions"][0]["variant"] = controlnet_union["variant"]

        return arguments

    def upload_image(self, image):
        try:
            # Convert PyTorch tensor to numpy array
            if isinstance(image, torch.Tensor):
                image = image.cpu().numpy()

            # Handle different shapes of numpy arrays
            if isinstance(image, np.ndarray):
                if image.ndim == 4 and image.shape[0] == 1:  # (1, H, W, 3) or (1, H, W, 1)
                    image = image.squeeze(0)
                
                if image.ndim == 3:
                    if image.shape[2] == 3:  # (H, W, 3) RGB image
                        pass
                    elif image.shape[2] == 1:  # (H, W, 1) grayscale
                        image = np.repeat(image, 3, axis=2)
                    elif image.shape[0] == 3:  # (3, H, W) RGB
                        image = np.transpose(image, (1, 2, 0))
                    elif image.shape[0] == 1:  # (1, H, W) grayscale
                        image = np.repeat(image.squeeze(0)[..., np.newaxis], 3, axis=2)
                elif image.shape == (1, 1, 1536):  # Special case for (1, 1, 1536) shape
                    image = image.reshape(32, 48)
                    image = np.repeat(image[..., np.newaxis], 3, axis=2)
                else:
                    raise ValueError(f"Unsupported image shape: {image.shape}")

                # Normalize to 0-255 range if not already
                if image.dtype != np.uint8:
                    image = (image - image.min()) / (image.max() - image.min()) * 255
                    image = image.astype(np.uint8)

                image = Image.fromarray(image)

            # Ensure image is in RGB mode
            if image.mode != 'RGB':
                image = image.convert('RGB')

            # Resize image if it's too large (optional, adjust max_size as needed)
            max_size = 1024  # Example max size
            if max(image.size) > max_size:
                image.thumbnail((max_size, max_size), Image.LANCZOS)

            # Convert PIL Image to bytes
            buffered = io.BytesIO()
            image.save(buffered, format="PNG")
            img_byte = buffered.getvalue()

            # Upload the image using fal_client
            url = fal_client.upload(img_byte, "image/png")
            logger.info(f"Image uploaded successfully. URL: {url}")
            return url
        except Exception as e:
            logger.error(f"Failed to process or upload image: {str(e)}")
            raise

NODE_CLASS_MAPPINGS = {
    "FalAPIFluxNodeWithControlNet": FalAPIFluxNodeWithControlNet
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "FalAPIFluxNodeWithControlNet": "Fal API Flux with ControlNet"
}