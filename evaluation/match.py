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
    print(otter_emb.shape)
    sim_emb = embed(sim_word)
    cos_sim = nn.CosineSimilarity(dim=1)
    match_words = []
    for i in range(otter_emb.shape[0]):
        sim = cos_sim(otter_emb[i].unsqueeze(0), sim_emb)
        print(sim)
        match_word = sim_word[torch.argmax(sim).item()]
        match_words.append(match_word)
    return match_words

def change_code(code, idx):
    code_list = code.split("\"")
    otter_word = code_list[1]
    otter_word_list = otter_word.split('_')
    otter_word = '_'.join(otter_word_list[:-1])
    with open('./scene_object.json', 'r') as f:
        data = json.load(f)
    keys = sorted(list(data.keys()))
    sim_word = data[keys[idx]]
    otter_word = [otter_word]
    match_word = match(otter_word, sim_word)
    code[1] = "\"" + match_word[0] + "\""
    code_str = ''.join(code_list)
    with open('./action.py', 'w') as f:
        f.write(code_str)
    
    

if __name__ == "__main__":
    # otter_word = ["meat_abcd_150"]
    # sim_word = ["electrical_fridge_abcd", "bacon", "fridge_abcd"]
    # match(otter_word, sim_word)
    # with open('./action.py', 'r') as f:
    #     code = f.read()
    #     change_code(code, 1)
    all_data = {}
    with open('./scene_object.json', 'r') as f:
        data = json.load(f)
    for i in data.keys():
        words = data[i]
        all_word = []
        for word in words:
            if word == 'robot0':
                continue
            word_list = word.split('_')
            word_str = '_'.join(word_list[:-1])
            all_word.append(word_str)
        all_data[i] = all_word
    with open('./scene_object.json', 'w') as f:
        f.write(json.dumps(all_data))