Math = int(input('Enter your Maths Marks '))
Programming = int(input('Enter your Programming Marks'))
Networking = int(input('Enter your Networking Marks '))
English = int(input('Enter your English Marks'))
PakStudies = int(input('Enter your Pak_Studies Marks '))

Total = Math+Programming+Networking+English+PakStudies
print('')
print('------Total Marks Obtain '+str(Total)+'------')
Percentage = round((Total/500) * 100)
print('------Percentage  '+str(Percentage)+' % ------')
print('')
if Percentage > 80:
    print('------ You have A+ grade ------')
elif Percentage>70:
    print('------ You have A grade ------')
elif Percentage > 60:
    print('------ You have B grade ------')
elif Percentage > 50:
    print('------ You have C grade ------')
elif Percentage > 45:
    print('------ You have D grade ------')
else:
    print('------ You are Fail ------')

