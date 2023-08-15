import ast
class Voting:
    def __init__(self):
        self.candidates = {0:{"name":"John", "v_mark":0, "voter":[]},
                           1:{"name":"Rachel", "v_mark":0, "voter":[]},
                           2:{"name":"Ross", "v_mark":0, "voter":[]},
                           3:{"name":"Phoebe", "v_mark":0, "voter":[]},
                           4:{"name":"Joey", "v_mark":0, "voter":[]},
                           }
        
        self.db = {}

    def main_section(self):
        # option=0
        try:
            while True:
                option = int(input("Enter 1 to register\nEnter 2 to login\nEnter 3 to exit:"))
                if option == 1:
                    self.registration()
                    break

                elif option == 2:
                    self.login()
                    break

                elif option == 3:
                    exit(1)
                    
                else:
                    print("option must be 1 or 2 or 3! Try again")

        
        except Exception as err:
            print("Please enter integer 1 or 2 or 3 only!")
            self.main_section()
            

    def registration(self):
        print("This is registration form!")
        try:
            email = input("Enter your email:")
            password_check = False
            while password_check == False:
                password = input("Enter your password:")
                comfirm_password = input("Enter password to comfirm:")

                if password != comfirm_password:
                    print("Your password doesn't match!Try again")

                else:
                    password_check = True
                    name = input("Enter your name:")
                    address = input("Enter your address:")
                    age_check = False
                    while age_check == False:
                        age = int(input("Enter your age:"))
                        if age < 18:
                            print("Your age must be greater than 18!")
                        else:
                            age_check = True
                            money_check = False
                            while money_check == False:       
                                show_money = int(input("Enter your money at least $100 to vote the candidates:"))
                                if show_money < 100:
                                    print("You must put $100 at least!")
                                else:
                                    money_check = True
                                    print("Registration completed successfully!")

                                    self.id = len(self.db)
                                    self.data_form = {self.id:{"email":email,"password":password,"name":name,"address":address,"age":str(age),"money":show_money}}
                                    self.db.update(self.data_form)
                                    print(self.db)
                                    self.recording_all_data()
                                    self.main_section()
                                    

        except Exception as err:
            print("User info input fails!Try again")
            self.registration()
                
    def login(self):
        print("This is Login Form!")

        try:
            login_email = input("Enter your email to login:")
            login_password = input("Enter your password to login:")
            self.login_id = -1
            for i in range(len(self.db)):
                if login_email == self.db[i]["email"] and login_password == self.db[i]["password"]:
                    self.login_id = i
                    break

            if self.login_id != -1:
                self.user_section(self.login_id)

            else:
                print("Incorrect email or password! Try again.")
                self.login()
        except Exception as err:
            print(err, "\nInvalid Login input.")

    def user_section(self,login_id):
        print("This is user section.")

        print("Welcome,",self.db[login_id]["name"])

        print("Please select one you want to vote!")
        for i in range(len(self.candidates)):
            print("id:{} Name:{} Vote_Mark:{}".format(i, self.candidates[i]["name"], self.candidates[i]["v_mark"]))
            

        try:
            v_id = int(input("Enter ID number u want to vote(1 vote = $10):"))
            self.candidates[v_id]["v_mark"] +=1
            self.candidates[v_id]["voter"].append(self.db[login_id]["name"])


            cost_money = False
            if cost_money == False:
                self.db[login_id]["money"] -= 10
                # print(self.db[login_id]["money"])

                print("Voting done successfully!")
                print("{}'s voting mark is : {}".format(self.candidates[v_id]["name"],self.candidates[v_id]["v_mark"]))

            for i in range(len(self.candidates[v_id]["voter"])):
                print("Voter:",self.candidates[v_id]["voter"][i])

            self.recording_all_data()

            # print(self.db)
            # print(self.candidates)
        except Exception as err:
            print(err,"Voting input error!")

        while True:
            try:
                afterVote_option = int(input("Press 1 to vote again\nPress 2 to get main_section\nPress 3 to exit:"))
                if afterVote_option == 1:
                    self.user_section(login_id)
                    break
                elif afterVote_option == 2:
                    self.main_section()
                    break
                elif afterVote_option == 3:
                    exit(1)
                else:
                    print("Invalid option after voting!")
            except Exception as err:
                print(err,"afterVote_error occurs!")


    def recording_all_data(self):
        with open("record_user_data.txt",'w') as file:
            file.write(str(self.db))
           
        with open("record_candidate_data.txt",'w') as f:
            f.write(str(self.candidates))

    def loading_all_data(self):
        # global db
        # global candidates
        with open("record_user_data.txt") as file:
            data = file.read()
            self.db = ast.literal_eval(data)

        with open("record_candidate_data.txt") as f:
            c_data = f.read()
            self.candidates = ast.literal_eval(c_data)


    
        



if __name__ == '__main__':
    
    voting = Voting()
    voting.loading_all_data()
    voting.main_section()



