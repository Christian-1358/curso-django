Guia Definitivo de Ubuntu para Devs Iniciantes

Baseado no vídeo: O Guia DEFINITIVO de UBUNTU para Devs Iniciantes (Fabio Akita)

1. Filosofia e Conceitos Fundamentais

1.1. Por que aprender Linux?

Ambiente dos servidores: Quase a totalidade da infraestrutura web moderna (Nuvem, AWS, GCP, Azure, Docker, Kubernetes) roda sobre distribuições Linux.

Mentalidade de desenvolvedor: Entender o sistema operacional por baixo dos panos evita a dependência de interfaces gráficas e traz autonomia na resolução de problemas.

Produtividade via Terminal: O CLI (Command Line Interface) permite automação, script de rotinas e execução rápida de tarefas complexas.

1.2. O que é o Linux?

Kernel vs. Distribuição:

Kernel: O núcleo do sistema operacional criado por Linus Torvalds em 1991. Gerencia hardware, memória, processos e I/O.

Distro (Distribuição): O Kernel empacotado junto a utilitários GNU, gerenciadores de pacote, servidores de exibição (Display Servers) e ambientes de trabalho (Desktop Environments). Ex: Ubuntu, Debian, Fedora, Arch Linux.

Ubuntu: Baseado em Debian, focado em facilidade de uso, forte suporte da comunidade e ciclos previsíveis de lançamento (versões LTS com 5 anos de suporte).

2. Estrutura de Arquivos no Linux (FHS - Filesystem Hierarchy Standard)

No Linux não existem letras de unidade como C:\ ou D:\. Tudo deriva do diretório raiz / (Root).

/ : Root (raiz do sistema).

/home/$USER : Diretório pessoal do usuário. Onde ficam seus documentos, projetos e configurações locais.

/bin e /usr/bin : Binários essenciais do sistema e executáveis de programas instalados.

/sbin e /usr/sbin : Binários do sistema voltados para administração.

/etc : Arquivos de configuração global do sistema e serviços.

/var : Dados variáveis de sistemas e programas (logs em /var/log, bancos de dados, filas).

/tmp : Arquivos temporários (limpos na reinicialização).

/opt : Softwares adicionais e pacotes de terceiros compilados manualmente.

/dev : Dispositivos de hardware mapeados como arquivos.

/proc e /sys : Sistemas de arquivos virtuais contendo informações do Kernel e processos em tempo real.

3. Comandos Essenciais do Terminal CLI

3.1. Navegação e Manipulação de Arquivos

# Saber em qual diretório você está no momento
pwd

# Listar arquivos e diretórios
ls
ls -la           # Lista detalhada (-l), incluindo arquivos ocultos (-a)

# Navegação
cd /caminho      # Navega para o diretório
cd ~             # Vai direto para o /home do usuário
cd ..            # Sobe um nível no diretório

# Criação e Remoção
mkdir nome_pasta # Cria uma pasta
mkdir -p p1/p2   # Cria estrutura de pastas aninhadas
touch arquivo.txt# Cria arquivo vazio ou atualiza timestamp
rm arquivo.txt   # Deleta arquivo
rm -rf pasta/    # Deleta pasta e seu conteúdo recursivamente (CUIDADO!)
cp orig dest     # Copia arquivo ou diretório (-r para diretórios)
mv orig dest     # Move ou renomeia arquivo/diretório

# Leitura e Exibição
cat arquivo.txt  # Exibe todo o conteúdo
less arquivo.txt # Navegação paginada pelo conteúdo
head -n 10 file  # Exibe as primeiras 10 linhas
tail -n 10 file  # Exibe as últimas 10 linhas
tail -f log.log  # Acompanha alterações no arquivo em tempo real


3.2. Permissões de Arquivos (POSIX)

Cada arquivo/diretório no Linux possui 3 tipos de permissão:

r (read - leitura) = 4

w (write - escrita) = 2

x (execute - execução) = 1

E 3 classes de controle:

u (user - proprietário)

g (group - grupo)

o (others - outros)

# Alterar permissões
chmod +x script.sh       # Torna o arquivo executável
chmod 755 script.sh      # rwxr-xr-x (Dono: 7, Grupo: 5, Outros: 5)
chmod 600 id_rsa         # rw------- (Apenas leitura/escrita para o dono)

# Alterar proprietário e grupo
sudo chown usuario:grupo arquivo.txt


