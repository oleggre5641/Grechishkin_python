Tour = {
    "Voyage" : {"Мексика", "Канада", "Израиль", "Италия","США"},
    "ReynaTour" : {"Англия", "Япония", "Канада", "ЮАР"},
    "Rainbow" : {"США", "Испания", "Швеция", "Австралия"}
}

Canada = []
USA = []

for tr in Tour.keys():
    if "Канада" in Tour[tr]:
        Canada.append(tr)

for tr in Tour.keys():
    if "США" in Tour[tr]:
        USA.append(tr)


print(f"Канада есть в данных турах : {Canada}\n"
      f"США есть в данных турах : {USA}")