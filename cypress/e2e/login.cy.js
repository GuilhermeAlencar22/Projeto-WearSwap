describe('teste login', () => {
    it('', () => {
        cy.visit('https://wearswap.azurewebsites.net', { failOnStatusCode: false });
        cy.get('input[name="username"]').type('Caio');
        cy.get('input[name="password"]').type('123');
        cy.get('input[type="submit"]').click(); 
        cy.wait(5000); 
       
        
    });
});



