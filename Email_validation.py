import re
def email_validation():
    email = 'ebimp4@gmail.com'
    result = re.findall(  '.+\@.+\..+' ,email )   
    if result:
        print('The email is vallid')
    else:
        print('The email is not valid!!')
    
    
email_validation()    
    