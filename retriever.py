import os
import json
import numpy as np
import jieba
from rank_bm25 import BM25Okapi
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from typing import List, Tuple, Any

class Retriever:
    def __init__(self, corpus_path: str, cache_dir: str = 'cache'):
        self.corpus_path = corpus_path
        self.cache_dir = cache_dir
        if not os.path.exists(cache_dir):
            os.makedirs(cache_dir)
            
        self.entries = []
        self._load_corpus()
        
        # Init BM25 (Pure statistical, no pre-training)
        tokenized_corpus = [doc['text'].lower().split() for doc in self.entries]
        self.bm25 = BM25Okapi(tokenized_corpus)
        
        # Init TF-IDF (Pure statistical from custom corpus, no pre-training!)
        self.vectorizer = TfidfVectorizer()
        texts = [doc['text'] for doc in self.entries]
        self.tfidf_matrix = self.vectorizer.fit_transform(texts)

    def _load_corpus(self):
        with open(self.corpus_path, 'r', encoding='utf-8') as f:
            for line in f:
                if not line.strip(): continue
                data = json.loads(line)
                for paraphrase in data['symptom_text']:
                    entry = data.copy()
                    entry['text'] = paraphrase
                    self.entries.append(entry)

    def search(self, query_text: str, device_filter: str = None, top_k: int = 3) -> List[dict]:
        tokenized_query = query_text.lower().split()
        bm25_scores = self.bm25.get_scores(tokenized_query)
        
        candidates = []
        for i, doc in enumerate(self.entries):
            if device_filter and doc['device'] != device_filter:
                continue
            candidates.append((i, bm25_scores[i]))
            
        candidates = sorted(candidates, key=lambda x: x[1], reverse=True)[:10]
        
        if not candidates:
            return []
            
        query_vec = self.vectorizer.transform([query_text])
        
        ranked_results = []
        seen_ids = set()
        
        for idx, bm25_score in candidates:
            doc_vec = self.tfidf_matrix[idx]
            sim = float(cosine_similarity(query_vec, doc_vec)[0][0])
            entry = self.entries[idx]
            
            if entry['id'] not in seen_ids:
                seen_ids.add(entry['id'])
                # Attach scores for UI transparency
                ranked_results.append({
                    "entry": entry,
                    "dense_score": sim, # Kept as dense_score for UI compatibility
                    "bm25_score": bm25_score,
                    "matched_text": entry['text']
                })
                
        ranked_results = sorted(ranked_results, key=lambda x: x["dense_score"], reverse=True)
        return ranked_results[:top_k]
