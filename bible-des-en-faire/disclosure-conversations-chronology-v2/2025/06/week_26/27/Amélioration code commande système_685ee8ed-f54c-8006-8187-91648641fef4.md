# Amélioration code commande système

**Date de création :** 2025-06-27 20:54:38

---

**Lucie :**
je me demande si mon code est bon si tu peux l'améliorer je ne vois pas de sortie a chaque fois:

#include "system_handler.h"
#include <string>
#include <array>
#include <memory>
#include <cstdio>

std::string handle_system_command(const std::string& input) {
    std::array<char, 128> buffer;
    std::string result;
    std::unique_ptr<FILE, decltype(&pclose)> pipe(popen(input.c_str(), "r"), pclose);
    if (!pipe) return "[Erreur d'exécution]";
    while (fgets(buffer.data(), buffer.size(), pipe.get()) != nullptr)
        result += buffer.data();
    return result;
}

---

**Lucie :**
comment acceder au bluetooth en ligne de commande?

---

**Lucie :**
comment acceder au wifi depuis le terminal?
