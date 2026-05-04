# MIS310-Final-Project
# Lecture-to-Notes Summarizer

This project is a Python application built for MIS 310 as a group project. It helps students turn lecture PDFs into short, organized summaries to make studying easier and more efficient.

## Overview

Students often deal with long lecture notes and transcripts that take a lot of time to review. This program helps solve that problem by allowing users to upload a PDF file and automatically generating a summary of the key points.

The goal is to save time and help students focus on the most important parts of their course material.

## Features

- Upload PDF lecture files
- Extract text from PDFs
- Generate summaries in different lengths (short, medium, long)
- Display results in a simple GUI
- Clear and reset output when needed

## How It Works

1. The user uploads a PDF file using the interface  
2. The program reads the file using PyPDF2  
3. The text is processed and sent to the OpenAI API  
4. The API returns a summarized version of the content  
5. The summary is displayed in the application window  

## Libraries Used

- `tkinter` – creates the graphical user interface  
- `filedialog` – handles file selection  
- `PyPDF2` – extracts text from PDF files  
- `openai` – generates summaries using AI  
- `os` – manages environment variables and API key  

## Installation

Install the required libraries:

```bash
pip install PyPDF2
pip install openai
