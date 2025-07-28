# Image Annotation with Gradio and Multimodal AI

This is a sample project demonstrating a fast and effective way to use image-text-to-text models for image annotation, combined with Gradio for simple web interfaces. Using `uv`, we created a project and a simple Gradio app in just a few steps. We use [LM Studio](https://lmstudio.ai) in the background, so make sure you have it installed and running.

You can use `<shift>-<ctrl>-p>` and the Simple Browser command in VS Code to view the app in the editor.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/podcast-annotate-image.git
   ```
2. Install dependencies:
   ```
   uv sync
   ```
3. Start LM Studio (see instructions below).
4. Run the Gradio app:
   ```
   uv run main.py
   ```

### LM Studio

Download and install [LM Studio](https://lmstudio.ai). Then search for a model that is (i) runnable on your device, and (ii) supports vision. Good starting points are:
- `qwen2.5-omni-3b`
- `gemma-3-4b-it-qat`
- `smolvlm-500m-instruct`

In the developer tab, allow connections to the server. Make sure the model is running and accessible (default port is usually 1234).

## Usage

Once the app is running, open the provided local URL in your browser. Upload an image, and the model will generate an annotation or description for it.

## Steps

This series is part of the preparation for the Health, AI, and Gamification Hackathon, or in short, HIGH. It’s taking place at the ACM Multimedia 2025 conference in Dublin. We're creating these projects to help participants like you gear up for this exciting 48-hour event where we'll be crafting innovative games to address global health challenges using multimodal AI. If you're hearing about this event for the first time, please check out our web page and our Discord server! We'd love to have you there!

🌍 [Health, AI & Gamification Hackathon (HIGH)](https://acmmm2025.org/call-for-hackathon-participation/)