4. Gerenciamento de Pacotes e Programas

4.1. APT (Advanced Package Tool - Ubuntu/Debian)

# Atualizar a lista de repositórios
sudo apt update

# Atualizar os pacotes instalados para as versões mais recentes
sudo apt upgrade -y

# Buscar por um pacote
apt search nome_pacote

# Instalar um pacote
sudo apt install nome_pacote -y

# Remover um pacote
sudo apt remove nome_pacote
sudo apt purge nome_pacote   # Remove o pacote e seus arquivos de configuração
sudo apt autoremove          # Limpa dependências que não são mais necessárias


4.2. Snaps e Flatpaks

Formatos de empacotamento isolados (containerizados) para distribuição universal no Linux.

Snap: Padrão da Canonical/Ubuntu.

sudo snap install code --classic   # Instalação do VS Code via Snap


5. Shell: Bash, Zsh e Variáveis de Ambiente

5.1. O que é o Shell?

O interpretador de comandos que recebe o input do usuário e envia para o sistema executar. O padrão do Ubuntu é o bash, mas muitos devs utilizam o zsh com repositórios como o Oh My Zsh.

5.2. Arquivos de Configuração (.bashrc / .zshrc)

Localizados no diretório /home/$USER/. São executados sempre que um novo terminal é aberto.

5.3. Variável PATH

Instrui o sistema sobre onde procurar arquivos executáveis ao digitar um comando no terminal.

# Adicionar um diretório customizado ao PATH (exemplo no .bashrc ou .zshrc)
export PATH="$HOME/bin:$HOME/.local/bin:$PATH"


5.4. Aliases (Atalhos de comandos)

# Exemplos de aliases úteis para adicionar no arquivo de configuração do shell:
alias gs="git status"
alias update="sudo apt update && sudo apt upgrade -y"


6. Configuração do Ambiente de Desenvolvimento (Dev Environment)

6.1. Ferramentas Essenciais de Compilação

sudo apt install build-essential curl wget git -y


build-essential: Pacote que inclui o compilador gcc, g++, make e bibliotecas necessárias para compilar código fonte.

6.2. Configuração Básica do Git

git config --global user.name "Seu Nome"
git config --global user.email "seuemail@exemplo.com"
git config --global core.editor "code --wait" # Ou vim, nano


6.3. Chaves SSH para GitHub / GitLab / Servidores

# Gerar chave SSH Ed25519 (mais segura e moderna)
ssh-keygen -t ed25519 -C "seuemail@exemplo.com"

# Iniciar o agent do SSH e adicionar a chave
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

# Exibir a chave pública para colar no GitHub/GitLab
cat ~/.ssh/id_ed25519.pub


6.4. Gerenciadores de Versão de Linguagens (Recomendados)Guia Definitivo de Ubuntu para Devs Iniciantes

Baseado no vídeo: O Guia DEFINITIVO de UBUNTU para Devs Iniciantes (Fabio Akita)

1. Filosofia e Conceitos Fundamentais

1.1. Por que aprender Linux?

Ambiente dos servidores: Quase a totalidade da infraestrutura web moderna (Nuvem, AWS, GCP, Azure, Docker, Kubernetes) roda sobre distribuições Linux.

Mentalidade de desenvolvedor: Entender o sistema operacional por baixo dos panos evita a dependência de interfaces gráficas e traz autonomia na resolução de problemas.

Produtividade via Terminal: O CLI (Command Line Interface) permite automação, script de rotinas e execução rápida de tarefas complexas.

1.2. O que é o Linux?

Kernel vs. Distribuição:

Kernel: O núcleo do sistema operacional criado por Linus Torvalds em 1991. Gerencia hardware, memória, processos e I/O.

Distro (Distribuição): O Kernel empacotado junto a utilitários GNU, gerenciadores de pacote, servidores de exibição (Display Servers) e ambientes de trabalho (Desktop Environments). Ex: Ubuntu, Debian, Fedora, Arch Linux.

Ubuntu: Baseado em Debian, focado em facilidade de uso, forte suporte da comunidade e ciclos previsíveis de lançamento (versões LTS com 5 anos de suporte).

2. Estrutura de Arquivos no Linux (FHS - Filesystem Hierarchy Standard)

No Linux não existem letras de unidade como C:\ ou D:\. Tudo deriva do diretório raiz / (Root).

