import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("PyThaiNLP/GPTmodel")

model = AutoModelForCausalLM.from_pretrained("PyThaiNLP/GPTmodel")

# WIP
