describe('Teste de login', () => {
    it('deve realizar o login e interagir com o menu', () => {
        cy.visit('https://wearswap.azurewebsites.net/', { failOnStatusCode: false });

        
        cy.get('input[name="username"]').type('Caio');
        cy.get('input[name="password"]').type('123');

        
        cy.get('input[type="submit"]').click();

        
        cy.wait(5000); 

        
        cy.get('.menu-icon').click();


        cy.wait(5000); 


        cy.get('button[type="submit"].button').contains('Configurações').click();;


        cy.wait(5000); 


        cy.get('div.config-option').contains('Alterar Senha').click();

        cy.wait(5000);

        cy.get('input[name="senha_antiga"]').type('123');
        cy.get('input[name="nova_senha"]').type('5678');
        cy.get('input[name="confirmar_nova_senha"]').type('5678'); 

        cy.get('button[type="submit"]').contains('Salvar').click();

        cy.wait(5000); 

        cy.get('button[type="submit"]').contains('Salvar').click();



        cy.wait(5000); 





        
    });
});


