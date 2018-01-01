# without additional data structure
def unique_string(ip_string):
    #chars = []
    for i in range(len(ip_string)):
        #print(i, ip_string[i])
        for j in range(i+1,len(ip_string)):
            #print(j, ip_string[j])
            if ip_string[i] == ip_string[j]:
                return False
    return True

print(unique_string("abia"))