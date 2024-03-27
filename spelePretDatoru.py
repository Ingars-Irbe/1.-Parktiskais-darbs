import random
#Klase, kas atbilst vienai virsotnei spēles kokā
class Virsotne:
    
    #Klases konstruktors, kas izveido virsotnes eksemplāru
    #Katrā virsotnes eksmeplārā glabājas virsotnes unikāls identifikators (id), skaitliskā virkne (virkne)
    #pirmā spēlētāja punkti (p1), otrā spēlētāja punkti(p2), un virsotnes atrašanās līmeņa numurs
    #Glabātie dati tiek padoti kā konstruktora argumenti
    def __init__(self, id, virkne, p1, p2, limenis):
        self.id=id
        self.virkne=virkne
        self.p1=p1
        self.p2=p2
        self.limenis=limenis

#Klase, kas atbilst spēles kokam        
class Speles_koks:
    
    #Klases konstruktors, kas izveido spēles koka eksemplāru
    #Spēles koka eksemplārs ietver sevī virsotņu kopu, kas tiek veidota kā Python saraksts un
    #loku kopu, kas tiek veidota kā Python vārdnīca (dictionary)
    #Gan virsotņu kopa, gan loku kopa sākotnējie ir tukšas
    #Virsotņu kopā glabāsies virsotnes viena aiz otras
    #Loku kopā glabāsies virsotnes unikāls identifikators kā vārdnīcas atslēga (key) un
    #ar konkrētu virsotni citu saistītu virsotņu unikālie identifikatori kā vērtības (values)
    def __init__(self):
        self.virsotnu_kopa=[]
        self.loku_kopa=dict()
    
    #Klases Speles_koks metode, kas pievieno spēles kokam jaunu virsotni, kuru saņem kā argumentu
    def pievienot_virsotni(self, Virsotne):
        self.virsotnu_kopa.append(Virsotne)
        
    #Klases Speles_koks metode, kura papildina loku kopu, saņemot kā argumentus
    #virsotnes identifikatoru, no kuras loks iziet, un virsotnes identifikatoru, kurā loks ieiet
    def pievienot_loku(self, sakumvirsotne_id, beiguvirsotne_id):
        self.loku_kopa[sakumvirsotne_id]=self.loku_kopa.get(sakumvirsotne_id,[])+[beiguvirsotne_id]

#Gājiena funkcija, kurā tiek atrasta nākamā virsotne atkarībā no spēlētāja lēmuma
def gajiena_parbaude (gajiena_tips,generetas_virsotnes,pasreizeja_virsotne):
    
    
    #Pārbauda vai virknē ir palikuši skaitļi
    if len(pasreizeja_virsotne[1]) > 0:
        
        #Izveido saraksta kopiju, lai neveidotos autsauce uz orģinālo sarakstu
        new_virkne = pasreizeja_virsotne[1].copy()
        
        pasreizejais_speletajs = (pasreizeja_virsotne[4] % 2) + 1 # Speletajs 1 vai 2
        

        #Atkarībā no spēlētāja izvēles veic vienu vai otru gājienu, kurā tiek saglabāts skaitlis 
        #no labās vai kreisās puses, un izņemts tas no saraksta.
        if gajiena_tips == '1':
            punkti = new_virkne.pop(0)
        else:
            punkti = new_virkne.pop()
        
        #Atkarībā no koka līmeņa nosaka, kuram spēlētājam ir gājiens, un no viņa atņem punktus
        if pasreizejais_speletajs == 1:
            new_p1 = pasreizeja_virsotne[2]
            new_p2 = pasreizeja_virsotne[3] - punkti
        else:
            new_p1 = pasreizeja_virsotne[2] - punkti
            new_p2 = pasreizeja_virsotne[3]
        
        #Izmantojot globālo mainīgo veido unikālu ID
        global j
        new_id='A'+str(j)
        j+=1
        
        #pieskaita jaunu līmeni
        new_limenis = pasreizeja_virsotne[4]+1

        #izveido virsotni
        new_virsotne=Virsotne(new_id, new_virkne, new_p1, new_p2, new_limenis)

        #Cikls kurš pārbauda vai jaunā virsotne jau iepriekš tika ievietota virsotņu kopā. Ja jā tad to izlaiž, ja nē tad to  pievieno virsotņu kopai. 
        parbaude=False
        i=0
        while (not parbaude) and (i<=len(sp.virsotnu_kopa)-1):
            if (sp.virsotnu_kopa[i].virkne==new_virsotne.virkne) and (sp.virsotnu_kopa[i].p1==new_virsotne.p1) and (sp.virsotnu_kopa[i].p2==new_virsotne.p2) and (sp.virsotnu_kopa[i].limenis==new_virsotne.limenis):
                parbaude=True
            else:
                i+=1   
        if not parbaude:
            sp.pievienot_virsotni(new_virsotne)
            generetas_virsotnes.append([new_id, new_virkne, new_p1, new_p2, new_limenis])
            #Izveido savienojumu starp pašreizējo virsotni un jauno virsotni
            sp.pievienot_loku(pasreizeja_virsotne[0],new_id)  
        else:
            j-=1
            #Izveido savienojumu starp pašreizējo virsotni un nākamo virsotni, kura jau eksistē
            sp.pievienot_loku(pasreizeja_virsotne[0],sp.virsotnu_kopa[i].id)