/ : Root (raiz do sistema).

/home/$USER : Diretório pessoal do usuário. Onde ficam seus documentos, projetos e configurações locais.

/bin e /usr/bin : Binários essenciais do sistema e executáveis de programas instalados.

/sbin e /usr/sbin : Binários do sistema voltados para administração.

/etc : Arquivos de configuração global do sistema e serviços.

/var : Dados variáveis de sistemas e programas (logs em /var/log, bancos de dados, filas).

/tmp : Arquivos temporários (limpos na reinicialização).

/opt : Softwares adicionais e pacotes de terceiros compilados manualmente.

/dev : Dispositivos de hardware mapeados como arquivos.

/proc e /sys : Sistemas de arquivos virtuais contendo informações do Kernel e processos em tempo real.

3. Comandos Essenciais do Terminal CLI

3.1. Navegação e Manipulação de Arquivos

# Saber em qual diretório você está no momento
pwd

# Listar arquivos e diretórios
ls
ls -la           # Lista detalhada (-l), incluindo arquivos ocultos (-a)

# Navegação
cd /caminho      # Navega para o diretório
cd ~             # Vai direto para o /home do usuário
cd ..            # Sobe um nível no diretório

# Criação e Remoção
mkdir nome_pasta # Cria uma pasta
mkdir -p p1/p2   # Cria estrutura de pastas aninhadas
touch arquivo.txt# Cria arquivo vazio ou atualiza timestamp
rm arquivo.txt   # Deleta arquivo
rm -rf pasta/    # Deleta pasta e seu conteúdo recursivamente (CUIDADO!)
cp orig dest     # Copia arquivo ou diretório (-r para diretórios)
mv orig dest     # Move ou renomeia arquivo/diretório

# Leitura e Exibição
cat arquivo.txt  # Exibe todo o conteúdo
less arquivo.txt # Navegação paginada pelo conteúdo
head -n 10 file  # Exibe as primeiras 10 linhas
tail -n 10 file  # Exibe as últimas 10 linhas
tail -f log.log  # Acompanha alterações no arquivo em tempo real


3.2. Permissões de Arquivos (POSIX)

Cada arquivo/diretório no Linux possui 3 tipos de permissão:

r (read - leitura) = 4

w (write - escrita) = 2

x (execute - execução) = 1

E 3 classes de controle:

u (user - proprietário)

g (group - grupo)

o (others - outros)

# Alterar permissões
chmod +x script.sh       # Torna o arquivo executável
chmod 755 script.sh      # rwxr-xr-x (Dono: 7, Grupo: 5, Outros: 5)
chmod 600 id_rsa         # rw------- (Apenas leitura/escrita para o dono)

# Alterar proprietário e grupo
sudo chown usuario:grupo arquivo.txt


4. Gerenciamento de Pacotes e Programas

4.1. APT (Advanced Package Tool - Ubuntu/Debian)

# Atualizar a lista de repositórios
sudo apt update

# Atualizar os pacotes instalados para as versões mais recentes
sudo apt upgrade -y

# Buscar por um pacote
apt search nome_pacote

# Instalar um pacote
sudo apt install nome_pacote -y

# Remover um pacote
sudo apt remove nome_pacote
sudo apt purge nome_pacote   # Remove o pacote e seus arquivos de configuração
sudo apt autoremove          # Limpa dependências que não são mais necessárias


4.2. Snaps e Flatpaks

Formatos de empacotamento isolados (containerizados) para distribuição universal no Linux.

Snap: Padrão da Canonical/Ubuntu.

sudo snap install code --classic   # Instalação do VS Code via Snap


5. Shell: Bash, Zsh e Variáveis de Ambiente

5.1. O que é o Shell?

O interpretador de comandos que recebe o input do usuário e envia para o sistema executar. O padrão do Ubuntu é o bash, mas muitos devs utilizam o zsh com repositórios como o Oh My Zsh.

5.2. Arquivos de Configuração (.bashrc / .zshrc)

Localizados no diretório /home/$USER/. São executados sempre que um novo terminal é aberto.

5.3. Variável PATH

Instrui o sistema sobre onde procurar arquivos executáveis ao digitar um comando no terminal.

# Adicionar um diretório customizado ao PATH (exemplo no .bashrc ou .zshrc)
export PATH="$HOME/bin:$HOME/.local/bin:$PATH"


