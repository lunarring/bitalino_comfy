
import platform
import sys

from src.bitalino_receiver import BitalinoReceiver

class LRBitalinoReceiver:
    def __init__(self):
        self.bitalino = None
        
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "bitalino_mac_address": ("STRING", {"default": "BTH00:21:08:35:15:32"}),
                "acquisition_duration": ("INT", {"default": 3600*24}),  # duration of bitalino readout (seconds)
                "sampling_freq": ("INT", {"default": 10}),  # how many sample per second
                "channel_code": ("INT", {"default": 7}),  # 7 is A3
            },
        }
    
    @classmethod 
    def IS_CHANGED(self, bitalino_mac_address, acquisition_duration, sampling_freq, channel_code):
        return float("NaN")
            
    RETURN_TYPES = ("FLOAT", )
    RETURN_NAMES = ("conductivity", )
    FUNCTION = "get_value"
    OUTPUT_NODE = False
    CATEGORY = "LunarRing/black_boxes"
    
    def get_value(self, bitalino_mac_address, acquisition_duration, sampling_freq, channel_code):
        if self.bitalino is None:
            self.bitalino = BitalinoReceiver(bitalino_mac_address, acquisition_duration, sampling_freq, channel_code)
        
        conductivity_value = self.bitalino.get_last_value()

        return ([conductivity_value])
