#Usando Ribeirão Preto como ponto de referencia, a equação horaria será

velCarro = 110
velCaminhao = 80
distancia = 100

tempo = distancia / velCaminhao
posiCarro = velCarro * tempo

#A equação do caminhão, por ir no sentido contrario assume valor negativo'''
posiCaminhao = -velCaminhao * (tempo + 0.17) #Equivalente a 10 min
velMediaCaminhao = distancia / (tempo + 0.17)

#A poisção em que os carros se cruzam é definida pela seguinte equação
posiFinal = (velCarro * distancia) / (velCarro + velMediaCaminhao)

print(f'Ambos os carros estarão a uma distância de {posiFinal:.2f} km de Ribeirão Preto')
print("Não é posivel que um esteja mais perto pois eles estão no mesmo ponto ao se cruzarem na via")
