
'''Basics of FastAPI learning'''

# from fastapi import FastAPI, Response, status, HTTPException
# from fastapi.params import Body
# from pydantic import BaseModel
# import psycopg2
# import time


#  app = FastAPI()




# class User(BaseModel):
#     name: str
#     email: str
#     age: int
#     gender: str
#     phone: str
#     address: str
#     city: str
#     state: str
#     country: str
#     zipcode: str
#     is_active: bool
#     role: str

# while True:

#     try:
#         conn = psycopg2.connect(
#             dbname="fastapi_db",
#             user="himu",
#             password="himu1234",
#             host="localhost",
#             port="5432"
#         )

#         cursor = conn.cursor()
#         print("successful connected to database")
#         break

#         # cursor.execute("select * from users")

#         # rows = cursor.fetchall()

#         # for row in rows:
#         #     print(row)

#         # cursor.close
#         # conn.close

#     except Exception as error:
#         print("database connection is failed")
#         print("error=======", error)
#         time.sleep(2)



# @app.post("/users")
# def add_user(user: User):
#     print("user=============",user.name)  # you will get the name from postman 
#     query = """
#         INSERT INTO users (
#             name, email, age, gender, phone, address,
#             city, state, country, zipcode, is_active, role
#         ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
#     """

#     values = (
#         user.name, user.email, user.age, user.gender, user.phone,
#         user.address, user.city, user.state, user.country,
#         user.zipcode, user.is_active, user.role
#     )

#     cursor.execute(query, values)
#     conn.commit()

#     return {"message": "User created successfully", "user": user}


# @app.get("/users")
# def get_users():
#     cursor.execute("""SELECT * FROM users WHERE id > %s""", (7))
#     users = cursor.fetchall()
#     return {"users":users}



# @app.get("/")
# def root():
#     return {"message": "welcome to fastapi tutorial"}


# class Post(BaseModel):
#     title:str
#     content:str
#     published: bool = True
#     # rating:Optional[int] = None



# # @app.post("/createposts")
# # def create_posts(payload: dict = Body(...)):     # THIS IS going to extract all the field from body and convert them in dict format .
# #     print(payload) 
# #     return {"message": "successfully created posts"}  # payload is just a variable name not a reserve keyword in this context
    
# @app.post("/posts", status_code=status.HTTP_201_CREATED)
# def create_posts(new_post: Post):      # the new_post is pydantic model
#     print(new_post.published) 
#     print(new_post.dict())
#     return {"data":"new_post"}  

# @app.get("/posts/{id}")
# def get_post_id(id:int, response: Response):
#     post = find_post(id)
#     if not post:
#         # response.status_code = 404
#         # response.status_code = status.HTTP_404_NOT_FOUND
#         # return {"message": "id is not found"}
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="id is not found")


#     return {"post_details": post}

