Fisikako Gradu Amaierako Lana: Prozesu estokastikoak fisikan eta ekonomian
============================

Orrialde honetan, Fisikako GRALerako garatutako kode guztia aurkitu daiteke. 

## Edukia

### Higidura browndarra

Lehenengo atalean, independenteak diren partikula browndarren multzo bat eraikitzen da. Kasu sinpleenetik hasten gara, 2D eta 3Dko simulazio estatikoak irudikatuz. Kodea ondo idatzita dagoen ziurtatzeko, partikula-multzoak, esperimentalki, emaitza teoriko jakin batzuk betetzen dituen aztertuko dugu. 

Simulazioa ondo burutu dela ziurtatzean, eraiki den kasu ideal horri zenbait propietate gehituko zaizkio: 

1. Partikula ez-independenteak simulatuko dira. Beraien arteko elkarrekintza simulatzeko, Lennard-Jones-en potentziala sartu da. 
2. Horrez gain, hasieratze-funtzio bat ere gehitu da (ordutik aurrera bi partikulek ezin izango dute bolumen bera okupatu). 
3. Azkenik, mugalde baldintza periodikoak ere ezarri dira (fisikako hainbat ikasgaitan orokortasunik galdu gabe egin dugun bezala). 


### Jito-indarpeko higidura browndarra

Oraingoan, partikula browndak dauden jariakinari jito-indar bat gehitu zaio. Izan ere, errealitatean behatzen diren eta browndartzat har daitezkeen partikulek, oro har, jito-indar bat jasan dezakete (eta hortaz, zilegi da Langevin-en ekuazioetan jito-indarra ereduztatuko duen indar bat gehitzea). Behin ere, kodea ondo dagoen frogatzeko, difusio-konstantea eta Einstein-en erlazioa kalkulatzen dira. 

### Merkatu-ereduak

Atal honetan, eta Yamada _et al._ -en artikuluari jarraituz, prozesu estokastikoetan oinarritutako bi merkatu-eredu eraikiko dira. Merkatu-eredu sinpleenari A Eredua deituko zaio eta hemen _partaide_ estokastikoaren ideia aurkeztuko da. Partaide hori, merkatuan parte hartzen duen edozein negoziatzaile izan daiteke: enpresa bat, banakako merkataria, negoziatzailea, gobernua, familia edo banku zentrala. Eta _estokastiko_ deritzo, esparru estokastiko bat erabiliz, modu baliokide batean modelizatu daitekeelako eragile ekonomiko horietako bakoitzak ekonomian duen esku-hartzea. Hortaz, merkatu-eredua osatzen duten osagai guztiak  _partaide estokastikoak_ izango dira, eta hauen arteko elkarrekintza aztertuko da.

Ondoren, ikusiko da, A Eredua ez dela merkatu errealetan behatzen den funtsezko propietate enpiriko bat erreproduzitzeko gai, partikula browndarren multzoarekin gertatzen zen bezala. Partikula browndarrek, errealitatean, norabide batean barreiatzean, zentzu _hobetsi_ bat izan dezakete. Eta eredua errealistago bilakatzeko helburuarekin, jito-indar konstante bat sartu zen. Prozedura berdina jarraituz ekonomiaren esparru honetan, beste efektu bat gehituko zaio A Ereduari, B Eredura helduz, lehenengoaren bertsio hobetua, eta errealitatetik hurbilago egongo dena. 

## Irakurlearentzako oharrak

- Orri honen helburua Fisikako GRALerako idatzi den kodea era argian aurkeztea da.
- Orrialde estatikoa denez, emaitza estatikoak baino ez dira aurkeztu liburu honetan. Animazioak exekutatzeko, github-eko _Jupyter notebook_ -a zuzenean exekutatzea iradokitzen da.
- Atal oro, hainbat azpiatalez osatuta dago. Bakoitzean, kodea ulertzeko lagungarriak izan daitezkeen azalpen laburtuak daude. Azalpen horien helburua ez da, inondik inora ere, kodean eta bere deskribapenean oinarritutako lan bat aurkeztea. Iruzkin gehienak ikaspen prozesuaren parte izan dira eta, agian, irakurleari lagun diezaioketenez, argibide gisa utzi dira. 
- _Notebook_ -ak berriro exekutatu dira _Book_ hau sortzeko. Prozesu estokastikoekin dihardugunez, irudi batzuk GRALean aurkeztutakoen ezberdinak izan daitezke. Gainera, erresoluzioa jaitsi zaie liburua errazago sortzeko.
- FORTRANen idatzi diren moduluak ezin dira era honetan publikatu. _Jupyter Book_ bateko edukia _Jupyter Notebook_ -ez edota _markdown_ fitxategiez osatuta egon behar da. Beraz, _.f95_ -en idatziriko modulua ezin da aurkeztu. Hala ere, nire github-era igo ditut.
