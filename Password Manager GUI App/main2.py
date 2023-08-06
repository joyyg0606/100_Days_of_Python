# try:
#     file = open("file.txt")
#     a_dict = {'key': "value"}
#     print(a_dict['key'])

# except FileNotFoundError:
#     file = open("file.txt", "w")
#     file.write("smth")

# except KeyError as error_message:
#     print(f"the key {error_message} does not exist")

# else:
#     content = file.read()
#     print(content)

# finally:
#     raise TypeError("this is an error")

# height = float(input("height: "))
# weight = int(input("Weight: "))

# if height > 3:
#     raise ValueError("liar ur too tall.")

# bmi = weight / height ** 2
# print(bmi)

# facebook_posts = [
#     {'Likes': 21, 'Comments': 2}, 
#     {'Likes': 13, 'Comments': 2, 'Shares': 1}, 
#     {'Likes': 33, 'Comments': 8, 'Shares': 3}, 
#     {'Comments': 4, 'Shares': 2}, 
#     {'Comments': 1, 'Shares': 1}, 
#     {'Likes': 19, 'Comments': 3}
# ]

# total_likes = 0

# for post in facebook_posts:
#     try:
#         total_likes = total_likes + post['Likes']
#     except KeyError:
#         pass

# print(total_likes)