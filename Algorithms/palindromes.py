str = 'racecar'

def checkispalindrome(str):
    
    startIndex = 0
    endIndex = len(str) - 1

    for x in str:
        if str[startIndex] != str[endIndex]:
            print('str is not a palindrome')
            return False
    print('str is a palindrome')
    return True

    # endIndex = len(str)
    # print(str)
    # for x in str:
    #     print(str)

    
checkispalindrome(str)


# if __name__ == "__checkispalindrome__":
#     checkispalindrome(str)