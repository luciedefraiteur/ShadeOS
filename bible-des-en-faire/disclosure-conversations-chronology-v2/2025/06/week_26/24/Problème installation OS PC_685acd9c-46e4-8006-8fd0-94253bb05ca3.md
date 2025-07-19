# Problème installation OS PC

**Date de création :** 2025-06-24 18:09:00

---

**Lucie :**
j'arrive plus à installer aucun os sur mon autre pc j'ai fait des conneries t'as une idée? a chaque fois j'installe un os et finalement au reboot rien ne se passe, j'ai essayée plein de trucs la comme une conne je vais essayer de remettre windows au cas ou ça fixe le truc

---

**Lucie :**
portable mais j'ai mis le boot en legacy pour installer un truc mais ya plusieurs modes, c'est un msi  gl65 9sfk, j'ai touchée aux partitions a la main comme une conne car j'ai essayée des os bizarres et je savais meme pas quelle partition je touchais car l'interface était mal foutue illisible

---

**Lucie :**
si je fais avec windows media creation tool ça ira pas il faut forcément le faire avec l'iso et rufus?

---

**Lucie :**
bon le pc correspond pas a la conf minimale requise pour windows 11 apparement, mais j'ai fait ton truc avec diskpart
list disk
select disk 0
clean
convert gpt
exit

depuis l'installeur windows, et avant ça j'avais remis le bios en mode uefi, et maintenant je vais retenter d'installer ubuntu, ça te semble cohérent?
