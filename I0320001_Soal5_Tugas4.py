s = "Tembok baruku coklat"
print("panjang dari s = %d" % len(s))

print("Kemunculan pertama a = %d" % s.index("a"))
print("a muncul sebanyak %d kali" % s.count("a"))

print("Lima karakter pertama adalah '%s'" % s[:5]) # Start to 5
print("Lima karakter berikutnya adalah '%s'" % s[5:10]) # 5 to 10
print("Karakter ketiga belas adalah '%s'" % s[12]) #
print("Karakter dengan indeks ganjil adalah '%s'" %s[1::2]) #(0-based indexing)
print("Lima karakter terakhir adalah '%s'" % s[-5:]) # 5th-from-last to end

print("String dalam huruf besar: %s" % s.upper())

print("String dalam huruf kecil: %s" % s.lower())

if s.startswith("Str"):
 print("String dimulai dengan 'Str'. Good!")

if s.endswith("ome!"):
 print("String diakhiri dengan 'ome!'. Good!")

# Pisahkan string menjadi tiga string yang terpisah,
# masing-masing hanya berisi satu kata
print("Pisahkan kata-kata dari string tersebut: %s" % s.split(" "))