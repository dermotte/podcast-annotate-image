# How to create a Web Based AI App with Gradio

This is a sample project for showing a fast road to success for using image-text-to-text models for image annotation and Gradio for simple web interfaces. Using `uv` we created a project and a simple Gradio app in a few steps. We use [LM Studio](https://lmstudio.ai) in the background, so make sure you have it installed and running.

Use `<shift>-<ctrl>-p` and the Simple Browser command in VS Code to view the Gradio app in the editor.

# Steps for creating the project

1. Create project with `uv init`
2. Add the gradio library with `uv add gradio`
3. Add the openAI library with `uv add lmstudio`
4. Run LM Studio with a vision model, e.g., 
    - gemma-3-4b-it-qat for general use, 
    - lmstudio-community/medgemma-4b-it-GGUF for medical use, or
    - smolvlm-500m-instruct if you need a small model.