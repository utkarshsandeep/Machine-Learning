import Credentials
client = Credentials.client
db = client.VisitorBook

def main():
    company = input('Enter Company Name')
    result=db.Company_name.insert_one({'Name':company})
    print(result.inserted_id)
if __name__== "__main__":
    main()
