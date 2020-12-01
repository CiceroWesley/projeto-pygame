try:
    import pygame
    from abertura import animation
    from uteis import jogo
except:
    print("Erro na importação.")

try:
    pygame.init()
    animation()

    jogo()

except RuntimeError:
    print("O programa abortou antes de terminar.")

except KeyboardInterrupt:
    print("Execução interrompida.")

except:
    print("Erro desconhecido.")