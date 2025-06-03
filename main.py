import json

with open('project.json', encoding='utf-8') as f:
    projeto = json.load(f)

codigo_cpp = """#include <iostream>
#include <thread>
#include <chrono>

void tocarSom(const std::string& nomeSom) {
    std::cout << "Tocando som: " << nomeSom << std::endl;
    std::this_thread::sleep_for(std::chrono::seconds(3)); // Simulação
    std::cout << "Som terminou: " << nomeSom << std::endl;
}

int main() {
    std::cout << "Bandeira verde clicada!" << std::endl;
"""

# Busca pelos blocos do Sprite1
sprite = next(t for t in projeto['targets'] if not t['isStage'])
blocos = sprite['blocks']

for id_bloco, bloco in blocos.items():
    if bloco['opcode'] == 'sound_playuntildone':
        id_som = bloco['inputs']['SOUND_MENU'][1]
        nome_som = blocos[id_som]['fields']['SOUND_MENU'][0]
        codigo_cpp += f'    tocarSom("{nome_som}");\n'

codigo_cpp += '    std::cout << "Pressione ENTER para sair...";\n'
codigo_cpp += '    std::cin.get();\n'
codigo_cpp += "    return 0;\n}"


with open('saida.cpp', 'w', encoding='utf-8') as f:
    f.write(codigo_cpp)

print("✅ Código C++ gerado em 'saida.cpp'")
