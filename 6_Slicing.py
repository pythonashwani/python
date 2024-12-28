planet1="Closest of Sun"
# C l o s e s t   o f    S  u  n
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13
print(planet1)
"""
print(planet1[0]) # C
print(planet1[1]) # l
print(planet1[2]) # o

print(planet1[-1]) # n
print(planet1[-2]) # u
print(planet1[-3]) # S

# Slicing a string, get a substring from a string
print(planet1[1:4]) # los
print(planet1[:])  # Closest of Sun
print(planet1[:7]) # Closest
print(planet1[11:]) # Sun

# Slicing Tuple
devops=("Linux", "Vagrant", "Bash Scripting", "AWS", "Jenkins", "Python", "Ansible")
print(devops[0])
print(devops[4])
print(devops[-1])

print(devops[2:5]) #   ('Bash Scripting', 'AWS', 'Jenkins')
print(devops[2:5][0]) # Bash Scripting

print(devops[2:5][0][5:11]) # Script
print(devops[2:5][0][5:11][-1])

# Slicing List
devops=["Linux", "Vagrant", "Bash Scripting", "AWS", "Jenkins", "Python", "Ansible"]
print(devops[0])
print(devops[4])
print(devops[-1])

print(devops[2:5])
print(devops[2:5][0])



print(devops[2:5][0][5:11])
print(devops[2:5][0][5:11][-1])

"""
# Dictionary Example
Skills = {
            "DevOps": ("AWS", "Jenkins", "Python", "Ansible"), 
            "Development": ["Java", "NodeJS", ".net"]
        }
print(Skills) # {'DevOps': ('AWS', 'Jenkins', 'Python', 'Ansible'), 'Development': ['Java', 'NodeJS', '.net']}
print(Skills["DevOps"]) # ('AWS', 'Jenkins', 'Python', 'Ansible')
print(Skills["Development"]) # ['Java', 'NodeJS', '.net']

print(Skills["DevOps"][-1]) # Ansible
print(Skills["DevOps"][-1][:3]) # Ans

