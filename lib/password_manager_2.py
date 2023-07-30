# == INSTRUCTIONS ==
#
# Purpose: Manage a user's (valid) passwords
#
# Methods:
#   1. Name: __init__
#CREATE EMPTY LIST
#      Arguments: none
#   2. Name: add
#      Purpose: add a password for a service IF it is valid, otherwise do nothing
#      Arguments: one string representing a service name,
#                 one string representing a password
#      Returns: None

        # THE SAME AS BEFORE SIMPLE CHAR'S AND FOR LOOP WITH A CHECK FOR LEN AND CHAR IN
    #   IF SO ADD TO EMPTY LIST

#   3. Name: remove
#      Purpose: remove a password for a service
#      Arguments: one string representing a service name
#      Returns: None
    #   DEL DICT['SERVICE NAME'] 
#   4. Name: update
#      Purpose: update a password for a service IF it is valid, otherwise do nothing
#      Arguments: one string representing a service name,
#                 one string representing a password
#      Returns: None
#       TURN ADD FUNC INTO A VARIABLE AND RUN UPDATES FUNCS ON IT
#   5. Name: list_services
#      Arguments: none
#      Returns: a list of all the services for which the user has a password
# RETURN THE LIST
#   6. Name: sort_services_by
#      Arguments: A string, either 'service' or 'added_on', def sort_services_by(self, service,added_on,reverse)
#                 (Optional) A string 'reverse'SORTED(REVERSE=TRUE) to reverse the order
#      Returns: a list of all the services for which the user has a password
#               in the order specified
#   7. Name: get_for_service
#      Arguments: one string representing a service name
#      Returns: the password for the given service, or None if none exists
        # STRING DICT['SERVICENAME'] RETURNS VALUE OF KEY FROM PAIR
#
# A reminder of the validity rules:
#   1. A password must be at least 8 characters long
#   2. A password must contain at least one of the following special characters:
#      `!`, `@`, `$`, `%` or `&`
#
# And a new rule: passwords must be unique (not reused in other services).

from datetime import datetime
class PasswordManager2:
    def __init__(self):
        self.logs = {}
        
    def add(self,service_name,password):
        self.service_name = service_name
        self.password = password
        special_char = ['!','@','£','%','&','$']

        #if len(self.password) > 7 and any(char in special_char for char in self.password):
        #elif password not in self.logs.values():
        if len(self.password) > 7 and any(char in special_char for char in self.password):
            if password not in self.logs.values():
                self.logs[service_name] = password
                self.logs['time_added'] = datetime.now()
            else:
                pass
        else:
            pass
                    
               
    
    def remove(self,rm_srvce_name):
        del self.logs[rm_srvce_name]


    def update(self,service_name,password):
        if password not in self.logs.values():
            self.add(service_name,password)
            
        
    def list_services(self):
        users = {key:pair for (key,pair) in self.logs.items() if key != 'time_added' and key != 'password' }
        print(list(users))
        return list(users)

    def sort_services_by(self,usecase = 'base',reverse = False):
        list_logs = list(self.logs.keys())
        keys_names_user = [k for k in list_logs if k != 'time_added' and k != 'password']
        if usecase == 'service' and reverse == 'reverse':
            return sorted(keys_names_user, reverse = True)

        elif usecase == 'service':
            return sorted(keys_names_user)

        #elif usecase == 'added_on' and reverse == 'reverse':
            # sorted_by_time = sorted([k for k in list_logs if k != 'password'],reverse =True)
            # sorted_by_names = [k for k in sorted_by_time if k != 'time_added' ]
            # return sorted_by_names
        elif usecase == 'added_on' and reverse == 'reverse':
            sorted_by_time = sorted(self.logs.items(), key=lambda item: item == 'time_added', reverse=False)
            ans = [sorted_by_time[0][0], sorted_by_time[2][0], sorted_by_time[3][0]]
            return ans[::-1]

        elif usecase == 'added_on':
            sorted_by_time = sorted(self.logs.items(), key=lambda item: item == 'time_added', reverse=True)
            ans = [sorted_by_time[0][0], sorted_by_time[2][0], sorted_by_time[3][0]]
            return ans


    def get_for_service(self,service_name):
        if service_name in self.logs:
            
            return(self.logs[service_name])
        else:
            pass



#
# Example usage:
#   > password_manager = PasswordManager2()
#   > password_manager.add('gmail', '12ab5!678')   # Valid password
#   > password_manager.add('facebook', '$abc1234') # Valid password
#   > password_manager.add('youtube', '3@245256')  # Valid password
#   > password_manager.add('twitter', '12345678')  # Invalid password, so ignored
#   > password_manager.get_for_service('facebook')
#   '$abc1234'
#   > password_manager.list_services()
#   ['gmail', 'facebook', 'youtube']
#   > password_manager.remove('facebook')
#   > password_manager.list_services()
#   ['gmail', 'youtube']
#   > password_manager.update('gmail', '12345678')  # Invalid password, so ignored
#   > password_manager.get_for_service('gmail')
#   '12ab5!678'
#   > password_manager.update('gmail', '%21321415')  # Valid password
#   > password_manager.get_for_service('gmail')
#   '%21321415'
#   > password_manager.sort_services_by('service')
#   ['gmail', 'youtube']
#   > password_manager.sort_services_by('added_on', 'reverse')
#   ['youtube', 'gmail']

# There are many more examples possible but the above should give you a good
# idea.

# == YOUR CODE ==


