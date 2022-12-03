import streamlit as st
import os

st.title("German Law Exam Sample app v1.0")

# https://docs.streamlit.io/knowledge-base/using-streamlit/how-download-file-streamlit
# https://discuss.streamlit.io/t/downloading-a-ms-word-document/28850

exam = st.sidebar.radio('SELECT EXAM',("Civil law","Public law","Criminal law"))

def download_template(exam_name,file_name):
    # download_file = os.path.join("template\\",exam_name + "\\" + file_name)
    download_file = os.path.join("template/", exam_name + "/" + file_name)
    with open(download_file, 'rb') as f:
        st.download_button('Download File ' + file_name, f, file_name=file_name,mime="docx")  # Defaults to 'application/octet-stream'    #
    st.text(download_file)

if exam == "Civil law":
    civil_task = st.sidebar.radio('CIVIL LAW TASKS', ("Civil law task 1", "Civil law task 2", "Civil law task 3"))
    if civil_task == "Civil law task 1":
        download_template("civil", "Civil law task 1.docx")
    elif civil_task == "Civil law task 2":
        download_template("civil", "Civil law task 2.docx")
    elif civil_task == "Civil law task 3":
        download_template("civil", "Civil law task 3.docx")
elif exam == "Public law":
    public_task = st.sidebar.radio('PUBLIC LAW TASKS', ("Public law task 1", "Public law task 2", "Public law task 3"))
    if public_task == "Public law task 1":
        download_template("public", "Public law task 1.docx")
    elif public_task == "Public law task 2":
        download_template("public", "Public law task 2.docx")
    elif public_task == "Public law task 3":
        download_template("public", "Public law task 3.docx")
elif exam == "Criminal law":
    criminal_task = st.sidebar.radio('CRIMINAL LAW TASKS', ("Criminal law task 1", "Criminal law task 2", "Criminal law task 3"))
    if criminal_task == "Criminal law task 1":
        download_template("criminal", "Criminal law task 1.docx")
    elif criminal_task == "Criminal law task 2":
        download_template("criminal", "Criminal law task 2.docx")
    elif criminal_task == "Criminal law task 3":
        download_template("criminal", "Criminal law task 3.docx")



