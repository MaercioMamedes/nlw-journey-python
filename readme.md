# NLW Journey Python
## Uma aplicação backend para gerenciar roteiros de viagens

### Apresentação

Esse projeto tem como principais objetivos, intenções educacionais, principalmente no sentido aspecto de implementação de uma API
Web. Ele é o resultado de uma formção técnica oferecida pela Plataforma de ensino de tecnologia [Rocketseat](https://www.rocketseat.com.br/).

Este repositório, é um fork do projeto desenvolvido pelo instrutor do curso, porém estou implentando algumas modificações
em relação à arquitetura e boas práticas. Novas funcionalidades não serão implementadas.

### Descrição

O projeto Journey ajuda o usuário a organizar viagens à trabalho ou lazer. O usuário pode criar uma
viagem com nome, data de início e fim. Dentro da viagem o usuário pode planejar sua viagem adicionando atividades para 
realizar em cada dia.

### Interface
#### [FIGMA](https://www.figma.com/community/file/1392276515495389646)
![](https://efficient-sloth-d85.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F08f749ff-d06d-49a8-a488-9846e081b224%2F10b40153-2c59-4c31-9183-9950cf1314af%2FThumbnail.png?table=block&id=b63aa1fe-9a90-4723-b06b-f078f39b1b1a&spaceId=08f749ff-d06d-49a8-a488-9846e081b224&width=2000&userId=&cache=v2)


### Requisitos Funcionanis

1. O usuário cadastra uma viagem informando o local de destino, data de início, data de término, emails dos convidados e também seu nome completo e endereço de email;
2. O criador da viagem recebe um email para confirmar a nova viagem através de um link. Ao clicar no link, a viagem é confirmada, os convidados recebem e-mail de confirmação de presença e o criador é redirecionado para página da viagem;
3. Os convidados, ao clicarem no link de confirmação de presença, são redirecionados para a aplicação onde devem inserir seu nome(alé, do e-mail que já estará preenchido) e então estarão confirmados na viagem;
4. Na página do evento, os participantes da viagem podem adicionar links importantes da viagem, como reserva no AirBnB, locais para serem visitados, etc;
5. Ainda na página do evento, ocriador e os convidador podem adicionar atividades que irão ocorrer durante a viagem com título, data e horário;
6. Novos participantes podem ser convidados dentro da página do evento através do e-mail e assim devem passar pelo fluxo de confirmação como qualquer outro convidado;


### [Documentação da API como referência](https://nlw-journey.apidocumentation.com/reference)

### Building