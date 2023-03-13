### Descrição:
API RestFull usando Django e django_rest_framework para simular um ecommerce.

Todas as funcionalidades numeradas abaixo devem ser desenvolvidas para o MVP do projeto.

1. Produtos
    O usuário deve ter acesso a uma rota onde pode buscar os produtos por nome, categoria e id.
    Deverá ter um estoque dos itens, quando o item estiver com 0 unidades deverá ter um campo indicando que o produto está indisponível.
    Caso um usuário tenha um produto no carrinho e ao finalizar a compra este produto estiver indisponível deve retornar um erro indicando que o produto não está mais disponível.
    Ao ser criado um pedido, deve subtrair a quantidade dos produtos do estoque.

2. Carrinho
    Será necessário desenvolver uma model para armazenar os produtos que o usuário selecionou, antes de finalizar a compra.
    Deve conter a lista dos produtos que foram pedidos, com o valor nos items.
    Um pedido não pode ser finalizado se não tiver estoque.
    Se os produtos do carrinho forem de diferentes vendedores, deve ser criado um pedido para cada.
  
3. Pedido
    Associado a cada pedido deve conter seu status PEDIDO REALIZADO, EM ANDAMENTO ou ENTREGUE para acompanhamento do usuário.
    Toda vez que o status do pedido for atualizado deve ser enviado um email ao comprador.
    Deve conter todos os dados dos produtos, menos a quantidade em estoque.
    O vendedor do produto deve conseguir atualizar o status do pedido.
    Deverá conter o horário que o pedido foi feito.
  
4. Endereço
    Usuário deve ter uma relacionamento com um campo de endereço.
  
5. Usuários
    O sistema deve permitir o cadastro de usuários. Deve haver, no mínimo, 3 tipos de usuários:
    Administrador
    Vendedor
    Cliente
    Deve ser possível também usuários não autenticados acessarem a plataforma para visualizar informações sobre os produtos.

6. Funcionalidades do administrador:
    O administrador pode transformar um usuário comum em vendedor.
    O usuário administrador deve ter acesso a todas as rotas.
    
7. Funcionalidades permitidas para os vendedores:
    Cadastrar novos produtos na plataforma.
    Atualizar o estoque do produto.
    Verificar pedidos realizados.
    Deve ter uma rota para visualizar todos os pedidos vendidos.
    Deve ter todos os acessos de um cliente. (O vendedor também pode ser cliente).
    
8. Funcionalidades permitidas para os clientes:
    Pode atualizar o perfil para se tornar vendedor.
    Adicionar produtos ao carrinho.
    Finalizar a compra dos produtos.
    Deve ter uma rota para visualizar todos os pedidos comprados.
  
 ###Diagrama:
    Diagrama de Entidade e Relacionamento Conceitual:
    https://i.imgur.com/0iDwEQr.png

# Instruções:

### Crie o ambiente virtual
python -m venv venv

### Ative o venv:

# git bash:
source venv/Scripts/activate

# linux:
source venv/bin/activate

# windows:
.\venv\Scripts\activate

### Instale as dependências

pip install -r requirements.txt

### Execute as migrações

python manage.py migrate

### Rotas de endpoint:

## Usuários:
/api/users/ -> Cadastro de usuários (admin, cliente, vendedor)
/api/users/ -> Listagem de todos usuários (somente admin)
/api/users/<str:user_id>/ -> Lista, Atualiza e Deleta por id de usuário (somente admin ou usuário dono da conta)

## Login:
/api/users/login/ -> Gera seu Token de autenticação.

## Produtos:
/api/products/ -> Cria um produto (somente vendedor ou admin), Lista todos os produtos (rota livre para todos usuários)
/api/products/<str:product_id>/ -> Lista, Atualiza e Deleta por id de produto (somente admin ou vendedor dono do produto)
/api/products/<str:product_id>/cart/ -> Adiciona um produto ao seu carrinho

## Carrinho:
/api/users/cart/products/ -> Lista meu carrinho de compras
/api/cart/product/remove/<str:product_id>/ -> Remove um produto do meu carrinho de compras

## Pedidos:
/api/orders/ -> Cria meus pedidos
/api/orders/user/ -> Lista meus pedidos comprados
/api/orders/report/ -> Lista os pedidos vendidos por vendedor se usuário for um vendedor e apenas de seus produtos, ou caso admin lista todos os pedidos de vendas de todos os vendedores.
/api/orders/<str:order_id>/ - Atualiza o status de uma ordem de pedido (somente vendedor dono, e admin)




