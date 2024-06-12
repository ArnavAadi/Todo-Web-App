import streamlit as st
import functions

def add_todo():
    new_todo = st.session_state["new_todo"] + "\n"

    todos.append(new_todo)
    with open("todos.txt", "w") as file_write:
        file_write.writelines(todos)


todos = functions.get_todos()

st.title("My Todo App")
st.subheader("This is my very own Todo App")
st.write("This is made to increase my <b>Productivity</b>", unsafe_allow_html=True)

st.text_input(label="-", placeholder="Add new Todo....",on_change=add_todo, key='new_todo')


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        with open("todos.txt", "w") as file_write:
            file_write.writelines(todos)
        del st.session_state[todo]
        st.experimental_rerun()


