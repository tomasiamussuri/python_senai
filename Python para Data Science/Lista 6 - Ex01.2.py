import keyboard
import time

palavra = ''

while True:
    
    evento = keyboard.read_event()
    print("O evento digitado foi: ", evento)
        
    if evento.event_type == keyboard.KEY_UP:
        letra = evento.name
        time.sleep(2)
        print("A letra digitado foi: ", letra)

        if letra != "space":
            palavra += letra
            print("A palavra é: ", palavra)
            
        else:
            if palavra == "ola":
                print(palavra + " mundo!")
            
            

        
