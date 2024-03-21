nric = input('Enter an NRIC number: ')

# Type your code below
validity = 1
prefix = nric[0].upper()
digits = nric[1:8]
suffix = nric[8:].upper()
prefix_list = ['S','T', 'F', 'G']
suffix_list_1 = ['J','Z','I','H','G','F','E','D','C','B','A']
suffix_list_2 = ['X','W','U','T','R','Q','P','N','M','L','K']
weight = [2,7,6,5,4,3,2]
sum = 0

if nric[0] not in prefix_list :
  validity *= 0 

elif len(digits) != 7:
  validity *= 0

elif not (digits.isdigit()):
  validity *= 0

elif len(suffix) != 1:
  validity *= 0

elif not nric[-1].isalpha():
  validity *= 0

elif (suffix not in suffix_list_1) and (suffix not in suffix_list_2):
  validity *= 0

else:

  if digits.isdigit():
    for x in range (7):
      sum = sum + int(digits[x]) * weight[x]
     # print(sum)
    if prefix in ['T','G']:
      sum = sum + 4

  sum = sum%11
 # print(sum)

  if prefix in ['S','T']:
      if suffix_list_1[sum] != suffix:
        validity *= 0

  if prefix in ['F','G']:
      if suffix_list_2[sum] != suffix:
         validity *= 0
  



if validity == 0:
  print("NRIC is invalid.")
else:
  print("NRIC is valid.")
