# Run ChatWithPDF with Ollama on Windows

Ollama runs both models locally. ChatWithPDF uses its OpenAI-compatible interface and sends requests to `127.0.0.1:11434` in Ollama mode. This mode uses no OpenAI API credits or real API key.

1. Install and open [Ollama for Windows](https://ollama.com/download/windows).
2. Open PowerShell in the folder with the latest `app.py`. If you downloaded an older ZIP, get the current version from GitHub.
3. Download the models and confirm they appear in the local list.

   ```powershell
   ollama pull nomic-embed-text
   ollama pull qwen2.5:3b
   ollama list
   ```

4. If the project folder has no `.venv` yet, install the dependencies.

   ```powershell
   py -m venv .venv
   .\.venv\Scripts\python.exe -m pip install -r requirements.txt
   ```

5. Stop any running ChatWithPDF instance with **Ctrl+C**. In PowerShell, select the local provider and start the app.

   ```powershell
   $env:CHATWITHPDF_PROVIDER = "ollama"
   .\.venv\Scripts\python.exe app.py
   ```

6. Open the Gradio URL printed in PowerShell. Upload a PDF with selectable text, click **Process PDF**, and then **Ask question**. With the Data Analyst Interview Questions and Answers PDF, ask what formula the guide uses to break down sales. Expect **Sales = number of orders × average order value**. Ask for the exact dollar loss in the 20% decline example to check whether the app identifies missing information.

If the app reports a connection error, open Ollama and retry. If it reports a missing model, rerun the matching `ollama pull` command. Model downloads require internet access. Local response speed depends on your computer.

To switch back, stop the app, run `$env:CHATWITHPDF_PROVIDER = "openai"`, and restart it with your OpenAI key configured locally. Process the PDF again after switching providers.

[Ollama Windows guide](https://docs.ollama.com/windows) · [OpenAI compatibility](https://docs.ollama.com/api/openai-compatibility)
