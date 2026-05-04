from tkinter import *
from tkinter import filedialog
from PyPDF2 import PdfReader
from openai import OpenAI

client = OpenAI(
    api_key="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")

# create workspace
ws = Tk()
ws.title("Lecture-to-Notes Summarizer")
ws.geometry("800x650")

# global variable for selected file
selected_file = ""


# function to upload pdf
def upload_pdf():
    global selected_file
    selected_file = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])

    if selected_file != "":
        fileLb.config(text=selected_file)
    else:
        fileLb.config(text="No file selected")

    # function to read pdf


def read_pdf(file_path):
    text = ""
    reader = PdfReader(file_path)
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text is not None:
            text = text + page_text
    return text


# function to generate summary
def generate_summary():
    summaryTxt.delete("1.0", END)

    if selected_file == "":
        summaryTxt.insert(END, "Please upload a PDF file first.")
        return
    elif lengthTf.get() == "":
        summaryTxt.insert(END, "Please enter summary length: short, medium, or long.")
        return

    length = lengthTf.get().lower()

    if length not in ("short", "medium", "long"):
        summaryTxt.insert(END, "Please enter short, medium, or long.")
        return

    length_instructions = {
        "short": "Write a SHORT summary (2-3 sentences).",
        "medium": "Write a MEDIUM summary (1-2 paragraphs).",
        "long": "Write a LONG detailed summary (3-4 paragraphs).",
    }

    text = read_pdf(selected_file)

    if text == "":
        summaryTxt.insert(END, "No readable text found in the PDF.")
        return

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": (
                    f"You are a helpful study assistant. "
                    f"{length_instructions[length]} "
                    f"Summarize the following lecture content into clear notes:\n\n{text}"
                )
            }
        ]
    )

    summary = response.choices[0].message.content
    summaryTxt.insert(END, summary)


# function to clear everything
def clear_all():
    global selected_file
    selected_file = ""
    fileLb.config(text="No file selected")
    lengthTf.delete(0, END)
    summaryTxt.delete("1.0", END)


# title label
titleLb = Label(ws, text="LECTURE-TO-NOTES SUMMARIZER")
titleLb.grid(row=0, column=0, columnspan=2, pady=15)

# instructions label
instructionsLb = Label(ws, text="Upload a PDF, type short/medium/long, then click Generate Summary.")
instructionsLb.grid(row=1, column=0, columnspan=2, pady=10)

# upload button
uploadBtn = Button(ws, text="Upload PDF", command=upload_pdf)
uploadBtn.grid(row=2, column=0, pady=10)

# file label
fileLb = Label(ws, text="No file selected")
fileLb.grid(row=2, column=1, pady=10)

# summary length label
lengthLb = Label(ws, text="Enter Summary Length:")
lengthLb.grid(row=3, column=0, pady=10)

# summary length entry
lengthTf = Entry(ws)
lengthTf.grid(row=3, column=1, pady=10)

# generate button
generateBtn = Button(ws, text="Generate Summary", command=generate_summary)
generateBtn.grid(row=4, column=0, columnspan=2, pady=15)

# summary output text box
summaryTxt = Text(ws, width=80, height=18)
summaryTxt.grid(row=5, column=0, columnspan=2, pady=10, padx=20)

# clear button
clearBtn = Button(ws, text="Clear", command=clear_all)
clearBtn.grid(row=6, column=0, columnspan=2, pady=15)

# keep window open
ws.mainloop()

