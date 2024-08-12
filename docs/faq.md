# FAQ

### 1. How do I install the roop extension?

While your pod is running and the Network Volume is attached:

#### Install the extension

```bash
source /workspace/venv/bin/activate
cd /workspace/stable-diffusion-webui/extensions
git clone --depth=1 https://github.com/ashleykleynhans/sd-webui-roop.git
cd /workspace/stable-diffusion-webui/extensions/sd-webui-roop
pip3 install -r requirements.txt
```

#### Download the model

```bash
mkdir -p /workspace/stable-diffusion-webui/models/roop
cd /workspace/stable-diffusion-webui/models/roop && \
wget https://huggingface.co/ashleykleynhans/inswapper/resolve/main/inswapper_128.onnx
```

Once you are done, you can terminate the pod.

### 2. How do I install InstantID

If you are doing a fresh install, then InstantID will already be installed.
However, if you installed the worker prior to 1 February 2024, you will need
to upgrade ControlNet and install the InstantID models as follows while your
pos is running and the Network Volume is attached:

#### Upgrade ControlNet

```bash
cd /workspace/stable-diffusion-webui/extensions/sd-webui-controlnet
git pull
source /workspace/venv/bin/activate
pip3 install -r requirements.txt
```

#### Download InstantID ControlNet Models

```bash
cd /workspace/stable-diffusion-webui/models/ControlNet
wget -O ip-adapter_instant_id_sdxl.bin "https://huggingface.co/InstantX/InstantID/resolve/main/ip-adapter.bin?download=true"
wget -O control_instant_id_sdxl.safetensors"https://huggingface.co/InstantX/InstantID/resolve/main/ControlNetModel/diffusion_pytorch_model.safetensors?download=true"
```

Once you are done, you can terminate the pod.