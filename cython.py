import os,platform,time

bitt=platform.architecture()[0]

if bitt=="64bit":
    os.system('clear');print(' [~] Your Device is 64 bit');time.sleep(1);print('\n\n[!] Your Python Version :');time.sleep(1);os.system('python --version')
    time.sleep(2)
    import CY64.cyt
if bitt=="32bit":
    os.system('clear');print(' [~] Your Device is 32 bit');time.sleep(1);print('\n\n[!] Your Python Version :');time.sleep(1);os.system('python --version')
    time.sleep(2)
    import CY32
else:
    print('\nYOUR DEVICE 32 BIT NOT SUPPORT')

#---------------------------------------------------------#
#                    THIS TOOL OWNED BY
#                •MARUFUL HAQUE MUHIB •
#--------------------------------------------------------#
