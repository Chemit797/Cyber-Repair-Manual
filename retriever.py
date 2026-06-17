import os
import json
import numpy as np
import jieba
from rank_bm25 import BM25Okapi
from sentence_transformers import SentenceTransformer
from typing import List, Tuple, Any

class Retriever:
    # Changed model to an English one
    def __init__(self, corpus_path: str, model_name: str = 'all-MiniLM-L6-v2', cache_dir: str = 'cache'):
        self.corpus_path = corpus_path
        self.cache_dir = cache_dir
        if not os.path.exists(cache_dir):
            os.makedirs(cache_dir)
            
        self.entries = []
        self._load_corpus()
        
        # Init BM25
        # For English, we can just split by space or use jieba, jieba handles english words ok
        tokenized_corpus = [doc['text'].lower().split() for doc in self.entries]
        self.bm25 = BM25Okapi(tokenized_corpus)
        
        # Init Sentence Transformer
        self.model = SentenceTransformer(model_name)
        self.embeddings = self._get_embeddings()

    def _load_corpus(self):
        with open(self.corpus_path, 'r', encoding='utf-8') as f:
            for line in f:
                if not line.strip(): continue
                data = json.loads(line)
                for paraphrase in data['symptom_text']:
                    entry = data.copy()
                    entry['text'] = paraphrase
                    self.entries.append(entry)

    def _get_embeddings(self):
        cache_file = os.path.join(self.cache_dir, 'corpus_embeddings_en.npy')
        if os.path.exists(cache_file):
            return np.load(cache_file)
        
        texts = [doc['text'] for doc in self.entries]
        print("Computing dense embeddings for the first time. Please wait...")
        embeddings = self.model.encode(texts, normalize_embeddings=True)
        np.save(cache_file, embeddings)
        return embeddings

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
            
        query_emb = self.model.encode([query_text], normalize_embeddings=True)[0]
        
        ranked_results = []
        seen_ids = set()
        
        for idx, bm25_score in candidates:
            doc_emb = self.embeddings[idx]
            sim = float(np.dot(query_emb, doc_emb))
            entry = self.entries[idx]
            
            if entry['id'] not in seen_ids:
                seen_ids.add(entry['id'])
                # Attach scores for UI transparency
                ranked_results.append({
                    "entry": entry,
                    "dense_score": sim,
                    "bm25_score": bm25_score,
                    "matched_text": entry['text']
                })
                
        ranked_results = sorted(ranked_results, key=lambda x: x["dense_score"], reverse=True)
        return ranked_results[:top_k]
