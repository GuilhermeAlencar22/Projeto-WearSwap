describe('Teste de login', () => {
    it('deve realizar o login e interagir com o menu', () => {
        cy.visit('https://wearswap.azurewebsites.net/', { failOnStatusCode: false });

        
        cy.get('input[name="username"]').type('teste');
        cy.get('input[name="password"]').type('1234');

        
        cy.get('input[type="submit"]').click();

        
        cy.wait(1000); 

        
        cy.get('.menu-icon').click();


        cy.wait(1000); 


        cy.get('button[type="submit"].button').contains('Configurações').click();;

        cy.wait(1000); 

        cy.on('window:confirm', (text) => {
            expect(text).to.contains('Tem certeza que deseja excluir sua conta?');
            
            return true;
        });

        
        cy.get('button[type="submit"]').contains('Excluir Conta').click();

        
        cy.get('.alert-success').should('contain', 'Conta excluída com sucesso');
        
    });
});


