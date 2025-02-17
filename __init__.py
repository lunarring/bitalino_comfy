IMPORT_ERROR_MESSAGE = "Lunar Ring Nodes: failed to import"
NODE_CLASS_MAPPINGS = {}

try:
    from .comfy.bitalino_receiver import LRBitalinoReceiver
    NODE_CLASS_MAPPINGS["LR BitalinoReceiver"] = LRBitalinoReceiver
except Exception as e:
    print(f"{IMPORT_ERROR_MESSAGE} Bitalino Receiver: {e}")

