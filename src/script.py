import time
import pyautogui
import keyboard


# INFO: Récupérer la résolution de l'écran
largeur, hauteur = pyautogui.size()

# INFO: Calculer le centre de l'écran
centre_x = largeur // 2
centre_y = hauteur // 2

def launch_script():
    print("En attente de la touche ALT pour démarrer...")
    # INFO: Attendre l'appui sur ALT
    keyboard.wait('alt')
    print("ALT détecté ! Démarrage de la boucle.")
    time.sleep(1)

    while True:
        
        if keyboard.is_pressed('alt'):
            print("Arrêt du script.")
            break

        # Position souris : X=937, Y=8710
        # pyautogui.click(centre_x, centre_y)
        # print(f"Clic effectué en ({centre_x}, {centre_y})")

        keyboard.press_and_release('e')
        print("Touche 'e' pressée")
        
        time.sleep(5)



def get_mouse_position():
    # pyautogui.displayMousePosition()
    while True:
        keyboard.wait('alt')
        x, y = pyautogui.position()
        print(f"Position souris : X={x}, Y={y}", end="\r")

# get_mouse_position()
launch_script()
