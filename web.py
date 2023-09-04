import streamlit as st
import functions
import os

if not os.path.exists('todos.txt'):
    with open('todos.txt','w') as file:
        pass

todos = functions.get_todos()


def add_todo():
    local_todo = st.session_state['new_todo']
    todos.append(local_todo + '\n')
    functions.write_todos(todos)


st.title('My Todo App')
st.subheader('This is my first web app')
st.write('This app is designed to increase your productivity')


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()


st.text_input(label='Add a new todo',placeholder='Enter text here...',max_chars=50,key='new_todo',on_change=add_todo)


