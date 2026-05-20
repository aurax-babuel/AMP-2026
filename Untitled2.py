#vou fazer outro codigo pq perdi o primeiro...

import random

numero_sorteado = random.randint(1, 10)

for tentativa in range(1, 6):
    palpite = int(input(f"Tentativas {tentativa}/5 - Usuario, por favor digite seu palpite (1 a 10): "))
    
    if palpite == numero_sorteado:
        print("Parabéns usuario.Você acertou!")
        break
        
    elif palpite > numero_sorteado:
        print("O numero é maior usuario!")
    else:
        print("O numero é menor usuario!")
else:
    print(f"Fim de jogo usuario! O número sorteado era {numero_sorteado}.")
    
#Só adicionei o elif e o else pra colocarem as ajudas de maior ou menor, Professora, minha mãe tá brigando cmg... dps eu continuo.