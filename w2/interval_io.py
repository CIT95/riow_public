# Rio's Code for Week 2 LT

# set run to Y
run = 'Y'
# while run equals to Y run the code
while run == 'Y':
    #ask user for starting number - convert input to integer
    print('Hello, please provide me a starting number  - integers only')
    start = int(input())

    #ask user for ending number - convert input to integer
    print('and provide me a ending number and I will output the prime numbers between')
    end = int(input())

    #if start is less than end give the user feedback, otherwise run code inside if statement
    if(start < end):


        #I did some minor modification
        #I will cover this part in the video
        for val in range(start, end + 1):
            print(val)
    else:
        print('Starting number needs to be greater than ending number')

    #ask user if they run to run the code again
    print('Run again? Y for yes')
    run = input()
    #because run needs to be string, we don't need to convert

    if(run != 'Y'):

        #if user enter anything but capital Y end the program
        print('Thanks for using my program!')
    continue
