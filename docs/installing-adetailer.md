# Install the After Detailer extension for A1111

> [!NOTE]
> This only applies if you have already installed the worker
> on your Network volume previously.

1. Deploy a pod with your network volume attached.
2. Start a terminal.
3. Run the following commands from the terminal:
   ```bash
   # Install After Detailer extension
   source /workspace/venv/bin/activate
   cd /workspace/stable-diffusion-webui
   git clone --depth=1 https://github.com/Bing-su/adetailer.git extensions/adetailer
   cd /workspace/stable-diffusion-webui/extensions/adetailer
   python3 -m install
    
   # Update A1111 configs
   cd /workspace/stable-diffusion-webui
   rm webui-user.sh config.json ui-config.json
   wget https://raw.githubusercontent.com/ashleykleynhans/runpod-worker-a1111/main/webui-user.sh
   wget https://raw.githubusercontent.com/ashleykleynhans/runpod-worker-a1111/main/config.json
   wget https://raw.githubusercontent.com/ashleykleynhans/runpod-worker-a1111/main/ui-config.json
   ```
