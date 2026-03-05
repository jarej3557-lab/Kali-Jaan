#!/bin/bash
echo "🤖 KALI JAAN AI UNIVERSE INSTALLATION STARTING..."

# 1. Essential AI Libraries
sudo apt update && sudo apt install -y python3-pip git-lfs
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
pip3 install transformers diffusers accelerate openai-whisper langchain

# 2. Ollama Install (Isse aap Llama 3, Mistral jaise bade AI bina internet ke chala sakte hain)
curl -fsSL https://ollama.com/install.sh | sh

# 3. Mass AI Tool Downloader (Top Hacking & Analysis AI)
mkdir -p ~/kali_jaan/ai_tools
cd ~/kali_jaan/ai_tools
git clone https://github.com/vinta/awesome-python # AI & Python resource list
git clone https://github.com/ollama/ollama-python
git clone https://github.com/huggingface/transformers

echo "✅ SHASHI BHAI, DUNIYA KE SARE AI TOOLS KA BASE READY HAI!"
echo "💡 Ab aap 'ollama run llama3' bolenge to AI chalne lagega."
