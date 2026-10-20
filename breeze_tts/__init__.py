"""Breeze TTS 2 inference code, packaged for installation (breeze-tts-packaged)."""

from pathlib import Path

PACKAGE_ROOT = Path(__file__).resolve().parent

# Warmup profile for the fast (CUDA Graph / torch.compile) inference path.
FAST_CONFIG_PATH = PACKAGE_ROOT / "configs" / "fast.json"
