# TLE
# class Solution:
#     def totalHammingDistance(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         sumval = 0
#         for i in range(len(nums)-1):
#             for j in range(i+1, len(nums)):
#                 sumval = sumval + bin(nums[i] ^ nums[j]).count('1')
#         return sumval

class Solution:
    def totalHammingDistance(self,nums):
        bits = [[0,0] for _ in range(32)]

        for val in nums:
            for i in range(32):
                bits[i][val%2] += 1
                val //= 2
        return sum(x*y for x,y in bits)

obj = Solution()
print(obj.totalHammingDistance([4953595,3761801,6771310,1966212,6939601,9011181,8088354,780695,6789604,3464583,5052723,459093,5081820,8974218,7889769,8524937,1442699,7412843,3159286,1581496,8094662,5897785,9032399,3797814,6070666,8944163,3761473,7592325,2580458,8344420,780953,2164366,2516142,7984723,8963834,951903,4645036,3251938,6186146,9126564,1373279,8231215,5704830,4255518,721207,9144792,3744360,8326780,4472782,4884252,6880401,7410402,102733,6282686,7689677,9811830,9875503,1935169,2941500,2539220,9016535,3140453,5529221,9714102,5590542,259484,3571049,7080228,4006967,7545956,6709209,2207641,9137377,1411322,9021048,7401267,1503367,1990250,5618645,4875224,8353117,6463497,7888394,3858602,8038981,6386950,8904789,1654058,5093128,2752240,6962291,8635744,8583168,6283539,6315114,1545406,9104323,1934523,5550691,7309882,1734116,2976978,9382566,3611085,3125146,7439671,9124903,8524273,9030540,1696333,8996653,5656504,5065460,7125118,6577373,6577079,813268,6625526,817129,1821752,7308829,5335102,4291119,319525,7794003,193888,2871790,5551430,4967233,5524487,3616277,7745378,6464224,5571795,3010899,4604432,1340912,6620557,5699990,7842217,6846318,7219133,6517921,4590761,1786170,1435932,5406141,7813834,9950327,3361445,3048204,1071413,8653893,4391766,8350476,6839232,4569822,6781196,2578837,6767009,5299595,7738725,8631920,3197979,9174122,8129517,7674657,9752201,332612,693323,9322758,4356697,6350527,7554250,7112556,7083462,6801847,4300105,1607428,7353853,3226868,8131612,3631210,4572333,7640618,4712617,4717826,8494577,6848915,3936134,3163950,3861119,6371512,8952636,6030094,8913916,7082213,1781039,4160659,4000285,3348006,6951197,2223084,2900279,2242495,9568466,2760692,3046168,9187426,1379000,8977527,8664445,3082185,6005190,5712477,8366470,3924123,3890339,4649052,1650316,5621401,5700385,6128336,2797318,7671438,6949225,3096814,2302303,6803919,7611697,1416172,4168820,9514858,9040928,8745625,1382447,9936280,5015116,9957202,161881,8396654,4082078,8728420,2080922,4089968,6145118,7570769,8211654,5737238,2401039,7784114,3087999,3674642,7524266,9570113,8060310,4819255,3255978,666359,1940388,624766,4536439,1177827,111833,2860208,8769198,2685477,1549375,191016,8633199,7017466,936498,6297801,7800992,6282589,6240686,2801766,6322997,5805452,3773849,7840178,6698602,7750902,1383204,5482179,4836588,9516019,4232322,1418904,6223988,5961859,2685338,635070,3807765,2201902,5505004,533475,928780,1253753,6334957,938929,438595,6543069,1360975,8673064,9681964,7173443,8301692,5934434,4000032,9950855,1062143,9737335,6755284,9548008,3779000,992968,6901603,9937306,916143,5657382,6889874,6623113,3512348,2478989,2515696,3739311,171281,8152919,6974937,8535354,4139707,991022,4239379,7521281,2774839,2111306,1301322,3536273,2769553,4691372,1240487,8566075,5139932,8302066,2524651,4292442,4585852,5860540,1498974,1059012,3694551,6637650,6492752,2827689,6344122,7052196,8063675,9771654,8440850,1387071,1771357,9281508,9376395,5132066,5580050,8195527,9971925,3459366,1829227,9123796,697279,3780584,9478613,2512925,6511870,8511894,2138354,4293902,8482807,7822412,7801041,512220,9283818,152318,4037491,5981090,663777,8026560,4376693,8482830,1979885,1200335,8266699,2005505,2969073,8126387,8533012,7465871,4354436,8868054,738202,1526999,5325697,1458262,8369138,8247045,1499439,3851044,6034898,6831744,4090826,5509834,8472506,4175351,1007642,3174428,9583801,4650261,5998844,4169122,4330371,4577156,9356023,4998262,1545690,3450001,1316004,3626070,6444107,353310,4703053,2235432,6188247,3264673,2514158,1907279,7263492,5693456,8803634,4260350,3491589,115963,8990141,9232096,8297865,6163312,6654283,2453959,3790487,6222733,4959718,1434084,406336,3418144,3437229,3938623,7468728,8998414,5207185,3476903,2510006,6167459,8690225,1129667,382314,5040479,9788052,9337191,6627729,8925704,5507528,4127741,7757150,6302696,6379258,3596033,6038404,4899818,756563,1158882,5246396,9854468,5193612,8301603,4134212,4775001,4118911,4848519,1506402,8677962,964094,6593062,2857368,8105186,8711073,7077359,5190617,8438594,2826966,7003930,1789592,4841708,5354104,2665623,2781797,6412700,2893152,9343338,6002137,4523817,7820029,2206335,6941213,2514441,8538748,5822576,8338138,740756,3369323,9120039,7325646,3610442,1370333,9984083,2255247,4637218,4236323,6372844,5187137,3493412,7809013,2908447,9568517,4261362,7630827,8507926,3631267,1850064,2841966,1060683,1397984,1461682,8016834,8620944,7685791,2346051,1772156,2652124,5994748,6884360,3872650,6966717,3327925,9800675,4087218,8199601,5497532,4003659,312777,2654100,8473471,1769528,390883,402617,9739513,1102530,7269333,8275320,5769452,7852850,8805659,8036572,785020,3297237,3936815,2228006,4966841,3531856,7921988,3844780,802296,2693078,2277960,8358829,4600370,3893431,9269739,3956323,7106405,2404848,8291266,5727875,9281966,1790577,4986227,3718089,1980615,6889512,143936,5054793,3692873,8818816,7516669,374822,3885457,3603367,1805564,597202,4630181,7171329,9351627,336335,3660827,9320228,9058433,5898271,8162492,9030015,5026435,6775568,8462997,4954655,4860198,1519821,6852807,8830824,5610659,1862635,3467519,2671808,4883714,9441391,3321416,6068400,5882724,4605663,7343972,5463101,9780465,6708615,3060815,2641178,559260,5168522,9332350,975976,4813791,3499642,6410646,1484994,2203129,5258194,174120,9027858,6055359,8215149,5209612,8860957,9902213,9934694,9871726,6682417,4783943,5873171,1848169,5541968,2533311,7717504,4826040,2282229,6903848,3774998,5808466,7116057,4458703,8595365,3873784,2515144,8920470,913311,6503248,6424940,1419853,2907988,3150613,8974251,9833801,698810,2367568,6872640,8360676,8407722,6252129,317047,2115144,4633190,7913149,3593907,8917321,32713,2358459,8924011,4320921,8346272,9783959,6257074,3121015,3428220,8755696,2843719,4370931,4373252,6237766,779215,9931024,8236482,8899677,1828672,4514735,4140299,71767,723257,7490917,6094892,4293634,9124865,3977605,6273024,4735843,1780252,8156996,1635520,9586741,6230597,7206631,4884295,3755525,6357999,9548778,5804945,4167698,5116027,164553,2006201,6179257,8275720,1330585,8475182,6067682,3464453,5295770,8688928,3057702,2609,5438640,8055640,2039251,4596718,6227002,375090,9247001,6638444,1654421,6995647,6438767,1349818,7569989,1895882,3346581,4007311,1738387,4408830,2333855,304695,4561526,5579859,9748412,3795422,6830213,6711955,2739373,5990046,6728646,2363544,6081406,3559121,6255487,8051462,5546319,1843210,6180722,4378020,1519876,8114058,8893800,1497223,7859043,1852854,3200009,8178465,2218781,3479423,7596002,745975,3510765,3278242,1437340,5390129,2471062,5743429,6546068,6437546,2508292,2597239,429133,5821435,8538574,9814957,186571,2446039,4175779,7253126,1516292,9188258,3466600,8706220,6460900,9354482,93033,2643740,1237283,6273157,9533973,578665,5427866,2044443,6270839,2866214,3573596,6253835,9721698,6495293,6177789,7146222,830812,1183135,3080322,98036,2363430,8486941,7211906,8991953,5885249,4050781,8611963,1674703,9569021,2225667,7699913,3588528,6988225,4675791,1538376,5851225,7492837,2335020,1441560,7705070,2506648,4264841,9016024,9712389,8909730,8802975,466160,8575713,2667175,7230638,7500945,1078331,4587853,1735768,86898,266952,8521125,1923682,9712182,3093368,6079181,6344834,4820358,8847988,3351850,5328217,6758013,3811155,5848209,5901459,307361,4787254,1614040,603047,4651540,9618555,4302116,4795259,3726118,1900795,8300883,8963950,3194183,7224128,8605529,287955,8832636,3164,1392904,6432967,5855686,8010241,3263126,5533350,4835118,2992818,2840623,4018528,2460481,2931785,5320994,3102652,1504323,836544,7351302,8795501,3800355,9081652,261761,374522,4036137,4781122,5742247,8283350,6914552,6363036,3641037,8085120,5004989,6897246,9532207,8808660,7038532,8245518,9515418,6893890,927692,6952404,692222,3506409,9669659,58909,7655606,8356179,9450774,605718,841794,1772942,5128269,7091493,4894532,4937537,4179394,5933319,5046472,1797181,4680898,9448837,7699714,1586890,5117798,9762441,5414870,4217738,3924105,9816901,6142356,7211614,2650710,977339,3095800,5383116,7672793,4576376,7375763,385484,9480336,5974207,9439819,1845122,6882107]))
