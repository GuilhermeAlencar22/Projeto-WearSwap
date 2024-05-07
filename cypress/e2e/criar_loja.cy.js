import 'cypress-file-upload';

describe('Teste de login', () => {
    it('deve realizar o login e interagir com o menu', () => {
        cy.visit('https://wearswap.azurewebsites.net/', { failOnStatusCode: false });

        
        cy.get('input[name="username"]').type('test2');
        cy.get('input[name="password"]').type('1234');

        
        cy.get('input[type="submit"]').click();

        
        cy.wait(2000); 

        
        cy.get('.menu-icon').click();


        cy.wait(2000); 

        cy.get('a.button').contains('Criar loja').click();

        cy.wait(2000); 

        cy.get('input[name="loja"]').type('WearSwap');
        cy.get('input[name="categoria"]').type('Rodrigo');
        cy.get('input[name="descricao"]').type('Camisa');
        cy.get('input[name="estado"]').type('81999616671');
        cy.get('input[name="preco"]').type('22');

        cy.wait(2000);

        cy.get('input[type="submit"][value="Enviar"]').click();

        cy.wait(2000);


        cy.get('a[href*="ver_loja_criada"]').find('button').click();

        cy.wait(2000);
    

        cy.get('a[href*="ver_item"]').find('button').click();

        cy.get('select[name="tipo_produto"]').select('camisa'); 
        cy.get('select[name="tamanho"]').select('M');
        cy.get('input[name="condicao"]').type('Nova')

        cy.get('textarea[name="descricao"]').type('Uma descrição detalhada do item');

        cy.get('input[name="preco"]').type('100');

        
        const filePath = 'rainbowsix.jpg';
        cy.get('input[type="file"]').attachFile(filePath);

        
        cy.get('form').submit();

        cy.wait(2000);

        cy.contains('a', 'Ver Itens na Loja').click();


    });
});


