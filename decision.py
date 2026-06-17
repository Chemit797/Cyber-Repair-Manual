from typing import List, Dict, Any

class DecisionGate:
    def __init__(self, score_threshold: float = 0.55, margin_threshold: float = 0.03):
        self.score_threshold = score_threshold
        self.margin_threshold = margin_threshold

    def evaluate(self, ranked_results: List[Dict]) -> dict:
        if not ranked_results:
            return {"status": "low_confidence", "top_result": None, "candidates": []}
            
        top1 = ranked_results[0]
        top1_score = top1["dense_score"]
        
        if top1_score < self.score_threshold:
            return {"status": "low_confidence", "top_result": None, "candidates": ranked_results[:3]}
            
        if len(ranked_results) > 1:
            top2_score = ranked_results[1]["dense_score"]
            if (top1_score - top2_score) < self.margin_threshold:
                return {
                    "status": "need_clarify", 
                    "top_result": None, 
                    "candidates": ranked_results[:2]
                }
                
        return {"status": "confident", "top_result": top1, "candidates": []}

    def get_clarification_question(self, candidates: List[Dict]) -> dict:
        for cand in candidates:
            entry = cand["entry"]
            if entry.get('ask_questions'):
                return {"question": entry['ask_questions'][0], "source_entry_id": entry['id']}
        return None