5.4. Aliases (Atalhos de comandos)

# Exemplos de aliases úteis para adicionar no arquivo de configuração do shell:
alias gs="git status"
alias update="sudo apt update && sudo apt upgrade -y"


6. Configuração do Ambiente de Desenvolvimento (Dev Environment)

6.1. Ferramentas Essenciais de Compilação

sudo apt install build-essential curl wget git -y


build-essential: Pacote que inclui o compilador gcc, g++, make e bibliotecas necessárias para compilar código fonte.

6.2. Configuração Básica do Git

git config --global user.name "Seu Nome"
git config --global user.email "seuemail@exemplo.com"
git config --global core.editor "code --wait" # Ou vim, nano


6.3. Chaves SSH para GitHub / GitLab / Servidores

# Gerar chave SSH Ed25519 (mais segura e moderna)
ssh-keygen -t ed25519 -C "seuemail@exemplo.com"

# Iniciar o agent do SSH e adicionar a chave
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

# Exibir a chave pública para colar no GitHub/GitLab
cat ~/.ssh/id_ed25519.pub


6.4. Gerenciadores de Versão de Linguagens (Recomendados)

Evite instalar linguagens de programação (Node.js, Python, Ruby) diretamente via apt global do sistema para evitar conflitos de versão. Use versionadores por usuário:

Node.js: nvm ou fnm

Python: pyenv / asdf

Ruby: rbenv ou rvm

Multi-linguagem: asdf-vm ou mise

7. Produtividade e Ferramentas CLI Recomendadas

Vim / Neovim: Editor de texto direto no terminal para edições rápidas de arquivos de configuração.

htop / btop: Monitoramento de recursos (CPU, Memória, Processos) em tempo real.

tmux: Multiplexador de terminal (permite dividir telas e manter sessões rodando em segundo plano).

curl / wget: Ferramentas para download e requisições HTTP via linha de comando.

Docker: Criação e execução de ambientes isolados via containers.

8. Principais Boas Práticas e Recomendações

Nunca use sudo indiscriminadamente: Apenas execute como sudo (root) comandos de alteração de sistema/instalação de pacotes globais. NUNCA rode o seu projeto, npm install ou pip install usando sudo.

Entenda as mensagens de erro: O terminal fornece diagnósticos claros. Sempre leia as saídas no console antes de buscar soluções.

Faça do terminal seu aliado: Aprenda os atalhos do teclado:

Ctrl + C: Interrompe a execução do processo atual.

Ctrl + Z: Envia o processo atual para background.

Ctrl + R: Busca no histórico de comandos anteriores.

Ctrl + L: Limpa a tela (equivalente ao comando clear).

Tab: Autocompleta caminhos e comandos.

Resumo elaborado para referência rápida de estudo e consulta contínua.

Evite instalar linguagens de programação (Node.js, Python, Ruby) diretamente via apt global do sistema para evitar conflitos de versão. Use versionadores por usuário:

Node.js: nvm ou fnm

Python: pyenv / asdf

Ruby: rbenv ou rvm

Multi-linguagem: asdf-vm ou mise

7. Produtividade e Ferramentas CLI Recomendadas

Vim / Neovim: Editor de texto direto no terminal para edições rápidas de arquivos de configuração.

htop / btop: Monitoramento de recursos (CPU, Memória, Processos) em tempo real.

tmux: Multiplexador de terminal (permite dividir telas e manter sessões rodando em segundo plano).

curl / wget: Ferramentas para download e requisições HTTP via linha de comando.

Docker: Criação e execução de ambientes isolados via containers.

8. Principais Boas Práticas e Recomendações

Nunca use sudo indiscriminadamente: Apenas execute como sudo (root) comandos de alteração de sistema/instalação de pacotes globais. NUNCA rode o seu projeto, npm install ou pip install usando sudo.

Entenda as mensagens de erro: O terminal fornece diagnósticos claros. Sempre leia as saídas no console antes de buscar soluções.

Faça do terminal seu aliado: Aprenda os atalhos do teclado:

Ctrl + C: Interrompe a execução do processo atual.

Ctrl + Z: Envia o processo atual para background.

Ctrl + R: Busca no histórico de comandos anteriores.

Ctrl + L: Limpa a tela (equivalente ao comando clear).

Tab: Autocompleta caminhos e comandos.

Resumo elaborado para referência rápida de estudo e consulta contínua.