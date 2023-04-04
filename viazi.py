def viazi():
    print("Umechagua viazi")
    print("1. Mbinu bora za kilimo")
    print("2. Mbolea bora na dawa bora za kuua wadudu")
    print("3. Njia bora za uvunaji na uhifadhi")
    taarifa = int(input("Chagua sehemu unayotaka taarifa: "))
    if (taarifa == 1):
        print("Mbinu bora za kilimo cha viazi")
        print("1. Chagua eneo bora la kilimo: Viazi zinahitaji mazingira mazuri ya kilimo ili kustawi vizuri. Eneo bora la kilimo la viazi ni lile lenye udongo wenye rutuba, unyevu wa kutosha na upatikanaji wa mwanga wa kutosha. Epuka maeneo yenye udongo ulio na chumvi nyingi au unyevu mwingi sana. 2. Chagua aina ya mbegu bora: Chagua aina ya mbegu za viazi zenye sifa bora za kilimo. Mbegu bora inapaswa kuwa na mavuno mengi, upinzani wa magonjwa na wadudu, na uwezo wa kuhimili hali ya hewa mbalimbali.")
    elif (taarifa == 2):
        print("Mbolea bora na dawa bora za kuua wadudu wa viazi")
        print("Tumia mbolea kwa kiwango sahihi: Viazi zinahitaji mbolea ya kutosha ili kukua vizuri. Tumia mbolea ya kikaboni au mbolea ya kemikali kulingana na hali ya shamba. Hakikisha unatumia mbolea kwa kiwango sahihi ili kuepuka athari za upungufu au ziada.")
        print("Kudhibiti wadudu na magonjwa: Wadudu na magonjwa yanaweza kuharibu mazao ya viazi. Kutumia dawa za kuua wadudu na magonjwa kwa wakati kunaweza kuepuka athari za wadudu na magonjwa.")
    elif (taarifa == 3):
        print("Njia bora za uvunaji na uhifadhi wa viazi")
        print("Kuvuna kwa wakati: Viazi zinapaswa kuvunwa wakati zimekomaa kabisa. Kuvuna mapema au kuchelewa kunaweza kupunguza mavuno na ubora wa mazao.")
        print("Hifadhi vizuri: Baada ya kuvuna, hifadhi vizuri viazi kwa kuzifunga kwenye mifuko au chombo cha hifadhi. Epuka hifadhi ya viazi")