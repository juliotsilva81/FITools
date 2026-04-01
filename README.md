# Ferramentas FIT - Edição e Modificação de BIOS

Este repositório contém uma coleção de utilitários e scripts voltados para o **FIT (Flash Image Tool / Firmware Interface Table)**, facilitando a análise, extração, edição e reconstrução de imagens de firmware BIOS/UEFI.

> **🔌 Integração:** Este repositório atua como o motor de ferramentas de baixo nível para a aplicação **JTS_Tool BIOS**, fornecendo os executáveis e scripts necessários para a reparação e modificação automatizada de arquivos de BIOS.

⚠️ **AVISO IMPORTANTE:** A edição e o *flashing* de uma BIOS modificada são procedimentos de alto risco. O uso incorreto destas ferramentas ou a gravação de uma imagem mal configurada pode corromper o firmware e inutilizar (*brick*) a placa-mãe e o equipamento. Todo o conteúdo deste repositório é fornecido "como está", sem garantias. **Use estritamente por sua conta e risco.**

## 🛠️ Funcionalidades

* **Extração e Descompactação:** Separa uma imagem de BIOS completa (ex: `.bin`, `.rom`) em suas respectivas regiões (Descriptor, ME/TXE/SPS, BIOS, GbE, PDR).
* **Modificação de Regiões:** Permite a substituição, injeção ou atualização de módulos específicos, como atualizações do Intel Management Engine (ME) ou Microcodes de CPU.
* **Reconstrução (Rebuild):** Empacota as regiões modificadas de volta em um único arquivo binário válido, pronto para gravação via software ou programadora SPI.
* **Análise e Validação:** Ferramentas para leitura e interpretação do *Firmware Interface Table* e verificação de integridade da imagem.

## 📂 Estrutura do Repositório

* `/bin` - Binários essenciais e ferramentas base para extração e compilação.
* `/scripts` - Scripts de automação (ex: Python/Bash) para agilizar tarefas rotineiras de *modding*.
* `/docs` - Guias detalhados de uso, mapas de memória da SPI e referências de documentação técnica.
* `/exemplos` - Arquivos de configuração (XMLs) e *templates* de uso.

## 🚀 Como Começar

### Pré-requisitos
* Sistema Operacional: Windows ou Linux (verifique a compatibilidade dos binários na pasta `/bin`).
* Python 3.8+ (necessário para rodar os scripts de automação).

### Instalação

1. Clone este repositório para a sua máquina local:
   ```bash
   git clone https://github.com/seu-usuario/ferramentas-fit-bios.git
   cd ferramentas-fit-bios
