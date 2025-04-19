from typing import Dict
from model import *

class InMemoryRepository():
    
    _vocab: Dict[str, Word] = None
    _counters: list[Counter] = None  

    def __init__(self):
        self._vocab = {}
        self._counters = []
                
    def is_word_exists(self, value: str) -> bool:
        return value in self._vocab

    def get_word(self, value: str) -> Word:
        return self._vocab[value]
        
    def get_translation(self, value: str) -> str:
        return self.get_word(value).translation

    def add_word(self, word: Word):
        self._vocab[word.value] = word