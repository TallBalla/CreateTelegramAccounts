import json


class FileHandler():
    def __init__(self, file_name):
        self.file_data = None
        self.location = f'../{file_name}.json'

    def create_json_file(self):
        with open(self.location, 'w') as outfile:
            json.dump([], outfile)

    def append_single_account_json_file(self, account):
        self.load_accounts()

        json_account = json.dumps(account.__dict__)
        self.file_data.append(json_account)

        self.update_accounts()

    # TODO ablitiy to add multiple accounts
    def append_multiple_account_json_file(self, *accounts):
        self.load_accounts()

        for account in accounts:
            json_account = json.dumps(account.__dict__)
            self.file_data.append(json_account)

        self.update_accounts()

    def load_accounts(self):
        with open(self.location, 'r') as infile:
            self.file_data = json.load(infile)

    def update_accounts(self):
        with open(self.location, 'w') as outfile:
            json.dump(self.file_data, outfile)

    def get_accounts(self):
        return self.file_data

    def get_account_by_index(self, index):
        return self.file_data[index]

if __name__ == '__main__':
    file_handler = FileHandler()
