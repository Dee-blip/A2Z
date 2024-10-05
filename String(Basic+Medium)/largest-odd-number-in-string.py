class Solution:
    def largestOddNumber(self, num: str) -> str:
        #ValueError: Exceeds the limit (4300 digits) for integer string conversion: value has 4302 digits; use sys.set_int_max_str_digits() to increase the limit
        # if num=="":
        #     return num
        # convert_into_integer=int(num)

        # while convert_into_integer>0:
        #     if convert_into_integer%2!=0:
        #         return str(convert_into_integer)
        #     convert_into_integer = convert_into_integer//10
        # return ""

        #Alternative approach
        for i in range(len(num)-1,-1,-1):
            if int(num[i])%2!=0:
                return num[:i+1]
        return ""




        
