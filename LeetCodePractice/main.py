#coding = utf-8

import p_001_TwoSum
import p_017_Letter_Combinations_of_a_Phone_Number

header = "*"*20
test_1 = "p_001_TwoSum"
test_17 = "p_017_Letter_Combinations_of_a_Phone_Number"

print header,"\n",test_1,"\n",header
s_1 = p_001_TwoSum.Solution()
s_1.test(s_1)

print header*2,"\n",test_17,"\n",header*2
s_17 = p_017_Letter_Combinations_of_a_Phone_Number.Solution()
s_17.test()
