# Fragmento de config LMI para vLLM con speculative decoding
engine = "Python"
option.model_id = "meta-llama/Llama-3-8B-Instruct"
option.dtype = "bfloat16"
option.tensor_parallel_degree = 1

# Pinche (draft): 5-10× más rápido que el chef
option.speculative_model = "meta-llama/Llama-3.2-1B-Instruct"
option.num_speculative_tokens = 5
option.speculative_draft_model_quantization = "fp16"

# Continuous batching (la cinta sincronizada)
option.max_num_seqs = 256
option.max_model_len = 8192
option.gpu_memory_utilization = 0.90