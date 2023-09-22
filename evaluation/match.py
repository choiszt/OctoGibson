from transformers import BertTokenizer, BertModel
import torch
import torch.nn as nn
import json

def embed(words):
    # Initialize the BERT tokenizer and model
    tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
    model = BertModel.from_pretrained("bert-base-uncased")

    # Initialize an empty list to store word embeddings
    word_embeddings = []

    # Iterate through the list of words
    for word in words:
        # Tokenize the word
        inputs = tokenizer(word, padding=True, truncation=True, return_tensors="pt")
        
        # Forward pass: obtain model outputs
        with torch.no_grad():
            outputs = model(**inputs)
        
        # Extract the hidden states (last layer)
        hidden_states = outputs.last_hidden_state
        
        # The word could be broken into multiple sub-words; take the mean of the embeddings
        mean_embedding = torch.mean(hidden_states, dim=1).squeeze()
        
        # Append the mean embedding to the list
        word_embeddings.append(mean_embedding)

    word_embeddings = torch.stack(word_embeddings, dim=0)
    return word_embeddings
    # Now word_embeddings contains the BERT embeddings for each word in the list
    # You can proceed to use these for matching using algorithms like the Hungarian algorithm
    
def match(otter_word, sim_word):
    otter_emb = embed(otter_word)
    sim_emb = embed(sim_word)
    cos_sim = nn.CosineSimilarity(dim=1)
    match_words = []
    for i in range(otter_emb.shape[0]):
        sim = cos_sim(otter_emb[i].unsqueeze(0), sim_emb)
        print(sim)
        match_word = sim_word[torch.argmax(sim).item()]
        match_words.append(match_word)
    return match_words
    
    

if __name__ == "__main__":
    otter_word = ["meat_0"]
    sim_word = ["electrical_fridge_abcd_0", "bacon_150", "fridge_abcd_0"]
    match(otter_word, sim_word)