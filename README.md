## Offline Llama OCR

### Step 1: Download Ollama
Download Ollama: [link](https://ollama.com/download)

In your terminal, run the following commands:
```
ollama pull llama3.2-vision
ollama serve
```

Navigate to `localhost:10434`. You should see a message like `Ollama is ready`.

### Step 2: Download Python and the Required Packages
Download Python: [link](https://www.python.org/downloads/)

How to Download Packages: [link](https://packaging.python.org/en/latest/tutorials/installing-packages/)

#### Download Pillow and requests
In your terminal, run the following commands:
```
pip install Pillow
pip install requests
```

### Step 3: Run the code
If you haven't already, clone the github repo:

`git clone https://github.com/jpat64/offline-ocr-llama.git`

**Note:** Each of the remaining steps can be performed without Internet access!

Enter the following command in the temrinal:
```
python3 ocr.py
```

Soon, you will get a response from the ML model! It will happen in the terminal window.

You can change which file is viewed by editing line 34 of `ocr.py`

**Note:** I've found the OCR process to take minutes at a time. So, be patient!
