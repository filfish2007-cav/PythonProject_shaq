# # task 1
# import random
#
# vlasni = set(map(int,input("VVedy chisla cheres comu ").split(",")))
#
# randomni = set(random.randint(1,100) for x in range(12))
#
# print("Maks znach vvedenyh: ",max(vlasni))
#
# print("Min znach vvedenyh: ",min(vlasni))
#
# print("Kilkist vlasnyh: ", len(vlasni))
#
# print("Unikalni vvedeni: ", vlasni - randomni)
#
# print("Spilni: ", vlasni.intersection(randomni))
#
# print("Vsi: ", vlasni | randomni)
# # task 2
# gosti = ["Oleg", "Denys", "Anton", "Mykola", "Grygoriy", "Denys"]
# nazva = "New Year party"
#
# def invite(spisok,svyato):
#     spisok=set(spisok)
#     for guest in spisok:
#         print(f"I invite you {guest}, to {svyato}")
#
# invite(gosti,nazva)
# # task 3
# person1_list = ["молоко", "хліб", "сир", "яблука", "кава"]
# person2_list = ["яблука", "банани", "сир", "вода", "печиво"]
#
# def shopping(persha,druga):
#     persha = set(persha)
#     druga = set(druga)
#
#     print("Tovary razom:", persha.intersection(druga))
#     print("Tovary lyshe pershiy:", persha.difference(druga))
#     print("Tovary lyshe druga:", druga.difference(persha))
#
# shopping(person1_list,person2_list)
# # task 4
# registered = ["Олексій", "Марія", "Іван", "Олена", "Дмитро", "Анна"]
# paid = ["Марія", "Іван", "Максим", "Анна", "Сергій"]
# confirmed = ["Іван", "Анна", "Максим", "Тетяна", "Олексій"]
#
# def hto_ye_hto(zareg,oplata,present):
#     zareg = set(zareg)
#     oplata = set(oplata)
#     present = set(present)
#
#     print("Registered but not paid: ", zareg-oplata)
#
#     print("Present but not registered: ", present-zareg)
#
#     print("Paid but not present: ", oplata-present)
#
#     print("Registered and paid: ", zareg & oplata)
#
#     print("Present,paid and registered: ", present & zareg & oplata)
#
# hto_ye_hto(registered,paid,confirmed)
# # task 5
all_employees = ["Артем", "Богдан", "Віра", "Гліб", "Денис", "Емма", "Женя", "Зоя"]
group_monday = ["Артем", "Богдан"]
group_tuesday = ["Віра", "Гліб", "Денис"]
group_wednesday = ["Емма", "Женя", "Денис"]

def perevirka(vsi,ponedilok,vivtorok,sereda):
    vsi = set(vsi)
    ponedilok = set(ponedilok)
    vivtorok = set(vivtorok)
    sereda = set(sereda)

    print("Ti kogo zabyly: ", vsi-ponedilok-vivtorok-sereda)
    print("To hto v dvoh grupah: ",ponedilok & vivtorok, ponedilok & sereda, sereda & vivtorok)

perevirka(all_employees,group_monday,group_tuesday,group_wednesday)


