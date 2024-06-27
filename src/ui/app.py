import time
import streamlit as st
from st_pages import Page, show_pages, add_page_title

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def init():
    add_page_title()
    show_pages(
        [
            Page("chat.py", "Chat", "-", True),
            Page("rag_chat.py", "RAG Chat", "✏️"),
            Page("create_index.py", "Create Index", "✏️"),
            Page("delete_index.py", "Delete Index", "✏️"),
        ]
    )

# Streamlit application
def main():
    init()

if __name__ == "__main__":
    main()