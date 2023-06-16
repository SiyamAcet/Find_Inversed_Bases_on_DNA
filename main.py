Sequence_1 = "GCTAGGACCTTGATAGAACCATGCATGCATGCATGCAGTCTGGTCACTATGCCGTC"

Sequence_2 = "TACGTATCGGCGTTAGCGTAGCATGCATGCATGCATCGATGCCTAACGTTCTAAGC"


def find_matching_bases(Sequence_1, Sequence_2):
    complement1 = ""
    for base in Sequence_1:
        if base == "A":
            complement1 += "T"
        elif base == "T":
            complement1 += "A"
        elif base == "C":
            complement1 += "G"
        elif base == "G":
            complement1 += "C"
    print("Sequence 1              :", Sequence_1)
    print("Compliment of Sequence 1:", complement1)
    print("")

    complement2 = ""
    for base in Sequence_2:
        if base == "A":
            complement2 += "T"
        elif base == "T":
            complement2 += "A"
        elif base == "C":
            complement2 += "G"
        elif base == "G":
            complement2 += "C"
    print("Sequence 2              :", Sequence_2)
    print("Compliment of Sequence 2:", complement2)
    print("")

    reverse_frontseq1 = complement1[::-1]  # complimenti alınmış birinci DNA'yı ters çevirme Sequence 2 ile karşılaştırmak için ters çevirme
    reverse_Sequence1 = Sequence_1[::-1]  # Sequence 1  DNA dizisini complimenti alınmış Sequence 2 ile karşılaştırmak için ters çevirme

    words1 = []
    worsd2 = []
    words3 = []
    words4 = []

    for i in range(
            len(Sequence_1)):  # bulduğum bu 4 tane dizinin her birini listeye atma (string üzerinde işlem yapamadım neden bilmiyorum çözemedim)
        words1.append(reverse_Sequence1[i])
        worsd2.append(Sequence_2[i])
        words3.append(reverse_frontseq1[i])
        words4.append(complement2[i])

    new_matches1 = []
    new_match1 = []
    new_matches2 = []
    new_match2 = []

    for i in range(len(words1)):
        if words3[i] == worsd2[i]:  # Sequence 2 ile complimentinin ters çevrilmiş hali olan Sequence 1 in baz karşılaştırılması. Eğer bazlar aynıysa new_match1 listesine atılır.
            new_match1.append(words3[i])
        if words3[i] != worsd2[i] and len(new_match1) != 0:  # eğer farklı bir baz gelirse biraraya gelmiş olan anlamlı bazlar new_matches1 listesine atılır. New_matches1 çift boyutlu bir liste.
            new_matches1.append(new_match1)
            new_match1 = []  # listeye atıldıktan sonra new_match1 listesi sıfırlanır.
        if words1[i] == words4[i]:  # Sequence 2'nun compilement hali ile Sequence 1' nın ters çevrilmiş hali kıyaslanır. Eğer aynı bazlar gelirse new_match2 listesine atılıt
            new_match2.append(words1[i])
        if words1[i] != words4[i] and len(new_match2) != 0:  # farklı bir baz gelirse bulununan anlamlı baz new_matches2 listesine atılır ve new_match2 litesi sıfırlanır.
            new_matches2.append(new_match2)
            new_match2 = []
    # print(new_matches2) # Sequence 2 ile aynı sırada gelen bazları yazdırma

    # print(new_matches1) # Sequence 2 'nun complimenti ile aynı sırada gelen bazları yazdırma

    ''' Nükleotit dizisinde aynı sırada gelen diğer nükleotitlerde keşfettim ama en uzun olanını alma kararı aldım. Dilerseniz üsteki iki printi yorum satırından çıkararak görebilirsiniz'''

    largest_list1 = None
    largest_length = 0

    for inner_list in new_matches2:
        length = len(inner_list)
        if length > largest_length:
            largest_length = length
            largest_list1 = inner_list
    largest_list1.reverse()
    list_string = "".join(largest_list1)
    print("The longest base sequence to be inverted on Sequence 1                 :", list_string)
    print("")

    longest_list2 = None
    largest_lenght2 = 0

    for list in new_matches1:
        number_of_elements = len(list)
        if number_of_elements > largest_lenght2:
            largest_lenght2 = number_of_elements
            longest_list2 = list
    new_str = "".join(longest_list2)

    print("The longest base sequence that has undergone an inversion on Sequence 2:", new_str)


find_matching_bases(Sequence_1, Sequence_2)