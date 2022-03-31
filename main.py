#=====================================================================================================
#    Author: Maximilian Edison                                                                       
#    Date:                                                                                            
#    License: https://github.com/MaxianEdison/PasswordGenerator/blob/main/LICENSE                      
#    Source: https://github.com/MaxianEdison/PasswordGenerator                                       
#=====================================================================================================


import random
import string 

print("hi, welcome to password generator!")
pass_len = int(input("\nEnter the length of your password: "))

all = string.ascii_letters + string.digits + string.punctuation
password = "".join(random.sample(all,pass_len))

print(password)
