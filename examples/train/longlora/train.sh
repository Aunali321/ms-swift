CUDA_VISIBLE_DEVICES=0 \
swift sft \
    --model_id_or_path LLM-Research/Meta-Llama-3.1-8B-Instruct \
    --sft_type longlora \
    --dataset longwriter-6k#1000 \
    --num_train_epochs 1 \
    --batch_size 1 \
    --weight_decay 0.1 \
    --learning_rate 1e-4 \
    --gradient_accumulation_steps 8 \
    --lora_rank 8 \
    --lora_alpha 32 \
    --lora_dropout_p 0.05 \
    --lora_target_modules ALL \
    --warmup_ratio 0.03 \
    --eval_steps 100 \
    --save_steps 100 \
    --save_total_limit 2 \
    --logging_steps 5