s=input()
print(any(c.isalnum() for c in s))
print(any(c.isalpha() for c in s))
print(any(c.isdigit() for c in s))
print(any(c.islower() for c in s))
print(any(c.isupper() for c in s))
# def check_string(s):
#     # Initialize flags
#     has_alnum = False
#     has_alpha = False
#     has_digit = False
#     has_lower = False
#     has_upper = False

#     # Iterate over each character
#     for char in s:
#         # Check for alphanumeric character
#         if ('a' <= char <= 'z') or ('A' <= char <= 'Z') or ('0' <= char <= '9'):
#             has_alnum = True
        
#         # Check for alphabetical character
#         if ('a' <= char <= 'z') or ('A' <= char <= 'Z'):
#             has_alpha = True
        
#         # Check for digits
#         if '0' <= char <= '9':
#             has_digit = True
        
#         # Check for lowercase characters
#         if 'a' <= char <= 'z':
#             has_lower = True
        
#         # Check for uppercase characters
#         if 'A' <= char <= 'Z':
#             has_upper = True

#     # Output the results
#     print(has_alnum)
#     print(has_alpha)
#     print(has_digit)
#     print(has_lower)
#     print(has_upper)

# # Input the string
# s = input()

# # Call the function
# check_string(s)

    