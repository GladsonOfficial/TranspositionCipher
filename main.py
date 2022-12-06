import encode
import decode

print('Welcome, This is a project which shows transposition cipher in action')


def about_us():
    print('Developed by Team Virtuosos\n\tGladson Thomas\n\tPratiksha Dabhade')


while True:
    print('1. Encode')
    print('2. Decode')
    print('3. About Us')
    print('4. Exit')
    print('please choose an option')
    op = input()
    if op == '1':
        encode.encode()
    if op == '2':
        decode.decode()
    if op == '3':
        about_us()
    if op == '4':
        print('Thank you')
        break
