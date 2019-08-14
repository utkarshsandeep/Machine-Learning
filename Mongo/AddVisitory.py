import Credentials
import datetime
client = Credentials.client
db = client.VisitorBook


def CheckUser():
    Name = input('Enter User Name')
    Password = input('Enter User Password')
    result=db.Company_Admin.find_one({'UserName':Name,'Password':Password})
    if result == None:
        User = None
        Company = None     
    else:
        User = result.get('_id')
        Company = result.get('Company')
    return User , Company
        
    
def addVisitor(User,Company):
    Name = input('Enter Name')
    Phone = input('Enter Phone Number')
    UID = input('Enter UID')
    Password = input('Enter User Password')
    result=db.Company_Visitors.insert_one({'Name':Name,
                                      'Phone':Phone,
                                      'UIP':UID,
                                        'User':User,
                                        'Company':Company,
                                      'date': datetime.datetime.utcnow()})
    



def main():
    User , Company =  CheckUser()   
    if User == None:
        Print("Wrong Credentials")
    else:
        addVisitor(User,Company)

if __name__== "__main__":
    main()
    
