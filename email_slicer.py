# collect email from user
# slice and split the email using the @
# the first part as the user name
# the second part is gonna be saved as domain
# split domain using . , 

def main():
    print("Welcome to e-mail slicer ")
    print("")

    email_input = input("Input your email addres: ")
    (username, domain) = email_input.split("@")
    (domain, extension) = domain.split(".")

    print("Username : ",  username)
    print("Domain :", domain)
    print("Extension: ", extension)

while True:
    main()
    quit()