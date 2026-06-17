import jieba
import jieba.posseg as pseg
from typing import List

class Query:
    def __init__(self, raw_text: str, device: str = None, symptoms: List[str] = None):
        self.raw_text = raw_text
        self.device = device
        self.symptoms = symptoms or []

class SymptomParser:
    def __init__(self, device_dict: str, symptom_dict: str):
        jieba.load_userdict(device_dict)
        jieba.load_userdict(symptom_dict)

    def parse(self, text: str) -> Query:
        # Convert to title case for device matching (e.g., 'flashlight' -> 'Flashlight')
        # However, for symptoms lower case is fine. Jieba is case sensitive for dictionary.
        # It's better to just use the original text for jieba, but let's normalize device names later.
        words = pseg.cut(text)
        device = None
        symptoms = []
        
        # We need a robust matching for device because of case sensitivity
        known_devices = {"flashlight": "Flashlight", "kettle": "Kettle", "coffee": "Coffee Machine", "fan": "Fan"}
        
        for word, flag in words:
            word_lower = word.lower()
            if not device:
                for k, v in known_devices.items():
                    if k in word_lower:
                        device = v
                        break
            
            if flag in ('SYMPTOM', 'COMPONENT', 'INDICATOR', 'ACTION'):
                symptoms.append(word.lower())
                
        # Fallback keyword search for devices if Jieba missed it due to casing
        text_lower = text.lower()
        if not device:
            for k, v in known_devices.items():
                if k in text_lower:
                    device = v
                    break
                    
        return Query(raw_text=text, device=device, symptoms=symptoms)

if __name__ == "__main__":
    parser = SymptomParser("device_dict.txt", "symptom_dict.txt")
    q = parser.parse("My Flashlight is broken and won't charge")
    print(f"Device: {q.device}, Symptoms: {q.symptoms}")
