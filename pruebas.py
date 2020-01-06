from PIL import Image, ImageFilter
 
#foto = Image.open('./cabify.jpeg')
imagen = Image.open('./cabify.jpeg')
imagen.mode
imagenbn = imagen.filter(ImageFilter.DETAIL)
imagenbn.show()
imagenbn.save('./cabify-gray.jpeg')
#detallar = imagen.filter(ImageFilter.DETAIL)
#datos = foto.getdata()
 
#para el calculo del promedio se utilizara la division entera con el operador de division doble "//" para evitar decimales
 
#promedio = [(datos[x][0] + datos[x][1] + datos[x][2]) // 3 for x in range(len(datos))]
 
#imagen_gris = Image.new('L', foto.size)
 
#imagen_gris.putdata(promedio)
 
#imagen_gris.save('./cabify_gray.jpeg')
 
#foto.close()
 
#imagen_gris.close()




























# from PIL import Image
#from PIL import EpsImagePlugin

#filename = 'cabify.jpeg'
#def open_eps(filename, dpi):
#    img = Image.open(filename)
 #   print(img)
  #  original = [float(d) for d in img.size]
    # scale = width / original[0] # calculated wrong height
   # scale = dpi/72.0            # this fixed it
    #if dpi is not 0:
     #   img.load(int(scale))
    #if scale != 1:
     #   img.thumbnail([round(scale * d) for d in original], Image.ANTIALIAS)
    #return img

#img = open_eps(filename, 300.0)
#img.save('cabify1.png', (300.0, 300.0))