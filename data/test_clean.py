from clean import clean_line
test_lines = [
	"Go. Ve. CC-BY 2.0 (France) Attribution: tatoeba.org #2877272 (CM) & #4986655 (cueyayotl)",
	"Hi. Hola. CC-BY 2.0 (France) Attribution: tatoeba.org #538123 (CM) & #431975 (Leono)",
	"Run! ¡Corre! CC-BY 2.0 (France) Attribution: tatoeba.org #906328 (papabear) & #1685404 (Elenitigormiti)"
]

print("Testing clean_line function:")
for line in test_lines:
	cleaned = clean_line(line)
	print(f"Original: {line}")
	print(f"Cleaned:  {cleaned}")
	print()