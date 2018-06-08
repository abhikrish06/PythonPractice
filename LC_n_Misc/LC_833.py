# incorrect
# incomplete

class Solution:
    def findReplaceString(self, S, indexes, sources, targets):
        """
        :type S: str
        :type indexes: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        other_S = S
        n = len(indexes)
        srtd_zpp = sorted(list(zip(indexes, sources, targets)),reverse=True)
        for i in range(n):
            st = srtd_zpp[i][0]
            en = len(srtd_zpp[i][1])
            sbstr = other_S[st:st + en]
            if sbstr == srtd_zpp[i][1]:
                S = S[:st]+ srtd_zpp[i][2]+ S[st+en:]
        return S


obj = Solution()
print(obj.findReplaceString("abcd", [0, 2], ["a", "cd"], ["eee", "ffff"]))
print(obj.findReplaceString("abcd", [0, 2], ["ab", "ec"], ["eee", "ffff"]))
print(obj.findReplaceString("ejvzndtzncrelhedwlwiqgdbdgctgubzczgtovufncicjlwsmfdcrqeaghuevyexqdhffikvecuazrelofjmyjjznnjdkimbklrh",
[25,35,60,77,69,79,15,19,58,92,27,64,4,11,51,7,72,67,30,0,74,98,17,85,48,32,38,62,43,2,9,55,87],
["gc","tov","vy","re","ikv","lo","dw","iqgdbd","ue","kimbk","tgu","qd","ndt","elhe","crq","zn","ec","ff","bz","ej","ua","rh","lw","jj","mfd","cz","ufn","ex","cjl","vz","cr","agh","znnj"],
["dxs","hn","vfc","wnr","tira","rko","oob","mlitiwj","zrj","onpp","ot","c","lm","hbsje","dgc","ruf","qi","h","vzn","ja","ow","te","km","imq","pia","ixp","xsod","m","eat","yf","lzu","dgy","dyrsc"]))

# print('abcd'.replace('a','eee'))

# op : "jayflmrufcwnrlheoobkmmlitiwjdxsotvznixpghnxsodcieatwspiadgcedgyzrjvfcmchhtiraqiowzrerkofjmyimqdyrscdonpplte"
# exp: "jayflmruflzuhbsjeoobkmmlitiwjdxsotvznixpghnxsodcieatwspiadgcedgyzrjvfcmchhtiraqiowzwnrrkofjmyimqdyrscdonpplte"
# exp: "jayflmruflzuhbsjeoobkmmlitiwjdxsotvznixpghnxsodcieatwspiadgcedgyzrjvfcmchhtiraqiowzwnrrkofjmyimqdyrscdonpplte
# a1 = [25,35,60,77,69,79,15,19,58,92,27,64,4,11,51,7,72,67,30,0,74,98,17,85,48,32,38,62,43,2,9,55,87]
# b1 = ["gc","tov","vy","re","ikv","lo","dw","iqgdbd","ue","kimbk","tgu","qd","ndt","elhe","crq","zn","ec","ff","bz","ej","ua","rh","lw","jj","mfd","cz","ufn","ex","cjl","vz","cr","agh","znnj"]
# c1 = ["dxs","hn","vfc","wnr","tira","rko","oob","mlitiwj","zrj","onpp","ot","c","lm","hbsje","dgc","ruf","qi","h","vzn","ja","ow","te","km","imq","pia","ixp","xsod","m","eat","yf","lzu","dgy","dyrsc"]
# print(list(zip(a1,b1,c1)))
# print(sorted(list(zip(a1,b1,c1)),reverse=True))
#