#tiek izsaukts spēles koka konstruktors, lai izveidotu tukšu koku        
sp=Speles_koks()
#tiek izveidots tukšs ģenerēto virsotņu saraksts
generetas_virsotnes=[]
#tiek izveidota un uzģenerēta virkne
gen_virkne = []
  #ievada virknes garumu

while True:
    try:
        daudzums = int(input("Virknes garums(15-25): "))
        if (daudzums >= 15 and daudzums <= 25):
            break
        else:
            print("Ievadīts nepareizsvirknes garums. Mēģinat vēlreiz")
    except:
        print("Nav ievadīts skaitlis. Mēginat vēlreiz")
    
    
for i in range(daudzums):
        gen_virkne.append(random.randint(1,3))

#tiek izveidota sākumvirsotne spēles kokā
sp.pievienot_virsotni(Virsotne('A1', gen_virkne, 80, 80, 1))
#tiek pievienota pirmā virsotne ģenerēto virsotņu sarakstam
generetas_virsotnes.append(['A1', gen_virkne, 80, 80, 1])
#mainīgais, kurš skaita virsotnes
j=2
#kamēr nav apskatītas visas saģenerētas virsotnes viena pēc otras
while len(generetas_virsotnes)>0:
    #par pašreiz apskatāmo virsotni kļūst pirmā virsotne saģenerēto virsotņu sarakstā
    pasreizeja_virsotne=generetas_virsotnes[0]
    
    pasreizejais_speletajs = (pasreizeja_virsotne[4] % 2) + 1 #Nosaka pašreizējo spēlētāju (1 vai 2)
    if (pasreizejais_speletajs == 1):
        print("Datora gājiens!")
    else:
        print("Spēlētāja gājiens!") #Izprintē pašreizējā spēlētāja gājienu.
    
    print("Pašreizējā virkne: ", pasreizeja_virsotne[1]) #Izprintē pašreizējo skaitļu virkni.
    
    
    if pasreizejais_speletajs == 1:
        gajiena_tips = random.choice(['1', '2'])
        if (gajiena_tips == 1):
            print("Dators izņem ciparu no kreisās puses")
        else:
            print("Dators izņem ciparu no kreisās puses")
    else:
        #Liek spēlētajam izvēlēties pusi no kuras izņemt skaitli
        while True:
            gajiena_tips = input("Ievadi '1', lai izņemt ciparu no kreisās puses, '2' no labās: ")
            if gajiena_tips in ['1', '2']:
                break
            else:
                print("Nepareiza ievade. Mēģinat vēlreiz")
    
   
            
    #tiek pārbaudīts gājiens
    gajiena_parbaude(gajiena_tips,generetas_virsotnes,pasreizeja_virsotne)
    
    #kad visi gājieni no pašreiz apskatāmās virsotnes ir apskatīti, šo virsotni dzēš no ģenerēto virsotņu saraksta
    generetas_virsotnes.pop(0)

# Pārbauda kuram spēlētājam ir vairāk punkti => tas arī uzvar.
if pasreizeja_virsotne[2] > pasreizeja_virsotne[3]:
    print(f"Spēlētājs uzvar ar {pasreizeja_virsotne[2]} punktiem!")
else:
    print(f"Dators uzvar ar {pasreizeja_virsotne[3]} punktiem!")
    
# Liel lietotājam izvēlēties vai tas vēlas redzēt spēles virsotņu un loku kopas
while True:
    paradit_virsotnes = input("Vai vēlaties apskatīt spēles virsotnes un lokus? [Y/N]: ")
    if paradit_virsotnes in ['y', 'Y']:
        for x in sp.virsotnu_kopa:
            #Tiek izvadīta spēles koka virsotņu kopa
            print(x.id,x.virkne,x.p1,x.p2,x.limenis)
        for x, y in sp.loku_kopa.items():
            #Tiek izvadīta spēles koka loku kopa
            print(x, y)
    if paradit_virsotnes in ['n', 'N']:
        break
    else:
        pass