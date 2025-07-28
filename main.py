import lmstudio as lms
import gradio as gr

# gemma models need an extensive system prompt ...
system_prompt = """You are a professional image annotator.
For each image you receive, you 
- give a title of maximum 64 characters, 
- a description with a maximum of 512 characters, 
- and a list of objects you identify in the images. 
You can use markdown to output the annotation. 
Constraints:
- Output the annotation only, no additional text.
- Describe the image on a factual level.
- Be as descriptive as possible while keeping the amount of characters in the limit."""

def analyze(image_path):
    model = lms.llm("gemma-3-4b-it-qat")
    # model = lms.llm("qwen2.5-vl-3b-instruct")
    # model = lms.llm("qwen2.5-omni-3b")
    image_handle = lms.prepare_image(image_path)
    chat = lms.Chat()

    chat.add_system_prompt(system_prompt)
    chat.add_user_message("Annotate this image.", images=[image_handle])
    prediction = model.respond(chat)
    return prediction

# simple interface
# demo = gr.Interface(fn=analyze, inputs=gr.Image(type="filepath"), outputs=gr.TextArea())

with gr.Blocks(title="Image Annotation App", theme=gr.themes.Ocean()) as demo: # type: ignore
    gr.HTML("<h1>Simple Gradio App for Image Annotation</h1>")
    with gr.Row():
        inp = gr.Image(label="Input Image", type="filepath", sources=["upload", "clipboard"], height=640)
        out = gr.Textbox(label="Annotation Output", max_lines=22)
    btn = gr.Button("Run")
    btn.click(fn=analyze, inputs=inp, outputs=out)

demo.launch()
