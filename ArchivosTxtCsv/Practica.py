file_path = "D:\Documents\CURSOS1\PYTHON\ArchivosTxtCsv\PracticasCrearFichero.txt"
f = open(file_path, mode = "x")
f.close()

with open(file_path, mode = "w") as f:
  f.write("Muy buenos días, majestad. ")
  f.write("Mi nombre es Pyratilla y soy el capitán de los Pyrates y a continuación procedo a explicar el motivo de nuestra visita a esta majestuosa y bella isla.")
  f.write("\nAntes de entrar en detalle en los motivos de nuestra presencia en su puerto, permítame ponerlo un poco en contexto. ")
  f.write("Hace un tiempo, lo que ya se siente como una eternidad, partimos de Isla Alegre con intención de surcar todos los mares y conocer todas las islas. ")
  f.write("Desde ese día hasta hoy, hemos visitado Isla Arrecife, Isla Espesura, Isla Torva, Isla Verde e Isla Golosa e incluso hemos luchado a muerte contra feroces enemigos. ")
  f.write("A lo que voy es a decir que hemos vivido aventuras inolvidables con el fin de cumplir nuestros sueños: el mío, convertirme en el pirata más famoso de todos los tiempos; el de mi navegante Pyerce, recorrer el mundo surcando los mares; y el de mi timonel Pym, trabajar en el barco que le haría conocer toods los mares y océanos del mundo.")
  f.write("\nPor lo tanto, el motivo de nuestra visita a Isla Lejana es simplemente poder explorarla y así conocerla. ")
  f.write("Como ya habrá deducido, se trata del último destino de nuestra gran aventura. ")
  f.write("Espero que nos permita poner pie en sus dominios, pues sería para nosotros todo un honor.")
  f.write("\nAtentamente, Pyratilla en nombre de los Pyrates.")

  with open(file_path) as f:
    print(f.read())