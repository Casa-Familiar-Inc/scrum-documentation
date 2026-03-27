Este sandbox server sirve como UAT el cual tiene reestriccion de acceso a internet, usando simplewall que es un firewall a nivel aplicacion, y unicamente debemos de dejar libre la API de appfolio para que el sincronizador entre appfolio y quickbooks pueda llamar a la API.

1. entrar al servidor 
2. El servidor se encuentra en 192.168.0.68 el cual es VNQB-SERVER
3. Abrir virtualbox 
4. ![[Pasted image 20260323145447.png]]

Usar QB-Isolated-QB-PreInstallation unicamente
Esta maquina virtual esta ligada a QB-Isolated por favor no eliminar ninguna de las dos maquinas virtuales.
Nota:
QB-Isolated-QB-PreInstallation es un estado de QB-Isolated previo a la instalacion de Quickbooks ya que se usara una version de QB sin licencia sin desarrollo que unicamente es valida por 30 dias
5. Este archivo se encuentra en C:\Users\nefil\OneDrive\Documents\Casa-Familiar-Sandbox-File y el Instalador de QB
6. ![[Pasted image 20260323152812.png]]
7. Esta imagen muestra la maquina virtual QB-Isolated-PreQB con el Estado Pre-QB, en ese estado ya se encuentran todas las configuraciones listas, excepto QB
8. Se instala QB y se usa el archivo de la compania.
9. ![[Pasted image 20260323153146.png]]
10. Se comparten las credenciales a Dancing Numbers: user: dancing-numbers, password: 12345678
11. El internet esta bloqueado por defecto para la cuenta de dancing numbers.
12. ![[Pasted image 20260323153418.png]] 
13. para usuario administrador - usuario: admin, password: CasaF@2026 es un local user
14. a dancing numbers se le invitara a usar la VPN tailscale
15. El sistema de VPN esta administrado con Tailscale
16. Tailscale es un software que esta instalado en el sandbox UAT para QB 
17. ![[Pasted image 20260323154003.png]]
18. https://login.tailscale.com/uinv/i3eoGdyebi11VwJTaTNs221
19. Una vez que el cliente de tailscale este configurado se puede usar RDP unicamente con el hostname qb-sandbox o la ip mostrada este sistema se llama ZERO TRUST ya que no expone ningun puerto publico a internet se crea una intranet.
20. Para el firewall usamos SimpleWall es un pequeno software gratuito que funciona mejor que el firewall nativo de windows,
21. ![[Pasted image 20260323154218.png]]
Aqui tenemos la opcion de dar permisos a ciertos software y servicios, siempre vamos a dar acceso a simplewall.exe, svhost y system para que RDP pueda funcionar.
En caso de que queramos permitir la navegacion permitimos msedge.exe unicamente dando click en el checkbox, otro software importante es tailscaled.exe y tailscaled-ipn.exe para que funcione la red Zero Trust.

Ya teniendo la configuracion de RPD y Tailscale en nuestro local podemos conectarnos con el escritorio remoto.
tambien podemos conectarnos al servidor VNQB-SERVER y administrar usando VirtualBox,
las instancias tienen snapshots, recomiendo unicamente usar 


Explicar como es el flujo del snapshot es unicamente en QB-Isolated-PreQB
El snapshot a eliminar el Pre-QB y  justamente despues de eliminar se tiene que crear uno nuevo.

QB-Isolated-PreQB es un clone ligado de QB-Isolated-1
y explica segun a la imagen

![[Pasted image 20260324131556.png]]