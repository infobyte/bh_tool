import requests
import json

class GithubModule:
    def __init__(self):
        self.options = [{
                'name': 'token',
                'value': '',
                'required': True,
                'description': "github token to request"
            }, {
                'name': 'blur',
                'value': 'yes',
                'required': True,
                'description': "get fruit over the token"    
            }]
        self.session = requests.Session()

    def get_token(self):
        return self.options[0]['value']

    def do_show(self, args):
        print("Module options:\n")
        table = [['Name', 'Current Setting', 'Required', 'Description']]        
        blur = self.options[1]['value'] == 'yes'

        for opt in self.options:
            table.append([ opt['name'], opt['value'], 'yes' if opt['required'] else 'no', opt['description']])
        
        return table

    def find_mail(self, username):
        mails = []

        headers = {'Authorization': 'Bearer ' + self.options[0]['value']}
        user_url = "https://api.github.com/users/" + username
        response = self.session.get(user_url, headers=headers)
        if response.status_code == 200:
            data = json.loads(response.text)
            mails.append({'user': username, 'email': data["email"]})
        else:
            print(f"[{Fore.RED}-{Style.RESET_ALL}] Error getting the information")
            return []

        return mails
