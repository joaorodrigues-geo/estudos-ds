km = float(input("How many km did you drived?: "))
days = float(input("How many days you had the veicle?: "))
totalprice = (km * 0.15)+ (60 * days)
print("O valor total a pagar por {} dias e {} km é de: {}€".format(days, km, totalprice))