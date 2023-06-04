# FriendFace post
user_id = 209
message = "D5 E5 C5 C4 G4"

language = 'English'
datetime = "20230215T124231Z"
location = (44.590533, -104.715556)

post = {"user_id":209, 'message':"D5 E5 C5 C4 G4", 'language':'English', 'datetime' :'20230215T124231Z', 'location': (44.590533, -104.715556)}


# to add datas inside the dic

post["p_id"]=22 # in key we should use qoutes

print(post)
print(post['user_id'])

# --------------------------

if 'location' in post:
    print(post['location'])
else:
    print("The post does not contain a location value.")

# ----------------------------

try:
    print(post['location'])
except KeyError:
    print("The post does not have a location.")
    
# ----------------------
# get method
loc = post.get('location', None) # if the dic key is not available then it return none

# Loop all the datas in the dic
for key in post.keys():
    value = post[key]
    print(key, "=", value)

for key, value in post.items():
    print(key, "=", value)

dir(post)
# pop , popitem this methods used to remove single data from lib
# clear will clean all datas in dic

help(post.pop)