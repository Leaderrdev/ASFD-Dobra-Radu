# Continut copiat de pe internet 
articol = """Într-o zi frumoasă de primăvară, când soarele strălucea, 
doi prieteni au decis să meargă într-o plimbare. Erau plini de entuziasm 
și voiau să exploreze natura."""

# Impartim sirul in 2 parti egale

lungime = len(articol)
jumatate = lungime // 2
prima_parte = articol[:jumatate]
a_doua_parte = articol[jumatate:]

# Modificari privind prima prima_parte

prima_parte = prima_parte.upper()
prima_parte = prima_parte.strip()

# Modificari privind a_doua_parte

a_doua_parte = a_doua_parte[::-1]
a_doua_parte = a_doua_parte.capitalize() 
import string
a_doua_parte = a_doua_parte.translate(str.maketrans('', '', string.punctuation))

# Combinare prima si a doua parte 

rezultatul_final = prima_parte + " " + a_doua_parte

# Afisarea Rezultatului Final 

print(rezultatul_final)