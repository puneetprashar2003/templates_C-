all_country_name={
1:'afghanistan',
2:'albania',
3 : 'algeria',
4 : 'andorra',
5 : 'angola',
6 : 'antiguaandbarbuda',
7 : 'argentina',
8 : 'armenia',
9 : 'australia',
10 : 'austria',
11 : 'azerbaijan',
12 : 'bahamas',
13 : 'bahrain',
14 : 'bangladesh',
15 : 'barbados',
16 : 'belarus',
17 : 'belgium',
18 : 'belize',
19 : 'benin',
20 : 'bhutan',
21 : 'bolivia',
22 : 'bosniaandherzegovina',
23 : 'botswana',
24 : 'brazil',
25:'brunei',
26:'bulgaria',
27:'burkinafaso',
28:'burundi',
29:'caboVerde',
30:'cambodia',
31:'cameroon',
32:'canada',
33:'car',
34:'chad',
35:'chile',
36:'china',
37:'colombia',
38:'comoros',
39:'congo',
40:'costaRica',
41:'cotedIvoire',
42:'croatia',
43:'cuba',
44:'cyprus',
45:'czechia',
46:'denmark',
47:'djibouti',
48:'dominica',
49:'dominicanrepublic',
50:'ecuador',
51:'egypt',
52:'elsalvador',
53:'equatorialguinea',
54:'eritrea',
55:'estonia',
56:'eswatini',
57:'ethiopia',
58:'fiji',
59:'finland',
60:'france',
61:'gabon',
62:'gambia',
63:'georgia',
64:'germay',
65:'ghana',
66:'greece',
67:'grenada',
68:'guatemala',
69:'guinea',
70:'guineabissau',
71:'guyana',
72:'haiti',
73:'honduras',
74:'hungary',
75:'iceland',
76:'india',
77:'indonesia',
78:'iran',
79:'iraq',
80:'ireland',
81:'israel',
82:'italy',
83:'jamaica',
84:'japan',
85:'jordan',
86:'kazakhstan',
87:'kenya',
88:'kiribati',
89:'kosovo',
90:'kuwait',
91:'kyrgyzstan',
92:'laos',
93:'latvia',
94:'lebanon',
95:'lesotho',
96:'liberia',
97:'libya',
98:'liechtenstein',
99:'lithuania',
100:'luxembourg',
101:'madagascar',
102:'malawi',
103:'malaysia',
104:'maldives',
105:'mali',
106:'malta',
107:'marshallislands',
108:'mauritania',
109:'mauritius',
110:'mexico',
111:'micronesia',
112:'moldova',
113:'monaco',
114:'mongolia',
115:'montenegro',
116:'morocco',
117:'mozambique',
118:'myanmar',
119:'namibia',
120:'nauru',
121:'nepal',
122:'netherlands',
123:'newzealand',
124:'nicaragua',
125:'niger',
126:'nigeria',
127:'northkorea',
128:'northmacedonia',
129:'norway',
130:'oman',
131:'pakistan',
132:'palau',
133:'palestine',
134:'panama',
135:'papuanewguinea',
136:'paraguay',
137:'peru',
138:'philippines',
139:'poland',
140:'portugal',
141:'qatar',
142:'romania',
143:'russia',
144:'rwanda',
145:'saintkittsandnevis',
146:'saintlucia',
147:'saintvincentandthegrenadines',
148:'samoa',
149:'sanmarino',
150:'saotomeandprincipe',
151:'saudiArabia',
152:'senegal',
153:'Serbia',
154:'seychelles',
155:'sierraLeone',
156:'singapore',
157:'slovakia',
158:'slovenia',
159:'solomonIslands',
160:'somalia',
161:'southafrica',
162:'southkorea',
163:'southsudan',
164:'spain',
165:'sriLanka',
166:'sudan',
167:'suriname',
168:'sweden',
169:'switzerland',
170:'syria',
171:'taiwan',
172:'tajikistan',
173:'tanzania',
174:'thailand',
175:'timorLeste',
176:'togo',
177:'tonga',
178:'trinidadandtobago',
179:'tunisia',
180:'turkey',
181:'turkmenistan',
182:'tuvalu',
183:'uganda',
184:'ukraine',
185:'uae',
186:'uk',
187:'usa',
188:'uruguay',
189:'uzbekistan',
190:'vanuatu',
191:'vaticancity',
192:'venezuela',
193:'vietnam',
194:'yemen',
195:'zambia',
196:'zimbabwe',
}
country_name,count='',0
while True :
    print("IF YOU WISH TO CONTINUE (then type y/yes) OTHERWISE (press any key to exit)")
    ask=input()
    if ask=='y' or ask.lower()=='yes' :
        print()
        print("ENTER THE PHRASE OF WORDS AS JUMBLED AS YOU WISH :)")
        print()
        p_name=input("ENTER THE PHRASE : ")
        for k in range(1,197) :
            for j in all_country_name[k] :
                if p_name.count(j)>=all_country_name[k].count(j) :
                    count+=1
            if count==len(all_country_name[k]) :
                print("THE REQUIRED COUNTRY NAME IS : ", all_country_name[k])
            count=0
    else :
        break

