# -*- coding: utf-8 -*-
"""Processamento de Imagens

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13mq1KKvqoigDWbka67fqRO0vX6lVrjjW

## **[Imagem 1](https://http2.mlstatic.com/spitz-alemao-macho-filhote-cachorro-branco-tricolor-babyface-D_NQ_NP_765421-MLB32010092464_082019-F.jpg)**
"""

# Commented out IPython magic to ensure Python compatibility.
import cv2
import matplotlib.pyplot as plt
import numpy as np
# %matplotlib inline

#carregando imagem
img = cv2.imread('Imagem1.jpg', cv2.IMREAD_GRAYSCALE)  
plt.imshow(img, cmap='gray', vmin=0, vmax=255)

#Propriedades da Imagem 
altura, largura = img.shape # altura é o nº de linhas da matriz, largura é o nº de colunas

print('Altura: {} px'.format(altura))
print('Largura: {} px\n\n'.format(largura))
print('Matriz bidimensional da imagem: \n\n', img)

#corte na imagem, selcianando região 
# slice
# imagem[altura/linha inicial:altura/linha final, largura/coluna inicial:largura/coluna final]

roi = img[10:10,70:220]
plt.imshow(roi, cmap='gray', vmin=0, vmax=255)

#rotacionando imagem 
roi_flip_vertical = roi[::-1,::] #imagem[altura/linha inicial:altura/linha final:-1(inverte a leitura), largura/coluna inicial:largura/coluna final:]
roi_flip_horizontal = roi[::,::-1]

plt.figure(figsize=(10,5))

plt.subplot(1,3,1)
plt.title('Original')
plt.imshow(roi, cmap='gray', vmin=0, vmax=255)

plt.subplot(1,3,2)
plt.title('Vertical')
plt.imshow(roi_flip_vertical, cmap='gray', vmin=0, vmax=255)

plt.subplot(1,3,3)
plt.title('Horizontal')
plt.imshow(roi_flip_horizontal, cmap='gray', vmin=0, vmax=255)


plt.tight_layout()

#Normalização da imagem 
#Normalização é o processo de mudar a faixa de valores de intensidade dos pixels de uma imagem. O processo acaba "normalizando" a intensidade para níveis mais naturais.
def normalizacao(img):
    return (img-img.min())/(img.max()-img.min())

img_normalizada = normalizacao(img)

print ("Menor valor de intensidade pré-normalização: {}".format(img.min()))
print ("Maior valor de intensidade pré-normalização: {}".format(img.max()))
print ("Menor valor de intensidade pós-normalização: {}".format(img_normalizada.min()))
print ("Maior valor de intensidade pós-normalização: {}".format(img_normalizada.max()))

