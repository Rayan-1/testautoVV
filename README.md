# testautoVV

1. De inicio teremos que ter um computador com algum sistema operacional instalado
2. Validando que temos um sistema operacional instalado devemos indetificar qual o sistema opeeracional temos windows? (7,8,10,11), Linux?(Ubuntu,mint,fedora) ou MacOs?
3. Apos indentificarmos o sistema operacional instalado, vamos inciar a intalções das dependencias de cada sistema operacional
4. Vamos Começar instalando o Python
   Windows:
     Instalar o Python:

             Baixe o instalador do Python para Windows no site oficial em https://www.python.org/.
             Execute o arquivo baixado e siga as instruções do instalador.
             Marque a opção "Adicionar Python ao PATH" durante a instalação para que o Python seja adicionado automaticamente ao PATH do sistema.
             python --version
             Isso deve exibir a versão do Python que você acabou de instalar.
             ![image](https://github.com/Rayan-1/testautoVV/assets/69490855/f5fd3f7e-ccdc-415e-896e-79d288ac6f34)
   Instalar um editor de texto ou IDE:

               Baixe e instale um editor de texto ou IDE de sua escolha, como Visual Studio Code, PyCharm ou IDLE.
   Escrever e executar um programa Python:]
   
               Abra o editor de texto ou IDE.
               Crie um novo arquivo e escreva seu código Python.
               Salve o arquivo com a extensão ".py".
               Abra o Prompt de Comando, navegue até o diretório onde o arquivo está salvo e execute o programa com o comando python nome_do_arquivo.py
   Linux:
      Instalar o Python:

       A maioria das distribuições Linux vem com o Python pré-instalado. Você pode verificar digitando o seguinte comando no terminal:
       python3 --version
       ![image](https://github.com/Rayan-1/testautoVV/assets/69490855/d2af3196-6ccb-4cd1-af86-5209ab92e8ec)
       Se o Python não estiver instalado, você pode instalá-lo usando o gerenciador de pacotes da sua distribuição. Por exemplo, no Ubuntu, você pode usar o seguinte comando:
        sudo apt update
        ![image](https://github.com/Rayan-1/testautoVV/assets/69490855/dbe9edaa-39f9-438e-b2b8-51d649795121)

       sudo apt install python3
        ![image](https://github.com/Rayan-1/testautoVV/assets/69490855/fa3c355e-03c3-42f4-8a3a-d4429058d487)

     Instalar um editor de texto ou IDE:

       Você pode instalar um editor de texto ou IDE da mesma forma que faria em um ambiente Windows. Por exemplo, você pode instalar o Visual Studio Code usando o gerenciador de pacotes 
       ou baixar o pacote .deb do site oficial e instalá-lo manualmente.
   
     Abra um editor de texto ou IDE.
           Escreva seu código Python e salve o arquivo com a extensão ".py".
           Abra o terminal, navegue até o diretório onde o arquivo está salvo e execute o programa com o comando python3 nome_do_arquivo.py

     Conseguiu Baixar Tudo?

     se sim, agora vamos instalar o principal, que no caso e a ferramenta do Pytest
     Use o Comando:
       pip install pytest
        Linux
       ![image](https://github.com/Rayan-1/testautoVV/assets/69490855/0eb9bc37-1386-4971-be68-421b4134466d)

       Windows
       ![image](https://github.com/Rayan-1/testautoVV/assets/69490855/b34f0fa3-ab7f-434e-a5d0-fd3ec2947f83)

   Instalou tudo?
   agora vamos para a execução
   clone o repositorio, primeiro copiando o caminho do repos
   ![image](https://github.com/Rayan-1/testautoVV/assets/69490855/6d2ab339-cbd9-4008-938c-176198b53c79)

   depois abra o terminal no seu Sistema operacional e execute
   git clone https://github.com/Rayan-1/testautoVV.git

   ![image](https://github.com/Rayan-1/testautoVV/assets/69490855/c85a8d7c-0adb-4b09-9f2a-ea0522d1deab)

   depois abrar o vs code no seu sistema operacional dentro da pasta do repos
   ![image](https://github.com/Rayan-1/testautoVV/assets/69490855/4a986de6-a3a9-42b3-b846-a772bc03ee24)
   e rode o comando "pytest" para fazer os testes automatizado com a ferramenta pyteste

   lembrando que no windows vc deve ta eum uma IDE, no linux pode ser por linha de comando mesmo




 
   



       




   
