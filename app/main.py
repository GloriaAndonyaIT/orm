from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from  models import User, Category, Task, Base
import os
# SQLITE DB connection
engine =  create_engine("sqlite:///database.db",echo=False )
Session = sessionmaker(bind=engine)

session = Session()


# USER
def create_user():
    username = input("Enter your username : ")
    email =    input("Enter your email    : ")
    
    user = User(username=username, email=email)
    session.add(user)
    session.commit()

    print(username, " created successfully!")

def fetch_users():
    users = session.query(User).all()
    for user in users:
        print(f"ID : {user.id}  USERNAME : {user.username} EMAIL : {user.email}")

#FETCH
def fetch_user_by_id():
    user_id = input("Enter user ID : ")
    user = session.query(User).get(user_id)
    if user:
        print(f"ID : {user.id}  USERNAME : {user.username} EMAIL : {user.email}")
    else:
        print("User not found!")
# Update
def update_user():
    user_id = input("Enter user ID : ")
    user = session.query(User).filter_by(id=user_id).first()
    if user:
        username = input("Enter new username : ")
        email = input("Enter new email : ")
        user.username = username
        user.email = email
        session.commit()
        print("User updated successfully!")
    else:
        print("User not found!")
# Delete
def delete_user():
    user_id = input("Enter user ID : ")
    user = session.query(User).filter_by(id=user_id).first()
    if user:
        session.delete(user)
        session.commit()
        print("User deleted successfully!")
    else:
        print("User not found!")

# Assignment
# Delete, Update, fetch single user


# CATEGORY
# Assignment
# ALL CRUD operations for category

# TASK
# CRUD 

# 




#Category
def create_category():
    name = input("Enter category name : ")
    

    category = Category(name=name)
    session.add(category)
    session.commit()

    print(name, " created successfully!")
def fetch_categories():
    categories = session.query(Category).all()
    for category in categories:
        print(f"ID : {category.id}  NAME : {category.name} ")
 #FETCH
def fetch_category_by_id():
    category_id = input("Enter category ID : ")
    category = session.query(Category).get(category_id)
    if category:
        print(f"ID : {category.id}  NAME : {category.name} ")
    else:
        print("Category not found!")

#UPDATE
def update_category():
    category_id = input("Enter category ID : ")
    category = session.query(Category).filter_by(id=category_id).first()
    if category:
        name = input("Enter new category name : ")
        
        category.name = name
      
        session.commit()
        print("Category updated successfully!")
    else:
        print("Category not found!")

#DELETE
def delete_category():
    category_id = input("Enter category ID : ")
    category = session.query(Category).filter_by(id=category_id).first()
    if category:
        session.delete(category)
        session.commit()
        print("Category deleted successfully!")
    else:
        print("Category not found!")


#TASK
def create_task():
    title = input("Enter task title : ")
    description = input("Enter task description : ")
    user_id = input("Enter user ID : ")
    category_id = input("Enter category ID : ")
    deadline = input("Enter due date(YYYY-MM-DD) or none : ")
    due_date = datetime.strptime(deadline, "%Y-%m-%d") if deadline else None

    

    category = session.query(Category).filter_by(id=category_id).first()
    user = session.query(User).filter_by(id=user_id).first()
    if category and user:   
        task = Task(title=title, description=description, user_id=user_id, category_id=category_id, due_date=due_date)
        session.add(task)
        session.commit()

        print(title, " created successfully!")
    else:
        print("Category or User not found!")

def fetch_tasks():
    tasks = session.query(Task).all()
    for task in tasks:
        print(f"ID : {task.id}  TITLE : {task.title} DESCRIPTION : {task.description} USER_ID : {task.user_id} CATEGORY_ID : {task.category_id}")

 #FETCH
def fetch_task_by_id():
    task_id = input("Enter task ID : ")
    task = session.query(Task).get(task_id)
    if task:
        print(f"ID : {task.id}  TITLE : {task.title} DESCRIPTION : {task.description} USER_ID : {task.user_id} CATEGORY_ID : {task.category_id}")
    else:
        print("Task not found!") 

#UPDATE
def update_task():
    task_id = input("Enter task ID : ")
    task = session.query(Task).filter_by(id=task_id).first()
    if task:
        title = input("Enter new task title : ")
        description = input("Enter new task description : ")
        # user_id = input("Enter new user ID : ")
        category_id = input("Enter new category ID : ")
        deadline = input("Enter due date(YYYY-MM-DD) or none : ")
        due_date = datetime.strptime(deadline, "%Y-%m-%d") if deadline else None
        task.title = title
        task.description = description
        task.due_date = due_date
        # task.user_id = user_id
        task.category_id = category_id
        session.commit()
        print("Task updated successfully!")
    else:
        print("Task not found!")
#DELETE
def delete_task():
    task_id = input("Enter task ID : ")
    task = session.query(Task).filter_by(id=task_id).first()
    if task:
        session.delete(task)
        session.commit()
        print("Task deleted successfully!")
    else:
        print("Task not found!")


def main():
    while True:
        print("============TASK MANAGER=============")
        print("1. Create User ")
        print("2. List Users ")
        print("3. Fetch User by ID ")
        print("4. Update User ")
        print("5. Delete User ")
        print("\n=== Category Management ===")
        print("6. Create Category ")
        print("7. List Categories ")
        print("8. Fetch Category by ID ")
        print("9. Update Category ")
        print("10. Delete Category ")
        print("\n=== Task Management ===")
        print("11. Create Task ")
        print("12. List Tasks ")
        print("13. Fetch Task by ID ")
        print("14. Update Task ")
        print("15. Delete Task ")
        print("0. Exit ")
        choice = input("Enter your choice : ")

        if choice=="1":
            create_user()
        elif choice=="2":
            fetch_users()
        elif choice=="3":
            fetch_user_by_id()
        elif choice=="4":
            update_user()
        elif choice=="5":
            delete_user()
        # Category options
        elif choice=="6":
            create_category()
        elif choice=="7":
            fetch_categories()
        elif choice=="8":
            fetch_category_by_id()
        elif choice=="9":
            update_category()
        elif choice=="10":
            delete_category()
        # Task options
        elif choice=="11":
            create_task()
        elif choice=="12":
            fetch_tasks()
        elif choice=="13":
            fetch_task_by_id()
        elif choice=="14":
            update_task()
        elif choice=="15":
            delete_task()
        elif choice=="0":
            print("Bye! Bye!")
            break
        else:
            print("Invalid input! Try again!")
main()