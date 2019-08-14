import Credentials
client = Credentials.client
db = client.VisitorBook

def newUser(CompObjID):
    Name = input('Enter User Name')
    Password = input('Enter User Password')
    result=db.Company_Admin.insert_one({'UserName':Name,
                                      'Password':Password,
                                      'Company':CompObjID
                                      })
    
    print(result.inserted_id)

def main():
    company = input('Enter Company Name')
    result=db.Company_name.find_one({'Name':company})
    if result == None:
        print("Company is not Exists ")
    else:
        CompObjID = result.get('_id')
        newUser(CompObjID)

if __name__ == "__main__":
    main()


