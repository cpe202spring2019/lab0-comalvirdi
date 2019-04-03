def weight_on_planets():
    weight = int(input('What do you weight on earth?'))

    mars = weight * 0.38
    jupiter = weight * 2.34

    print ('On Mars you would weigh ' + mars+ ' pounds.\n'+'On Jupiter you would weigh '+ jupiter+ ' pounds.'  )
   
   
if __name__ == '__main__':
   weight_on_planets()