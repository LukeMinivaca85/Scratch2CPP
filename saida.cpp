#include <iostream>
#include <thread>
#include <chrono>

void tocarSom(const std::string& nomeSom) {
    std::cout << "Tocando som: " << nomeSom << std::endl;
    std::this_thread::sleep_for(std::chrono::seconds(3)); // Simulação
    std::cout << "Som terminou: " << nomeSom << std::endl;
}

int main() {
    std::cout << "Bandeira verde clicada!" << std::endl;
    tocarSom("Lukintosh Unreal Awakening");
    std::cout << "Pressione ENTER para sair...";
    std::cin.get();
    return 0;
}