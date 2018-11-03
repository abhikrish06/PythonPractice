# copied solution
class Solution:
    def subarrayBitwiseORs(self, A):
        # Tabulation is a list of sets, one for each number in A.
        # Each set, at position i, is initialised to containing the element at A[i]
        tabulation = [{A[i]} for i in range(len(A))]
        # print(tabulation)

        # And now we need to go through, updating the sets based on the previous set.
        for i in range(1, len(A)):
            for previous_result in tabulation[i - 1]:
                tabulation[i].add(A[i] | previous_result)

                # Return the number of unique numbers in the tabulation list.
        return len(set.union(*tabulation)) if len(A) > 0 else 0

obj = Solution()
# print(obj.subarrayBitwiseORs([113420779,896107400,92828268,769991745,290611940,904406351,777451070,424384242,658684970,406062998,668165106,962113078,784039066,1748181,493013045,67064862,840700412,368634315,590465192,928142475,228238344,404692700,162443200,6006412,456373150,736296761,620934602,965248622,958851125,984885883,525886399,832261635,980826297,146443878,815320990,217741563,239086780,428303225,73799296,110484788,415231705,959127049,194849624,85057939,80779630,448079509,601259745,566707448,162719409,265828470,534974450,640993950,828116759,943904045,295612903,416377967,431543995,269300645,141774983,47648020,518119196,756700966,413115261,205702615,78130472,273614210,34335562,386980638,259987335,486634675,179893992,313625495,507894840,628321548,879944610,937804436,462287754,271154774,405733258,162528945,456525338,291102433,925407377,186515027,389748395,348434393,999895841,44210862,289014554,809409635,89561646,373954282,213442201,96674582,533922221,301398972,580456390,778086260,411639500,767705753,305582066,497439685,167890011,839770827,593991139,527304874,404027396,892461918,47224569,844152264,525457740,881792826,619530679,274288980,15123928,26482158,309895191,787022215,472775016,755672770,91985330,812646502,853346957,759102925,54402761,549306423,995498830,769987891,643024022,353127293,701443921,997201905,586874309,474829836,353408396,693500433,586427773,924629636,590238769,972584348,145478161,312773230,304306581,120540898,262665495,131971056,74629207,167077931,31619588,758655449,231194336,464497563,389313629,802922943,257421165,54160085,699119677,727870552,73173493,352664533,703007626,183922606,657800318,603461240,853343155,626880003,963971474,318855479,140182549,354449349,675850466,684884375,311693559,520914711,827148472,343424680,995552914,403253701,438668874,72963579,277819525,758709389,383519033,898352618,364928423,341116554,108206548,980817727,472878399,489851845,631338365,737318078,54354919,530872750,115697127,987204952,334045554,460408328,773508941,358292156,508336407,257841024,426156523,823649914,94942053,676791485,312298447,476869199,711350997,532041816,635470130,635172621,432935903,616018077,765463195,591254539,992367201,837225252,149473046,231764785,945088727,59293126,59813292,71860862,237147721,206171094,838763304,602224485,746476494,254886137,629621957,537599342,935623266,824165179,520442399,168284246,262762913,482439667,400686578,744020403,3504730,921998778,603031916,876654909,284239492,984120047,245127128,896600877,998275927,129711781,493005253,378912621,18395524,294445839,293068920,303354591,105605073,599763447,901061628,283402733,630737575,418698793,15167812,880677047,883567019,61752965,802912146,955897323,278784801,168161720,78535888,730833658,902342947,433227271,348097869,755407473,671660080,461964842,536789796,958011752,694439783,913002234,505822060,651561500,189278069,62585446,91189192,178319631,904516917,64127900,4559661,132477043,337516550,818504672,979496732,423298204,953561021,147313204,636420717,663724973,172726497,638911217,993349328,912559732,895950263,517225500,177794178,236327264,959632657,264229835,569176193,148615558,151964834,469940201,291695202,345417769,959294514,861127311,267667749,207983485,116531843,458138178,59410083,541541070,487641800,389910494,29632547,803738996,123788159,128161208,525798711,242845439,905461196,657780036,559161288,425261492,157193428,400598454,901166144,116822944,108051430,289428657,564549841,339899333,468890929,561740140,467861034,970719919,768439551,415016507,226905307,122808638,546150435,39005553,753471644,365024378,862678758,153558531,562401958,485433477,142236357,687086291,539724459,778229427,939135675,779118105,807988674,581004033,474891699,34491959,226065074,652471012,393958445,845509639,340132341,910422311,104051624,800473552,494609881,770431082,239949152,608636231,650734407,757217074,325306349,224112195,1205686,871386868,987965771,547350265,164746943,701694566,719635705,688906840,590057017,356796223,861412347,502056317,355755401,193075050,365538282,166862695,293414793,181798637,199822054,598884830,340795509,590825839,797712880,58155892,343611021,989837914,363438821,922261728,763157677,310727679,213478316,334295612,542369991,454118900,170904526,372971423,859452283,726515524,743966639,991515606,790502325,101460909,452401398,120734291,392445624,563386462,332532248,999312751,346347365,285026534,941168116,26147496,756733629,258468560,801114800,473938566,601916233,33316574,290983105,893335464,304924679,200154734,153607150,696096390,397431803,450536871,298140488,753286896,393487348,244160599,910248594,984676004,96904828,114581093,695717378,815846526,617361021,975679210,138298539,678914881,936045126,44603754,84163422,634567979,335019246,889648065,975674317,534360006,405317211,550298282,592060088,299614675,30143677,376890462,661009608,758889848,707087283,390653934,881598639,821874013,182612466,481495010,964840067,966401177,605895943,943504394,51204444,544413729,133434448,334752624,349500597,434021017,675720848,507485566,310896277,920099850,357460524,977669038,862665826,781261109,285515483,456603377,453418333,71644381,749108695,179820995,620164443,87339760,511561764,591818187,22466941,756980419,884797082,854702560,39751926,217741482,61358326,298665842,923200623,302294776,511579408,276890797,503290102,734576800,941586662,593049903,363234554,697576315,472400093,308204204,700677712,403678723,672298631,932435837,938443014,314249724,656335212,105444808,665955866,539693765,491410871,777224043,622561882,580218740,203616625,455726329,464332702,385283570,382995165,929262339,105213328,891503931,899621329,155580400,548655172,395245624,37023575,375585767,615208237,206777055,97226015,248887329,488183218,272904196,180600369,49542080,907748371,626289692,618759805,541588960,208360316,762624660,33929822,805381055,408277693,168766097,732479025,668425104,881239887,555884301,555891567,95339443,919597742,643494983,195484291,437858206,33324704,704344737,220783822,493169115,108487403,551039142,338405759,834191669,585898907,722256336,446529541,477828506,721171278,826814012,12573185,225746075,834962652,714187040,360011320,103560097,858963867,17453914,73923255,9639664,502844009,714018685,125346257,140586964,382703925,44450795,293084175,281035593,689774051,661943410,180992421,438683619,92243699,203128799,687289044,246610965,851587644,266123117,700084838,709557729,75078993,799756011,272371304,198067435,377564514,583472359,435438803,413775940,606322194,918028097,220542940,143632236,971874537,832937699,360079909,864380344,765619990,477878433,428028329,41424001,603272639,284773089,907110699,185263934,10166758,708831404,825274382,15784913,112782135,858824325,766603386,823927420,717176953,426235865,62856337,533871876,612338013,193307316,459507264,472336403,443006179,36660635,714918313,901350385,640964740,212506843,166629516,191371378,238624579,407157191,55688771,268874525,243892912,805321444,788926125,24130339,852300110,714002453,81857327,822896361,770651798,966609676,666413759,210547395,893910176,311550974,17242346,166453689,590038876,398082098,836644759,980618570,657496902,676337118,666896952,727130958,518226910,191529935,983110557,439498831,783622450,159054381,69342940,769160809,876011808,94442269,578982027,518133007,322624549,840232208,244017095,519107219,169628319,753008955,470026554,433913254,682193154,125991845,924381388,926272617,758087454,719324099,575949890,549450196,786756120,480761205,38566552,708202624,527046371,155499266,856185391,157808817,380659236,109069669,186812611,182195167,28600457,4509147,358416754,39161189,996489140,597414548,636735375,585199059,289353807,263027728,300124271,728928708,3831445,219020280,949316674,701493809,616176032,53280588,985464753,885773728,828552957,118045432,25055000,77252481,380880227,884438668,461627483,733739168,193684462,92322189,310166857,173821354,55016891,688326654,999136057,176089877,951129193,113823257,877071302,423350581,716475606,972916703,115728631,331678071,348776327,362145390,282958498,229389005,200719334,752093344,477737465,873767170,24814928,122871446,874492133,230668039,412438743,567691477,101168718,515699164,990048311,709681508,241981839,767877533,783273202,561941178,878536993,721405375,395492856,947189986,993666396,585792483,281658084,934670279,42470681,167222202,777977615,246576703,466138859,644041705,527971815,166422751,604941229,788108772,300315862,569580313,990758846,630976938,291017165,901697713,114556686,620050821,499506408,415219990,339763698,193939437,427575934,380189426,825947487,78780033,338996818,179869582,904413299,133844371,777421126,143225416,731745520,809676892,776650514,665936391,348261259,389058508,688805516,566768771,832755181,668306278,298222420,475113346,590468380,17960007,11791074,708871437,58213145,449002765,262629344,5348873,546443733,717214218,874787104,805203848,367614899,434683477,78358667,881888628,301669669,351418412,144897974,333186240,701937397,303708274,865461085,229863649,405222822,578198155,877319588,746614338,439718290,456232317,373348771,4002089,724578781,70257309,286009374,63699869,749455331,387825678,271003052,55350758,173212713,953403358,214944804,273299603,91410479,751257857,887011459,986333295,824573829,195156532,910882806,430431795,618682417,416612662,638867359,881120400,184647712,486706614,881803112,305203799,587394708,188879274,550113053,47234033,443032075,424500246,129070579,102035847,839630129,957333942,604394724,153169968,953012311,238766156,162310932,181910101,544753768,161322048,504579689,700611362,136327168,597356643,780360770,574767977,52938424,285553516,1839599,993977492,406484173,532701412,571678385,879424482,104226224,491370680,621278995,329846469,735975681,535927553,622373177,865312658,8125051,307021027,228721060,454800371,924316559,651805172,568791989,501579039,164163549,967644579,375322759,622248427,717415107,118735132,31355414,794739764,957519656,268364085,700137858,526887381,163967943,209662065,935005693,693747822,286448386,963241081,88182172,118708997,29701185,902668813]))
# print(obj.subarrayBitwiseORs([1,2,4]))
print(obj.subarrayBitwiseORs([1,1,2]))
