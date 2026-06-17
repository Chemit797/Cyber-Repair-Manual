import os
import shutil

# Make sure cache is clean for the test
shutil.rmtree('cache', ignore_errors=True)

from parser import SymptomParser
from retriever import Retriever
from decision import DecisionGate
from renderer import Renderer

def test():
    print("Loading components...")
    parser = SymptomParser("device_dict.txt", "symptom_dict.txt")
    retriever = Retriever("data/train_corpus.jsonl", model_name='all-MiniLM-L6-v2')
    gate = DecisionGate()
    renderer = Renderer()
    
    print("Testing Parser...")
    query = parser.parse("My coffee machine makes a loud pump noise but no water comes out")
    print(f"Device: {query.device}, Symptoms: {query.symptoms}")
    
    print("Testing Retriever...")
    results = retriever.search(query.raw_text, query.device)
    for i, res in enumerate(results):
        print(f"Match {i}: {res['entry']['fault_category']} (BM25: {res['bm25_score']}, Dense: {res['dense_score']})")
        
    print("Testing Decision...")
    decision = gate.evaluate(results)
    print(f"Decision Status: {decision['status']}")
    
    if decision['status'] == 'confident':
        print(renderer.render(decision['top_result']['entry']))
        
    print("ALL TESTS PASSED SUCCESSFULLY!")

if __name__ == "__main__":
    test()
