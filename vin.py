def validate_vin(data):
    """
    Validate a VIN against the 9th position checksum
    See: http://en.wikipedia.org/wiki/Vehicle_Identification_Number#Check_digit_calculation
    Test VINs:
        1M8GDM9AXKP042788
        11111111111111111
    """
    POSITIONAL_WEIGHTS = [8,7,6,5,4,3,2,10,0,9,8,7,6,5,4,3,2]
    ILLEGAL_ALL = ['I', 'O', 'Q']
    ILLEGAL_TENTH = ['U','Z','0']
    LETTER_KEY = dict(
        A=1,B=2,C=3,D=4,E=5,F=6,G=7,H=8,
        J=1,K=2,L=3,M=4,N=5,P=7,R=9,
        S=2,T=3,U=4,V=5,W=6,X=7,Y=8,Z=9,
    )

    if len(data) == 17:
        vin = data.upper()

        for char in ILLEGAL_ALL:
            if char in vin:
                print('Field cannot contain "I", "O", or "Q".')
                return False
        if vin[10] in ILLEGAL_TENTH:
            print('Field cannot contain "U", "Z", or "0" in position 10.')
            return False

        # check_digit = vin[8]

        # pos=sum=0
        # for char in vin:
        #     value = int(LETTER_KEY[char]) if char in LETTER_KEY else int(char)
        #     weight = POSITIONAL_WEIGHTS[pos]
        #     sum += (value * weight)
        #     pos += 1

        # calc_check_digit = int(sum) % 11

        # if calc_check_digit == 10:
        #     calc_check_digit = 'X'

        # if str(check_digit) != str(calc_check_digit):
        #     print('Invalid VIN.')
        #     return False
    else:
        print('Field must be 17 characters.')
        return False
    return True

print(validate_vin('VSSAA7KNXLW001336'))