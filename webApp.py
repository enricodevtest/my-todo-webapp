# in a terminal, run streamlit (from the same directory as the webApp.py AND totolist.txt)
# with the following command:
# streamlit run C:\_SR\CODE\Python\MegaCourse\app01\venv\webApp.py

# !! The script is executed EVERY time the webpage is reloaded.

import streamlit as st
import myfunctions

filename = "todolist.txt"
todo_list = sorted(myfunctions.readTodos(filename))

def add_todo():
    a_todo = st.session_state["new_todo"]+"\n"
    todo_list.append(a_todo)
    myfunctions.writeTodos(filename, sorted(todo_list))
    st.session_state["new_todo"]=""

st.title("My To-Do App")
st.subheader("This is my To-Do App")
st.write("Use this app to track your list of To-Dos")

for index,todo in enumerate(todo_list):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todo_list.pop(index)
        myfunctions.writeTodos(filename,todo_list)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="Enter a to-do:",
              placeholder="Add a To-Do here",
              on_change=add_todo,
              key="new_todo")
# st.session_state