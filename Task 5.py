import gradio as gr

def square_number(n):
    return n ** 2

demo = gr.Interface(fn=square_number, inputs="number", outputs="number")
demo.launch()