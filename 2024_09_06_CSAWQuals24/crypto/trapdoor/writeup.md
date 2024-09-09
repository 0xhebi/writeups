https://ctftime.org/event/2398

# trapdoor (crypto)

You'll need more than 2700 core-years to break this encryption!

## Solution

```python
from math import gcd

c2 = 494623168173341363340467373358957745383595056417571755948370162317759417390186160270770025384341351293889439841723113891870589515038055355274713359875028285461281491108349357922761267441245606066321766119545935676079271349094728585175909045924367012097484771776396598141703907624715907730873180080611197080012999970125893693838478647963157490065546947042621326070901482489910203413759703603136944502613002083194569025640046380564488058425650504612206627739749051853591610981053026318569730551988841304231276711969977298162726941928222523464544797141812329957714866356009363861914935745207975118182966833811723664044706845207847731129336219505772833893718601825819419057471717431953601897992835582033908346998397116046369365580899868759006665351628889935594587647946796811554073758809039163703319444890860711787316692186294350180062910771860180483152240985537326837665737974072086105081591429007858987697382766650868798693024212101169297652870122729568327958629779258375463408029863902774673729692698603549762248768090302360950262068792179771304874203556781584256503067131440856389473604578859795120178476492827306744971082872861030028803971595639553063854220185280566575307797482645881434704155764917254239587927218075951473385530833
n1 = 537269810177819460077689661554997290782982019008162377330038831815573146869875494409546502741769078888560119836988893807659619131795600022996155542011901767164659622251852771410530047820953404275439162903782253582402317577272023052873061733154947413969140900242586288282386516940748102303139488999388815366805771566027048823971232923901589854972341140497344922557809346957285480088567527430942352224246175865278666886538920772608403444601667114300055814252644535406924681931233694920723837668899531758291081568304763353729111948368345349994099868469305792181073122419940610781784779666456780500932337154438538720823939250386789917476722260336949625831449027815346423132208841389383282133423240342633209093536658578807788187537292687621305485734565276685038174693348234827761258142100019798785254244633108887403538365377022084266245064851786520352683721896084403163679116876924559581709943841877168418550922700610256010165841228197765129411475811684669156709601802234298096100301516880419138890353002776631827361005170877640327516465104169299292924318171783865084478980121378972145656688829725118773293892358855082049175572479466474304782889913529927629420886850515337785270820884245044809646784251398955378537462225157041205713008379
n2 = 675112413040615754855341368347991520700645749707972662375138119848808538466484973026629442817490775679486087477873647170707728077849174294413106449041183548981099164777126469098349759962366886352375485394430924686294932854410357033579891793697466117311282071223849125728247324019661552591602816412461639181036083039951358738639409104870090776274099206184327026885209301129700589120263558741373320717866973004474880824451611558352986814186406024139122101780061421498582804842387331594088633719788918481809465044314609904522824483927173924396330723272200351268059583559155873089840203176526189465332287149408627146863937339106591410131104971158916770664709755851365697530033135116269758729627681863469646687585133174854282299126206393656205822175860114547244407037919126445577158000448033562711159480289599400271620922791664179514807098083591794558148460941940996477066832640360820650342057071277962750427121243576612067919616033880922920641430414655749007393524344586517489346008845986135281381956392366857764758769758991862758292829265731964283719870708510272500471228442964550074672417445262035130720875562744233719280755235051883245392409892775011413342074824090752055820699150296553380118608786447588243723987854862785887828651597

p = gcd(n1, n2)
q = n2 // p
phi = (p - 1) * (q - 1)
d = pow(65537, -1, phi)
flag = pow(c2, d, n2)

# csawctf{n0_p0lyn0m1al_t1m3_f4ct0r1ng_n33d3d_t0_0p3n_th1s_tr4pd00r!}
print(flag.to_bytes(length=(flag.bit_length() + 7) // 8, byteorder="big").decode()) 

```

## Flag
`csawctf{n0_p0lyn0m1al_t1m3_f4ct0r1ng_n33d3d_t0_0p3n_th1s_tr4pd00r!}`

smiley 2024/09/07